"""Create/reuse a private connector and test it. Requires the mistralai SDK.

MISTRAL_API_KEY authenticates to Mistral. BALL_RANKS_API_KEY is optional.
Never prints either credential. Does not invoke a language model.
"""
import asyncio
import json
import os


async def main():
    key = os.environ.get("MISTRAL_API_KEY")
    if not key:
        raise SystemExit("MISTRAL_API_KEY is required; no connector was created.")
    from mistralai.client import Mistral
    client = Mistral(api_key=key)
    name = "ball-ranks-private-review"
    try:
        connector = await client.beta.connectors.get_async(connector_id_or_name=name)
    except Exception as error:
        if getattr(error, "status_code", None) != 404:
            raise
        connector = await client.beta.connectors.create_async(
            name=name,
            description="Published fantasy football and basketball rankings and projections.",
            server="https://ballranks.com/api/mcp",
            visibility="private",
        )
    if connector.server != "https://ballranks.com/api/mcp" or connector.visibility != "private":
        raise SystemExit("Existing connector differs from the private Ball Ranks configuration; no changes made.")
    headers = {}
    if os.environ.get("BALL_RANKS_API_KEY"):
        headers["Authorization"] = "Bearer " + os.environ["BALL_RANKS_API_KEY"]
    # Mistral requires user credentials even for anonymous connections.
    await client.beta.connectors.create_or_update_user_credentials_async(
        connector_id_or_name=name, name="ball-ranks-review", credentials={"headers": headers}, is_default=True,
    )
    tools = await client.beta.connectors.list_tools_async(connector_id_or_name=name)
    names = {tool.name for tool in tools}
    expected = {"get_week_rankings", "get_season_rankings", "get_player_rankings", "get_player_projections"}
    if names != expected:
        raise SystemExit("Discovered tool names differ from the expected four tools.")
    print("Private connector discovered all four Ball Ranks tools.")
    result = await client.beta.connectors.call_tool_async(
        connector_id_or_name=name, tool_name="get_season_rankings", arguments={"sport": "basketball", "limit": 5},
    )
    if getattr(result, "is_error", False):
        raise SystemExit("Tool returned an error; inspect it securely in Studio before recording a demo.")
    data = getattr(result, "structured_content", None)
    if not isinstance(data, dict):
        for item in result.content:
            if getattr(item, "text", None):
                try:
                    candidate = json.loads(item.text)
                    if isinstance(candidate, dict) and "rankings" in candidate:
                        data = candidate
                        break
                except json.JSONDecodeError:
                    continue
    if not isinstance(data, dict) or len(data.get("rankings", [])) != 5 or not data.get("sourceUrl"):
        raise SystemExit("Expected five rankings and a source URL; inspect the result securely in Studio.")
    print("Mistral returned five basketball rankings and a source URL. Host conversations remain to be tested.")


if __name__ == "__main__":
    asyncio.run(main())

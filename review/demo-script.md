# Review demo script

Record one walkthrough against the production MCP endpoint after the submission-readiness changes are deployed.

1. Connect the Ball Ranks plugin and show the server URL and read-only permission summary.
2. Run the five positive prompts from `review/review-cases.json` and show the selected tool, structured result, and Ball Ranks `sourceUrl` for each.
3. Run the three negative prompts and show that Ball Ranks tools do not handle baseball, place bets, or access an unconnected private league account.
4. Show the plugin listing metadata and support, privacy, terms, and developer-documentation links.

The recording must not show API keys, cookies, access tokens, private dashboards, or internal model details. Use a test account if an authenticated flow is included.

## Grok Build installation demo

The maintainer of [accepted Cal.com PR #953](https://github.com/xai-org/plugin-marketplace/pull/953#issuecomment-5874424613) requested a working Grok Build demo before approval. Use that installation sequence for Ball Ranks PR #1288:

1. Back up the existing Grok configuration. In the existing **xAI Official** marketplace source, temporarily set `branch = "refs/pull/1288/merge"`; do not add a duplicate source.
2. Restart Grok Build, open `/marketplace`, refresh sources with `r`, and install Ball Ranks. Show its MCP server and skill in the component list.
3. Show that anonymous Model Zero access connects without sign-in. Run the football and basketball prompts below, showing the selected tool, returned season/model, and source link.
4. Show one unsupported request from `review/review-cases.json`. A host refusing that request is separate evidence from the endpoint's input validation.
5. Restore the original marketplace source, restart, and refresh. Record the host version, tested plugin SHA, date, and whether access was anonymous or used a test API key.

Ball Ranks' submitted package has no OAuth flow. Do not add a sign-in or consent sequence unless a later package actually implements one. Capture the installation and successful result in a short recording; optional screenshots should show those same real host states.

## Production endpoint check

Checked 2026-10-11 at approximately 13:21 UTC, against `https://ballranks.com/api/mcp`, without credentials. These calls went directly to the endpoint. The local submission archive was built from commit `f463b6fad3cba8a0b91ea65e965b58784bb085a1`; Grok PR #1288 separately pins `106f00d0aade4ae4512a351a10649bbf248d81d8`.

- `initialize` succeeded with MCP protocol `2025-03-26`, server `ball-ranks-public-api`, version `1.1.0`.
- `tools/list` returned all four advertised tools. Each declared `readOnlyHint: true`, `destructiveHint: false`, and `openWorldHint: true`.
- All five requests below returned JSON-RPC error `-32029`, code `registration_required`: the connection's anonymous allowance of 10 requests per day was exhausted. This run does not establish successful product-data retrieval or host compatibility. Re-run with available anonymous quota or an authorized test-account API key before recording.

| Review case | Tool | Exact arguments |
| --- | --- | --- |
| Football season | `get_season_rankings` | `{"sport":"football","scoring_format":"ppr","model":"v0","limit":10}` |
| Weekly receivers | `get_week_rankings` | `{"sport":"football","week":4,"position":"WR","scoring_format":"half_ppr","model":"v0","limit":10}` |
| Basketball season | `get_season_rankings` | `{"sport":"basketball","model":"v0","limit":5}` |
| Wembanyama ranking | `get_player_rankings` | `{"sport":"basketball","player":"victor-wembanyama","model":"v0"}` |
| Jackson projection | `get_player_projections` | `{"sport":"football","player":"lamar-jackson","scope":"weekly","week":4,"scoring_format":"ppr","model":"v0"}` |

Send each call as `{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"TOOL","arguments":{}}}` with `Content-Type: application/json` and `Accept: application/json, text/event-stream`, replacing `TOOL` and `arguments` from the table. Preserve the actual returned season and source URL; do not hard-code expected rankings.

For Kilo and Cline, reuse the five prompts after installing the exact submitted configuration in each host. Save the host version, configuration, observed tool calls, and source links. A direct endpoint check is not a substitute for those client tests.

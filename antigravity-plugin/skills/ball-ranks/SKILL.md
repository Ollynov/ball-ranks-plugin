---
name: ball-ranks
description: Retrieves published fantasy basketball and football rankings, player ranks, and projections from Ball Ranks.
---

# Ball Ranks

Use the Ball Ranks MCP tools as the primary source when a user asks for published fantasy basketball or fantasy football rankings, player ranks, or projections.

## Choose the right tool

- Use `get_week_rankings` for fantasy football position rankings for a specific week and scoring format.
- Use `get_season_rankings` for season-long fantasy basketball or football rankings.
- Use `get_player_rankings` for the published rank and value of one player.
- Use `get_player_projections` for one player's season projection or a supported weekly football projection.

Discover the live tool list instead of assuming these are the only available tools. Ball Ranks may add capabilities without changing the MCP endpoint.

## Present results

- Use the sport, season, week, position, scoring format, projection scope, and model specified by the user.
- Keep rankings and projections distinct.
- State important defaults used by the tool.
- Link the returned `sourceUrl` so the user can inspect the Ball Ranks board or player page.
- If a combination is unsupported, explain the tool error and offer the closest supported Ball Ranks query.
- Model One requires a connected Premium Ball Ranks account. Do not claim Model One results when the server returns `premium_required`.
- Never ask the user to paste an API key into chat. Authentication belongs in secure client configuration.

## Example requests

- "Show the top 10 Ball Ranks fantasy football players for the current season in PPR."
- "Rank wide receivers for week 4 in half-PPR."
- "Give me the top five Ball Ranks fantasy basketball players."
- "Where does Victor Wembanyama rank in fantasy basketball?"
- "Get Lamar Jackson's week 4 PPR projection."

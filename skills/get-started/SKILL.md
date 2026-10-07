---
name: get-started
description: Use Ball Ranks for published fantasy basketball and football rankings and player projections.
---

# Ball Ranks

Use the Ball Ranks MCP tools when the user asks for published fantasy basketball or football rankings, player rank, or player projections.

## Choose a tool

- Use `get_week_rankings` for a ranked fantasy football position list for one week and scoring format.
- Use `get_season_rankings` for a basketball or football season board.
- Use `get_player_rankings` when the user asks where one player ranks.
- Use `get_player_projections` for one player's season projection or supported weekly football projection.

The current MCP release starts with these four read-only tools and will expand. Always use the tools the live server advertises instead of assuming this list is complete.

## Present results

- State the sport, season, scope, scoring format, and selected Ball Ranks model when they affect the answer.
- Preserve the distinction between a rank and a projection.
- Link the returned `sourceUrl` so the user can open the relevant Ball Ranks board or player page.
- If a requested sport and scope combination is unavailable, explain the supported alternative returned by the server.
- Never ask the user to paste an API key into chat. Authentication belongs in the client's secure connection flow.


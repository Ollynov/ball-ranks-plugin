# Ball Ranks plugin

Ball Ranks provides published fantasy basketball and football rankings and player projections through a read-only remote MCP server.

This repository packages the same live server for ChatGPT and Codex, Claude, Gemini CLI, Grok Build, Muse Code, and other Agent Plugins or MCP-compatible clients. The initial MCP surface contains four tools; clients discover the live tool list so Ball Ranks can add capabilities without changing the server URL.

## Server

- MCP endpoint: `https://ballranks.com/api/mcp`
- Developer documentation: `https://ballranks.com/developers`
- OpenAPI: `https://ballranks.com/openapi.json`
- Support: `https://ballranks.com/support`
- Privacy: `https://ballranks.com/privacy`
- Terms: `https://ballranks.com/terms`

## Install

Clients that support Agent Plugins can install this repository directly. Platform-native manifests are also included:

- `plugin.json` and `mcp.json`: Agent Plugins, ChatGPT, and Codex
- `server.json`: Official MCP Registry
- `.codex-plugin/plugin.json`: Codex local plugin compatibility
- `.claude-plugin/plugin.json` and `.mcp.json`: Claude Code and Grok Build
- `gemini-extension.json`: Gemini CLI

No API keys are stored in this repository. Anonymous Model Zero access works with lower request limits. Ball Ranks API keys can be created at `https://ballranks.com/account#developer-access` for account-level limits; clients must store credentials securely.

## Current tools

- `get_week_rankings`
- `get_season_rankings`
- `get_player_rankings`
- `get_player_projections`

All tools are read-only and return structured content plus a canonical `sourceUrl`.

## Support

Email `help@ballranks.com` or visit `https://ballranks.com/support`. Never include passwords, sign-in cookies, or full API keys in a support request.

## License

The packaging files and skill instructions in this repository are available under the MIT License. Ball Ranks data and services remain subject to the Ball Ranks Terms of Service.

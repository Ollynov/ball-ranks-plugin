# Ball Ranks plugin

Ball Ranks provides published fantasy basketball and football rankings and player projections through a read-only remote MCP server.

This repository packages the same live server for ChatGPT and Codex, Claude, Google Antigravity, Gemini CLI, Grok Build, Muse Code, and other Agent Plugins or MCP-compatible clients. The initial MCP surface contains four tools; clients discover the live tool list so Ball Ranks can add capabilities without changing the server URL.

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
- `antigravity-plugin/`: Google Antigravity 2.0, CLI, and IDE
- `gemini-extension.json` and `GEMINI.md`: enterprise and paid API-key Gemini CLI installations

No API keys are stored in this repository. Anonymous Model Zero access works with lower request limits. Ball Ranks API keys can be created at `https://ballranks.com/account#developer-access` for account-level limits; clients must store credentials securely.

### Google Antigravity

Google moved unpaid and Google One Gemini CLI users to Antigravity CLI on June 18, 2026. Clone this repository, then install the native package from its dedicated directory:

```sh
agy plugin install ./antigravity-plugin
```

Inside the Antigravity CLI, the equivalent command is:

```text
/plugin install ./antigravity-plugin
```

The package installs as `ball-ranks`, connects to the production MCP endpoint through `serverUrl`, and includes a focused Ball Ranks skill. Run `agy plugin list` and open `/mcp` to verify that the plugin and server loaded.

For a workspace-only Antigravity 2.0 or IDE installation, copy the package directory to `.agents/plugins/ball-ranks/`. For a global installation, copy it to `~/.gemini/config/plugins/ball-ranks/`.

Marketplace publication is separate from the package. Google currently asks publishers to complete its [Antigravity Marketplace interest form](https://forms.gle/2EX5RFYPoJe1UgxR9).

### Gemini CLI (enterprise and API-key installations)

Install directly from the public repository:

```sh
gemini extensions install https://github.com/Ollynov/ball-ranks-plugin
```

Restart Gemini CLI after installation, then run `/extensions list` and `/mcp` to confirm that `ball-ranks` and its live tools are available. `GEMINI.md` gives Gemini concise tool-selection and response guidance. This package remains for enterprise and paid API-key Gemini CLI installations.

The public gallery discovers repositories automatically. This repository is public, has the `gemini-cli-extension` GitHub topic, and keeps `gemini-extension.json` at the repository root. No separate gallery submission is required.

## Current tools

- `get_week_rankings`
- `get_season_rankings`
- `get_player_rankings`
- `get_player_projections`

All tools are read-only and return structured content plus a canonical `sourceUrl`.

## Review material

`review/review-cases.json` contains the five positive and three negative cases used for platform review. `review/demo-script.md` is the shared walkthrough plan. Run both against production after any tool-contract change.

## Support

Email `help@ballranks.com` or visit `https://ballranks.com/support`. Never include passwords, sign-in cookies, or full API keys in a support request.

## License

The packaging files and skill instructions in this repository are available under the MIT License. Ball Ranks data and services remain subject to the Ball Ranks Terms of Service.

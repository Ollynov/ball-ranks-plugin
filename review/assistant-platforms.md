# Assistant review preparation

Verified 2026-10-11 against public package commit `f202c44` and the production MCP server. This is technical preparation, not a record of submitted forms or successful host conversations.

## Shared listing and reviewer answers

- Name: Ball Ranks Fantasy Sports (publisher and website brand stay Ball Ranks).
- Publisher/support: Ball Ranks, `help@ballranks.com`.
- Description: Published fantasy basketball and football rankings and player projections.
- Repository: https://github.com/Ollynov/ball-ranks-plugin
- Endpoint/transport: `https://ballranks.com/api/mcp`, Streamable HTTP.
- Documentation: https://ballranks.com/developers
- Support: https://ballranks.com/support
- Privacy: https://ballranks.com/privacy
- Terms: https://ballranks.com/terms
- Icon: `assets/icon.png`; dark icon: `assets/icon-dark.png`.
- Intended users: adult fantasy basketball and football players comparing published player rankings and projections.
- Added value: structured, paginated ranking data with explicit sport, scoring, model, season/week and source links. Reviewers can compare results without extracting tables from rendered pages.

| Tool | Inputs | Output |
| --- | --- | --- |
| `get_week_rankings` | Week 1–18; optional football position, season, scoring, model, limit/offset | Ranked football position list and projected points |
| `get_season_rankings` | Sport; optional season, scoring, model, limit/offset | Ranked football or nine-category per-game basketball list |
| `get_player_rankings` | Sport, player ID/slug; optional season, scoring, model | One player's season ranking |
| `get_player_projections` | Sport, player ID/slug; optional scope, season, week, scoring, model | Season projection or weekly football projection |

All four tools retrieve published data. None edits rosters, connects a private league, places a bet, sends a message, or processes payment. Their production annotations are `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`, `openWorldHint: true`. Titles, output schemas, source/support links and `noauth` tool metadata are live.

Authentication: public Model Zero (`v0`) accepts no credentials. Optional Ball Ranks keys use `Authorization: Bearer <key>` where a host accepts headers. Model One (`v1`) requires Premium. These keys are not OAuth tokens; this package declares no OAuth flow or scopes. Keep real keys outside manifests, screenshots and recordings.

Limits documented by the product: anonymous 50/day per observed IP; Free account 8/minute and 80/day; Premium account 60/minute and 1,000/day. Product requests also pass a 60/minute IP guard; MCP discovery has a separate 300/minute guard. Shared platform egress can combine anonymous users' usage. After HTTP 429, respect `Retry-After` and report the error without inventing rankings. An invalid/revoked key is unauthorized; unsupported sport/week/scoring combinations require clarification or a supported request.

Reviewer procedure:

1. Connect the HTTPS endpoint with anonymous authentication, or use a dedicated test key where supported.
2. Run `node scripts/check-production-mcp.mjs`; expect initialization and exactly four tools.
3. Run `node scripts/check-production-mcp.mjs --data`; this exercises the five positive requests in `review/review-cases.json` and exits unsuccessfully for blocked/missing data. A quota error stops further calls.
4. In each actual host conversation, run all five positive and three negative prompts from that file. Capture the selected tools, returned values/source URLs and refusal or clarification behavior. Direct HTTP checks do not prove model tool selection.
5. Record installation, authentication choice, successful football/basketball requests and failure handling using `review/demo-script.md`.

### Data-processing questionnaire draft

Tools receive sports/player query parameters and return public product data. The server processes request metadata and an API key/account identifier when provided for authentication, quotas and security. It does not request private fantasy-league data through these four tools.

The [published privacy policy](https://ballranks.com/privacy#public-api-and-mcp) states that Supabase stores key metadata and rate counters; Vercel processes traffic/operational logs. Keys are stored as one-way hashes. Rate counters use salted one-way actor hashes, with deletion targeted within 48 hours. Key metadata remains until account deletion, subject to security/legal exceptions. Users can revoke keys in their account and request deletion through support. Backup copies may persist temporarily. These are policy statements; this review did not audit production provider log retention or verify deletion jobs.

Before submitting a legal questionnaire, the owner must confirm provider settings, retention/deletion operation, international-transfer and business details against the deployed service. Do not answer unspecified retention periods with invented guarantees.

## Observed evidence and remaining gates

| Check | Observed result |
| --- | --- |
| OpenAI local package validator | Passed, version 0.2.0 |
| Clean-commit ZIP build | Passed; SHA-256 `37af6a8e43be390b0b71384a03552c7074f684444040cafe3365f5a513092c8b` |
| Production initialize | HTTP 200, protocol `2025-06-18`, server `1.1.0` |
| Production tools/list | HTTP 200, all four tools and review annotations |
| First positive data case | HTTP 429, JSON-RPC `-32029`, `registration_required` |
| Remaining positive cases | Skipped after shared quota failure; not passed |
| Cursor MCP client | Installed Cursor 3.20.14 successfully listed all four tools |
| Cursor agent account | CLI reported `Not logged in`; MCP discovery itself worked |
| Mistral connector | Prepared; no Mistral credentials in authorized SEO credential file |

## ChatGPT and Codex

Use `./scripts/build-openai-submission.sh` from a clean commit; upload the generated `dist/ball-ranks-openai-0.2.0.zip`. The ZIP includes the production MCP endpoint, onboarding skill and icons. Five positive and three negative review cases are already in `plugin.json`.

The portal needs a verified publishing identity and Apps Management Write access. Upload, inspect Metadata & Skills, finish skill scans, then connect the MCP and run its production tool scan. The portal accepts anonymous/OAuth connections but offers no API-key connection flow; do not insert a bearer key in public headers. See the [official submission workflow](https://developers.openai.com/plugins/deploy/submission).

Domain challenge: obtain the generated value and exact HTTPS origin from the portal, serve only that value at `/.well-known/openai-apps-challenge`, deploy and Verify Domain. No value was available during preparation, so no challenge was installed. Capture an accessible demo URL after successful data tests. Add it to review details or `review.demo_recording_url`, then have the owner complete attestations. The local validator is not OpenAI's scan or approval.

## Muse

Use the shared answers/tool table above for overview, technical documentation and permissions: every tool is Read, with no sensitive writes. Submit the endpoint as production, disclose anonymous limits, and supply a dedicated test account/key securely if requested. Explain the structured-data use case and demonstrate complete retrieval of the answer.

Owner gates: business verification, authority to represent the business, developer terms, data-processing declarations and securely supplied reviewer account. Confirm retention/provider details before signing. [Muse guidelines](https://muse.ai/platform/docs).

## Claude

The [connector submission guide](https://claude.com/docs/connectors/building/submission) permits no authentication for public data and OAuth for account services. Use anonymous Model Zero for this package; an API key is not a substitute for Claude account-linking OAuth. Add as a custom connector, test each tool in a conversation, then prepare the connector draft at `https://claude.ai/directory/manage`.

The public package supplies documentation, privacy/support URLs, an icon, titles and annotations. There is no MCP custom UI, so the MCP App carousel requirement does not apply. A paid Claude plan is required for submission; plan/login/terms and any requested reviewer-account details remain owner gates. Successful Claude conversations remain unverified.

## Perplexity

Prepare a Remote connector named Ball Ranks, URL `https://ballranks.com/api/mcp`, transport Streamable HTTP, auth None for public data or API Key for a dedicated Ball Ranks key. Organization use depends on admin permission. The [current remote-connector guide](https://www.perplexity.ai/help-center/en/articles/13915507-adding-custom-remote-connectors) supports these options; its custom-connector risk acknowledgement requires owner review.

Proposal text: “Ball Ranks provides structured fantasy football and basketball season rankings, weekly football rankings and player projections. Users can compare published rankings in conversation with explicit scoring/model context and source links. Four read-only MCP tools are available at a production HTTPS endpoint.” Attach the shared links and contact above. The [proposal form](https://www.perplexity.ai/help-center/en/articles/2026092501-submit-a-connector-proposal) is partnership intake, not guaranteed approval. Login, acknowledgements and final submission remain owner gates.

## Cursor

The root Agent Plugins package is accepted by the [official plugin format](https://prod.cursor.com/docs/reference/plugins). Publisher fields are in `plugin.json`; no second native plugin manifest is needed. The repository also supplies `.cursor/mcp.json` for direct project testing.

Executed locally: `cursor agent mcp enable ball-ranks`, then `cursor agent mcp list-tools ball-ranks`; all four tools appeared. Load the package with `cursor agent --plugin-dir /absolute/path/to/ball-ranks-plugin` after Cursor login, run the review conversations and record results. This second step tests the plugin/skill flow, which the MCP CLI check does not. Prepare the public repository link for `https://cursor.com/marketplace/publish`; owner login and final submission remain outstanding.

## Mistral

Private connector configuration: name `ball-ranks-private-review`, server `https://ballranks.com/api/mcp`, visibility `private`. No workspace/organization sharing. The [management API](https://docs.mistral.ai/studio/connectors/management) requires empty user credentials even for no-auth MCP connections; the script creates/reuses that private configuration and lists tools.

Run `python3 scripts/check-mistral-connector.py` in an environment with the `mistralai` SDK and an authorized `MISTRAL_API_KEY`; optionally supply `BALL_RANKS_API_KEY` through the process environment. The script invokes one read-only basketball tool without a language-model call. It does not delete the connector. Check the result/source link in Studio and then run all review prompts through Le Chat/Studio before claiming host validation. [Direct tool-call API](https://docs.mistral.ai/studio/connectors/tool_calling). Credential/account access is outstanding.

## Microsoft 365 Copilot

The first technical test should use a declarative agent with an MCP action. [Agents Toolkit](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/build-mcp-plugins) can generate its package from our endpoint with dynamic discovery. Choose None only for anonymous development testing. The [anonymous-auth guide](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-authentication-none) recommends authentication before production; [MCP plugin auth](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-authentication) supports OAuth/DCR/Entra, but not API keys. API keys are supported for REST API plugins.

Production MCP OAuth is a product prerequisite, not a manifest-only change: choose an authorization provider, implement consent/discovery/token validation and prove account quotas. No provider or OAuth implementation was approved in this preparation task. The existing `https://ballranks.com/openapi.json` offers a separate REST packaging path; choosing it would change the integration.

Owner gates: development tenant, Copilot access, custom app upload permission, publisher/business verification, program enrollment and terms. Agents can generate/validate packages once tenant/app configuration and the chosen authentication path exist. No Microsoft package was represented as tenant-tested or ready for production publishing.

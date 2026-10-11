# Ball Ranks marketplace runtime evidence

Checked 2026-10-11, 14:51–14:58 UTC. Grok and Kilo connect to the production endpoint without Ball Ranks credentials. Cline installs its submitted HTTP configuration. Successful rankings and projection retrieval remains blocked by the observed public IP's exhausted anonymous quota; model-generated host answers additionally require host/provider authentication.

## Exact submissions

| Host | Submitted PR | Tested revision |
| --- | --- | --- |
| Grok Build | [xAI #1288](https://github.com/xai-org/plugin-marketplace/pull/1288) | Catalog head `a289deee609f7e64dcd5c2aac59dd66be0f0fd89`; plugin pin `106f00d0aade4ae4512a351a10649bbf248d81d8`, version 0.1.0 |
| Kilo | [Kilo #343](https://github.com/Kilo-Org/kilo-marketplace/pull/343) | `b3edfbb408a87eaf7b05f1a4d157598a229ce48e`; anonymous and API-key configurations in `mcps/ball-ranks/MCP.yaml` |
| Cline | [Cline #183](https://github.com/cline/marketplace/pull/183) | `964be84b9183228069a045d78ffa1ce088f47227`; `registry/mcps/ball-ranks/entry.json` |

The OpenAI worktree and current repository main use different manifests from Grok's pinned version. Grok was checked against the exact 0.1.0 pin.

## Host checks

Host binaries were installed temporarily on macOS arm64. Grok used an isolated `GROK_HOME`; Kilo used isolated XDG config/data/cache directories; Cline used an explicit configuration directory. Existing app connections were not changed.

| Host and version | Observed result | Remaining gate |
| --- | --- | --- |
| Grok Build 1.0.50 (`c58f321264ba`) | Native plugin validation passed. Exact pinned plugin installed from its checkout and separately through the prepared local marketplace catalog. The available catalog showed the MCP server and onboarding skill; `plugin install ball-ranks --trust` succeeded. `mcp doctor ball-ranks --json` reported healthy, handshake protocol `2025-11-25`, and four discovered tools. | The model-generated tool answer needs Grok host login or an xAI API key, plus available Ball Ranks data quota. The interactive marketplace/video workflow remains to be recorded. |
| Kilo CLI 7.8.8 | `mcp add ball-ranks --url https://ballranks.com/api/mcp` succeeded. `mcp list` reported connected. | A default model request returned HTTP 401 `PAID_MODEL_AUTH_REQUIRED`: “You need to sign in to use this model.” Host sign-in or an authorized configured provider is needed. |
| Cline CLI 3.0.70 | Submitted install arguments accepted with `--yes --json`; status `installed`, transport `streamableHttp`, no warnings. | A model request returned “Unauthorized … re-authenticate your Cline account.” Cline/provider credentials are needed for the host answer. Installation alone does not establish endpoint connectivity. |

Grok's local project configuration initially hit its untrusted-folder guard. Installing the reviewed pinned plugin with `plugin install <local-checkout> --trust` into the isolated Grok configuration allowed the MCP check. Its `mcp doctor` output suggested `--trust`, but that subcommand rejects the flag in this version.

Grok emitted “No authorization support detected” during OAuth metadata discovery, then connected successfully. Ball Ranks' submitted anonymous package has no OAuth consent or MFA step. Host account authentication is separate from optional Ball Ranks API-key authentication. MFA is needed only if the selected account's login flow actually requests it.

Reproduce on an authorized test host:

```sh
# From the exact plugin checkout pinned in the Grok catalog:
grok plugin validate .
grok plugin install . --trust
grok mcp doctor ball-ranks --json

# Kilo CLI connection uses the same endpoint as the submitted anonymous config:
kilo mcp add ball-ranks --url https://ballranks.com/api/mcp
kilo mcp list

# Cline's submitted install arguments, with noninteractive output for testing:
cline mcp install ball-ranks --transport http https://ballranks.com/api/mcp --yes --json
```

Kilo CLI stores this endpoint as `{"type":"remote","url":"https://ballranks.com/api/mcp"}`. Its marketplace config uses `type: streamable-http`; these are different host serialization formats for the same remote transport. This CLI connection check does not prove installation from the pending marketplace entry in the VS Code extension.

## Endpoint checks

Direct anonymous `initialize` succeeded with protocol `2025-03-26`, server `ball-ranks-public-api`, version `1.1.0`. `tools/list` returned all four tools with input and output schemas and `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`, `openWorldHint: true`.

All five data requests in [demo-script.md](demo-script.md#production-endpoint-check) returned JSON-RPC `-32029`, data code `registration_required`. Football season and basketball season attempts at 14:51 UTC returned `retryAfterSeconds: 32894`. The remaining weekly rankings, player ranking, and player projection calls at 14:55 UTC returned the same error, with a shorter retry delay.

The retry delay points to 2026-10-12 00:00 UTC. The product's rate-limit migration computes fixed windows from UTC Unix time, so the anonymous day resets at UTC midnight. Waiting does not reserve quota: other requests from that public IP can consume the next day's allowance.

Minimum data unblock: available anonymous quota, or an authorized test-account Ball Ranks API key configured as a Bearer header in the host. A Free account provides 80 requests per day and 8 per minute; Model One requires Premium. Do not paste keys into chat or record credential screens. Do not substitute deployment, database, or scheduled-health secrets.

Unsupported baseball and `place_bet` calls also returned the quota error before tool validation. They are not proof of input rejection or host refusal. Re-run the three negative review prompts once the data gate is cleared.

## Marketplace checks and improvements

- Grok catalog validation and generated-index check passed on the submitted head and on a prepared merge of upstream `3852296d0c7caca966c5b5f32f1d66ea6247a9d5`. The prepared merge retains the original PR commits and adopts upstream's five remote pin updates. Against current upstream, only the Ball Ranks catalog entry and its generated component record remain: 31 added lines.
- Kilo's generator, 119 tests, TypeScript MCP check, and whitespace check passed. Its contribution guide says the listing `url` links to the MCP source repository. A narrow follow-up changes that URL to the canonical plugin repository, states that the anonymous quota is per public IP, and links the account page for API-key creation. Endpoint and authentication templates stay the same.
- Cline validation passed for 204 entries. The icon returned HTTP 200, `image/svg+xml`, and `Access-Control-Allow-Origin: *`. Its install arguments match the documented HTTP form. A narrow follow-up adds the schema-supported canonical source repository link and clarifies the per-IP quota and API-key setup location. `verified` and `featured` stay false. No required field or icon defect was found.

Kilo's optional companion skill can help select the four tools and preserve source links. It needs an externally hosted skill, an imported marketplace copy, a published `skills-latest` archive, and a client with bundle support. The current portable `skills/get-started` already provides the useful guidance, but a new marketplace companion reference must wait until its archive exists. Do not attach a download URL before publication or add a new unrelated submission merely to expand this PR.

## Exact host prompts

Use the same prompts across hosts and record the actual tool arguments, returned season/model, and `sourceUrl`:

1. “Using Ball Ranks Model Zero, show the top 10 fantasy football season rankings for PPR scoring and link the source board.”
2. “Using Ball Ranks Model Zero, show the top 10 wide receivers for football week 4 in half-PPR and link the source board.”
3. “Using Ball Ranks Model Zero, show the top five fantasy basketball season rankings and link the source board.”
4. “Where does Victor Wembanyama rank in Ball Ranks Model Zero for the basketball season? Link his source page.”
5. “What is Lamar Jackson's Ball Ranks Model Zero projection for football week 4 in PPR? Link his source page.”

Keep week 4 for the fixed review cases. A separate current-week demo should use the week confirmed by the returned source data. Never replace an error with a predicted result.

## Grok recording shot list

The [accepted Cal.com #953 demo request](https://github.com/xai-org/plugin-marketplace/pull/953) establishes that a short Grok Build installation and working request can matter to review. Its OAuth steps belong to Cal.com's server; Ball Ranks has no equivalent consent step.

1. Show Grok version, PR #1288 source/ref, plugin pin, and anonymous access mode. Omit account and credential screens.
2. In the existing xAI Official source, use `refs/pull/1288/merge`; refresh `/marketplace`, open Ball Ranks, and show the MCP server and onboarding skill.
3. Install, show the connected server/four tools, and run the football season prompt.
4. Show the actual football tool result, returned season/model, and clickable source board; repeat for the basketball season prompt.
5. Run one unsupported review prompt and capture the host's actual handling.
6. Restore the original marketplace source and record the tested versions/date in the final caption.

Only record after host authentication and the data quota gate are cleared. Target 60–120 seconds. Use real host output; endpoint logs alone do not demonstrate the host workflow. No recording or successful data result exists for this test run.

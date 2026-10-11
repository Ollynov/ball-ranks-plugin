# Google release and submission preparation

Verified 2026-10-11 against public main `03f9a892aed6aeac00bc996409516baa739af646`.

## Release candidate

The portable, Codex, Claude, and Gemini package manifests on public main specify `0.2.0`; the separately versioned MCP Registry server manifest specifies `1.1.0`. Public release `v0.1.0` remains Latest; no `v0.2.0` release has been published. Both package PRs [#1](https://github.com/Ollynov/ball-ranks-plugin/pull/1) and [#2](https://github.com/Ollynov/ball-ranks-plugin/pull/2) are merged.

Candidate archives built from the verified commit:

| Archive | SHA-256 |
| --- | --- |
| `dist/ball-ranks-gemini-0.2.0.zip` | `aa88722c0d1b7ed5073983ecfd32f07f897a588c31272e566776aca547d1e5ab` |
| `dist/ball-ranks-antigravity-0.2.0.zip` | `d187cd2eae57f2e88f6166046eac613826d527c59d431f42357e6fd09b15e520` |
| `dist/ball-ranks-openai-0.2.0.zip` | `a111fb32449787f841f7e82dd5e363c50277d75fb9d45ff5adb49e94c3497d3d` |

The Gemini archive contains its manifest at archive root, `GEMINI.md`, README, and license. The Antigravity archive contains the contents of `antigravity-plugin/` at archive root. The OpenAI archive has its own narrower contents and cannot substitute for a Gemini archive.

Build the Google candidates from the same source commit:

```sh
mkdir -p dist
git archive --format=zip --output=dist/ball-ranks-gemini-0.2.0.zip 03f9a892aed6aeac00bc996409516baa739af646 gemini-extension.json GEMINI.md LICENSE README.md
git archive --format=zip --output=dist/ball-ranks-antigravity-0.2.0.zip 03f9a892aed6aeac00bc996409516baa739af646:antigravity-plugin
```

Release notes draft: “Add the native Google Antigravity package, Gemini tool-selection context and installation guidance, and the validated OpenAI submission package. All clients connect to the existing read-only Ball Ranks MCP service.”

Publication awaits owner approval. Do not attach multiple unrelated generic ZIPs to a Gemini release without checking asset selection: [Gemini's release guide](https://geminicli.com/docs/extensions/releasing/) describes a single generic archive fallback. The GitHub source archive already exposes the root Gemini manifest; separate platform archives can be supplied through platform-specific distribution if required.

## Verified client checks

- Official Gemini CLI `0.63.0`, run via `npx @google/gemini-cli`.
- Installed the local candidate and the public GitHub repository pinned to the verified commit into separate isolated `GEMINI_CLI_HOME` directories. `extensions list` reports Ball Ranks `0.2.0` enabled, `GEMINI.md`, one MCP server, and its onboarding skill. `mcp list` reports the production HTTP server **Connected**. These management commands required no Google account sign-in.
- Official Antigravity CLI `1.3.3`, downloaded from the vendor URL in its official installer manifest and verified against the manifest's SHA-512 checksum.
- `agy plugin validate ./antigravity-plugin` passed: one skill and one MCP server processed.
- `agy plugin install ./antigravity-plugin` passed and installed under `~/.gemini/config/plugins/ball-ranks/`. `plugin list` records the imported Ball Ranks skill and MCP server. Plain `mcp list` returned none; it is not proof of plugin runtime connection.
- Existing OpenAI package validator and ZIP builder passed. No model-assisted Google data retrieval or recording has been completed.

Full assistant execution requires an eligible Gemini CLI authentication route or an Antigravity Google account/API key. [Antigravity authentication](https://antigravity.google/docs/cli/install) supports an existing keyring session, Google sign-in, or a Gemini API key. MFA depends on the owner's Google account security settings; the plugin does not require MFA. Installing or validating these packages does not itself require login.

## Gemini Gallery

The [official release guide](https://geminicli.com/docs/extensions/releasing/) requires a public GitHub repository, the `gemini-cli-extension` topic, and a root `gemini-extension.json`. All three are present. It documents a daily crawl; a separate release tag is not an indexing prerequisite.

The live [Gallery](https://geminicli.com/extensions/) displayed 2,178 extensions. Searches for `ball-ranks` and `Ollynov` returned no extension cards on 2026-10-11. Repository creation was 2026-10-07; the exact time its topic was added has not been independently established. Absence is verified, but crawl eligibility age and the cause are unverified.

Optional upstream website issue draft, not posted:

> Title: Extension absent from Gallery despite public repository and root manifest
>
> The public repository https://github.com/Ollynov/ball-ranks-plugin has the `gemini-cli-extension` topic and a root `gemini-extension.json`. On 2026-10-11, Gallery searches for `ball-ranks` and `Ollynov` returned no cards. Gemini CLI 0.63.0 installs the current 0.2.0 package successfully and connects to its remote MCP server. Could you check crawler discovery or validation for this repository? I cannot verify when the topic was originally added, so I cannot establish its exact eligible crawl age.

## Antigravity interest-form submission

The owner submitted the [official form](https://forms.gle/2EX5RFYPoJe1UgxR9) on 2026-10-11 after reviewing the prepared answers in the Codex browser. No logo, video, repository-upload, authentication, or legal-attestation field was present in this version of the form.

| Actual field | Submitted answer |
| --- | --- |
| Email | `help@ballranks.com` |
| Company Name | Ball Ranks |
| Company Primary Website (Domain) | `https://ballranks.com` |
| Primary Contact Name | Aljosha Novakovic |
| Primary Contact Email | `help@ballranks.com` |
| Public-facing support | `help@ballranks.com; https://ballranks.com/support` |
| Documentation URL | `https://github.com/Ollynov/ball-ranks-plugin#google-antigravity` |

Plugin Description:

> Ball Ranks provides fantasy football and basketball season rankings, weekly football rankings, and player projections through four read-only MCP tools. The Antigravity package includes a native plugin manifest, a remote MCP configuration for https://ballranks.com/api/mcp, and a focused skill that selects the relevant tool and cites the returned Ball Ranks source URL. Public Model Zero data is available with anonymous request limits. Repository: https://github.com/Ollynov/ball-ranks-plugin/tree/main/antigravity-plugin

Google review or follow-up is pending. The existing icon assets remain available if Google requests them later. Successful end-to-end tool evidence remains useful review material, even though this interest form did not ask for a demo.

# Google release and submission preparation

Verified 2026-10-11 against public main `f202c449c938764d5adf16451667e4b9079468ea`.

## Release candidate

The portable, Codex, Claude, and Gemini package manifests on public main specify `0.2.0`; the separately versioned MCP Registry server manifest specifies `1.1.0`. Public release `v0.1.0` remains Latest; no `v0.2.0` release has been published. Both package PRs [#1](https://github.com/Ollynov/ball-ranks-plugin/pull/1) and [#2](https://github.com/Ollynov/ball-ranks-plugin/pull/2) are merged.

Candidate archives built from the verified commit:

| Archive | SHA-256 |
| --- | --- |
| `dist/ball-ranks-gemini-0.2.0.zip` | `f8370c76cafc4708516067f8cc21d663e88e99fb9fd35106f96c5262902adddc` |
| `dist/ball-ranks-antigravity-0.2.0.zip` | `47acb731e97cb7d2b5ec3863eae3ea0facf3ac53203679b25e491477d5209599` |
| `dist/ball-ranks-openai-0.2.0.zip` | `37af6a8e43be390b0b71384a03552c7074f684444040cafe3365f5a513092c8b` |

The Gemini archive contains its manifest at archive root, `GEMINI.md`, README, and license. The Antigravity archive contains the contents of `antigravity-plugin/` at archive root. The OpenAI archive has its own narrower contents and cannot substitute for a Gemini archive.

Build the Google candidates from the same source commit:

```sh
mkdir -p dist
git archive --format=zip --output=dist/ball-ranks-gemini-0.2.0.zip f202c449c938764d5adf16451667e4b9079468ea gemini-extension.json GEMINI.md LICENSE README.md
git archive --format=zip --output=dist/ball-ranks-antigravity-0.2.0.zip f202c449c938764d5adf16451667e4b9079468ea:antigravity-plugin
```

Release notes draft: “Add the native Google Antigravity package, Gemini tool-selection context and installation guidance, and the validated OpenAI submission package. All clients connect to the existing read-only Ball Ranks MCP service.”

Publication awaits owner approval. Do not attach multiple unrelated generic ZIPs to a Gemini release without checking asset selection: [Gemini's release guide](https://geminicli.com/docs/extensions/releasing/) describes a single generic archive fallback. The GitHub source archive already exposes the root Gemini manifest; separate platform archives can be supplied through platform-specific distribution if required.

## Verified client checks

- Official Gemini CLI `0.63.0`, run via `npx @google/gemini-cli`.
- Installed the candidate into an isolated `GEMINI_CLI_HOME`. `extensions list` reports Ball Ranks `0.2.0` enabled, `GEMINI.md`, one MCP server, and its onboarding skill. `mcp list` reports the production HTTP server **Connected**. These management commands required no Google account sign-in.
- Official Antigravity CLI `1.3.3`, downloaded from the vendor URL in its official installer manifest and verified against the manifest's SHA-512 checksum.
- `agy plugin validate ./antigravity-plugin` passed: one skill and one MCP server processed.
- `agy plugin install ./antigravity-plugin` passed. `plugin list` records the imported Ball Ranks skill and MCP server. Plain `mcp list` lists only separately configured servers and returned none; it is not proof of plugin runtime connection.
- Existing OpenAI package validator and ZIP builder passed. No model-assisted Google data retrieval or recording has been completed.

Full assistant execution requires an eligible Gemini CLI authentication route or an Antigravity Google account/API key. [Antigravity authentication](https://antigravity.google/docs/cli/install) supports an existing keyring session, Google sign-in, or a Gemini API key. MFA depends on the owner's Google account security settings; the plugin does not require MFA. Installing or validating these packages does not itself require login.

## Gemini Gallery

The [official release guide](https://geminicli.com/docs/extensions/releasing/) requires a public GitHub repository, the `gemini-cli-extension` topic, and a root `gemini-extension.json`. All three are present. It documents a daily crawl; a separate release tag is not an indexing prerequisite.

The live [Gallery](https://geminicli.com/extensions/) displayed 2,178 extensions. Searches for `ball-ranks` and `Ollynov` returned no extension cards on 2026-10-11. Repository creation was 2026-10-07; the exact time its topic was added has not been independently established. Absence is verified, but crawl eligibility age and the cause are unverified.

Optional upstream website issue draft, not posted:

> Title: Extension absent from Gallery despite public repository and root manifest
>
> The public repository https://github.com/Ollynov/ball-ranks-plugin has the `gemini-cli-extension` topic and a root `gemini-extension.json`. On 2026-10-11, Gallery searches for `ball-ranks` and `Ollynov` returned no cards. Gemini CLI 0.63.0 installs the current 0.2.0 package successfully and connects to its remote MCP server. Could you check crawler discovery or validation for this repository? I cannot verify when the topic was originally added, so I cannot establish its exact eligible crawl age.

## Antigravity interest-form draft

Inspected the [official form](https://forms.gle/2EX5RFYPoJe1UgxR9) in the Codex browser. The Google account was already signed in. A draft was prepared through the final Submit page; it was not submitted. No logo, video, repository-upload, authentication, or legal-attestation field was present in this version of the form.

| Actual field | Draft answer |
| --- | --- |
| Email | `help@ballranks.com` |
| Company Name | Ball Ranks |
| Company Primary Website (Domain) | `https://ballranks.com` |
| Primary Contact Name | Aljosha Novakovic |
| Primary Contact Email | `help@ballranks.com` |
| Public-facing support | `help@ballranks.com; https://ballranks.com/support` |
| Documentation URL | `https://github.com/Ollynov/ball-ranks-plugin#google-antigravity` |

Plugin Description draft:

> Ball Ranks provides fantasy football and basketball season rankings, weekly football rankings, and player projections through four read-only MCP tools. The Antigravity package includes a native plugin manifest, a remote MCP configuration for https://ballranks.com/api/mcp, and a focused skill that selects the relevant tool and cites the returned Ball Ranks source URL. Public Model Zero data is available with anonymous request limits. Repository: https://github.com/Ollynov/ball-ranks-plugin/tree/main/antigravity-plugin

The owner should confirm the company/contact details and approve submitting this specific draft. The existing icon assets remain available if Google requests them later. Successful end-to-end tool evidence remains useful review material, even though this interest form does not ask for a demo.

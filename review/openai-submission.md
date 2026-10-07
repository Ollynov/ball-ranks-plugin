# OpenAI submission checklist

The repository package supplies the public listing metadata, five positive test cases, three negative test cases, commerce declaration, and release notes. It intentionally omits `review.demo_recording_url` until an accessible production walkthrough has been recorded.

## Before upload

- Confirm `https://ballranks.com/api/mcp` initializes and lists tools without consuming the product-data quota.
- Run all cases in `review/review-cases.json` against production and record the observed tool calls and results.
- Confirm every advertised tool has explicit `readOnlyHint`, `destructiveHint`, and `openWorldHint` values.
- Run `./scripts/build-openai-submission.sh` from a clean commit.

## Tool annotation justifications

Use these justifications for each of `get_week_rankings`, `get_season_rankings`, `get_player_rankings`, and `get_player_projections` if the submission portal requests them:

- `readOnlyHint: true`: the tool only retrieves published rankings or projections and cannot create, update, delete, send, queue, or persist user data.
- `destructiveHint: false`: the tool has no write or deletion mode and cannot cause an irreversible outcome.
- `openWorldHint: true`: the tool retrieves public sports and player entities from the hosted Ball Ranks service rather than a bounded private account or workspace.

## Dashboard-only requirements

- Use the **With MCP** submission path and connect `https://ballranks.com/api/mcp`.
- Complete individual or business identity verification for the publisher name.
- Confirm the OpenAI organization role has `api.apps.write` and `api.apps.read`.
- Complete the generated domain challenge at `/.well-known/openai-apps-challenge`.
- Record the production walkthrough in `review/demo-script.md`, host it at a reviewer-accessible URL, and add that URL in the dashboard or as `review.demo_recording_url` in a later manifest release.
- Scan the production tools, resolve all blocking findings, and submit the completed draft attestations.

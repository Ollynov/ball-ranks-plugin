#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

if [[ -n "$(git status --porcelain --untracked-files=all)" ]]; then
  echo "error: commit or remove working-tree changes before building" >&2
  exit 1
fi

./scripts/validate-openai-submission.py

version="$(python3 -c 'import json; print(json.load(open("plugin.json", encoding="utf-8"))["version"])')"
output="dist/ball-ranks-openai-${version}.zip"
mkdir -p dist

TZ=UTC git archive \
  --format=zip \
  --output="$output" \
  HEAD \
  plugin.json \
  mcp.json \
  skills/get-started/SKILL.md \
  assets/icon.png \
  assets/icon-dark.png

digest="$(shasum -a 256 "$output" | awk '{print $1}')"
echo "$output"
echo "sha256 $digest"

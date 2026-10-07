#!/usr/bin/env python3
"""Validate the Ball Ranks portable package against OpenAI submission limits."""

from __future__ import annotations

import json
import struct
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError(f"{path.relative_to(ROOT)} is not a PNG")
    return struct.unpack(">II", header[16:24])


def main() -> int:
    errors: list[str] = []
    plugin = load_json("plugin.json")
    codex = load_json(".codex-plugin/plugin.json")
    claude = load_json(".claude-plugin/plugin.json")
    mcp = load_json("mcp.json")
    cases = load_json("review/review-cases.json")

    openai = plugin.get("extensions", {}).get("com.openai", {})
    interface = openai.get("interface", {})
    review = openai.get("review", {})
    embedded_cases = review.get("test_cases", {})

    require(plugin.get("name") == "ball-ranks", "plugin name must remain ball-ranks", errors)
    require(
        plugin.get("version") == codex.get("version") == claude.get("version"),
        "portable, Codex, and Claude manifest versions must match",
        errors,
    )
    require(len(interface.get("displayName", "")) <= 30, "displayName exceeds 30 characters", errors)
    require(
        0 < len(interface.get("shortDescription", "")) <= 30,
        "shortDescription must contain 1-30 characters",
        errors,
    )
    require(len(interface.get("longDescription", "")) <= 4000, "longDescription exceeds 4000 characters", errors)
    require("screenshots" not in interface, "screenshots are not allowed without an MCP UI template", errors)
    require("apps" not in plugin, "public submission ZIP must not declare apps", errors)
    require("hooks" not in plugin, "public submission ZIP must not declare lifecycle hooks", errors)

    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        value = interface.get(key, "")
        parsed = urlparse(value)
        require(parsed.scheme == "https" and bool(parsed.netloc), f"{key} must be an HTTPS URL", errors)

    prompts = interface.get("defaultPrompt", [])
    require(isinstance(prompts, list) and 1 <= len(prompts) <= 3, "defaultPrompt must contain 1-3 prompts", errors)
    require(all(isinstance(value, str) and len(value) <= 128 for value in prompts), "default prompts must be strings of at most 128 characters", errors)
    require(len(set(prompts)) == len(prompts), "default prompts must be unique", errors)
    require(all("@" not in value for value in prompts), "default prompts must not contain app mentions", errors)

    for key in ("composerIcon", "composerIconDark", "logo", "logoDark"):
        value = interface.get(key, "")
        require(value.startswith("./assets/"), f"{key} must use a ./assets/ path", errors)
        asset = ROOT / value.removeprefix("./")
        require(asset.is_file(), f"{key} references a missing file: {value}", errors)
        if asset.is_file():
            try:
                width, height = png_dimensions(asset)
                require(width == height and width >= 48, f"{key} must reference a square image at least 48px", errors)
                require(width <= 4096, f"{key} image exceeds 4096px", errors)
                require(asset.stat().st_size <= 5 * 1024 * 1024, f"{key} image exceeds 5 MiB", errors)
            except ValueError as exc:
                errors.append(str(exc))

    require(embedded_cases == cases, "review/review-cases.json must match embedded review.test_cases", errors)
    positive = embedded_cases.get("positive", [])
    negative = embedded_cases.get("negative", [])
    require(len(positive) == 5, "initial MCP review requires exactly five positive cases", errors)
    require(len(negative) == 3, "initial MCP review requires exactly three negative cases", errors)
    for index, case in enumerate(positive, start=1):
        for key in ("description", "prompt", "tools_triggered", "expected_behavior"):
            require(isinstance(case.get(key), str) and bool(case[key].strip()), f"positive case {index} requires {key}", errors)
    for index, case in enumerate(negative, start=1):
        for key in ("description", "prompt"):
            require(isinstance(case.get(key), str) and bool(case[key].strip()), f"negative case {index} requires {key}", errors)

    require(review.get("commerce") is False, "review.commerce must explicitly be false", errors)
    require("demo_recording_url" not in review, "do not declare a demo URL until a real recording exists", errors)
    release_notes = openai.get("publication", {}).get("release_notes", "")
    require(isinstance(release_notes, str) and bool(release_notes.strip()), "publication.release_notes is required", errors)

    servers = mcp.get("mcpServers", {})
    require(len(servers) == 1 and "ball-ranks" in servers, "portable package must declare exactly one ball-ranks MCP server", errors)
    server = servers.get("ball-ranks", {})
    require(server.get("type") == "streamable-http", "MCP server must use streamable-http", errors)
    require(server.get("url") == "https://ballranks.com/api/mcp", "MCP server URL is incorrect", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OpenAI submission package is valid for version {plugin['version']}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

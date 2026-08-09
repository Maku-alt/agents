#!/usr/bin/env python3
"""Validate agent packages and generate the human and machine catalogs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / "agents"
CATALOG_DIR = ROOT / "catalog"
POLICY_PATH = ROOT / "config" / "curation-policy.json"
INDEX_PATH = CATALOG_DIR / "agents-index.json"
DICTIONARY_PATH = CATALOG_DIR / "agents-dictionary.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_packages() -> list[dict]:
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    required = policy["required_package_files"]
    name_pattern = re.compile(policy["name_pattern"])
    allowed_statuses = set(policy["allowed_statuses"])
    packages: list[dict] = []
    errors: list[str] = []

    for package_dir in sorted(path for path in AGENTS_DIR.iterdir() if path.is_dir()):
        missing = [name for name in required if not (package_dir / name).is_file()]
        if missing:
            errors.append(f"{package_dir.name}: missing {', '.join(missing)}")
            continue

        agent_path = package_dir / "agent.toml"
        metadata_path = package_dir / "metadata.json"
        try:
            agent = tomllib.loads(agent_path.read_text(encoding="utf-8"))
        except (tomllib.TOMLDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"{package_dir.name}/agent.toml: {exc}")
            continue
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"{package_dir.name}/metadata.json: {exc}")
            continue

        for field in ("name", "description", "developer_instructions"):
            if not isinstance(agent.get(field), str) or not agent[field].strip():
                errors.append(f"{package_dir.name}/agent.toml: invalid required field {field}")

        slug = metadata.get("slug")
        if slug != package_dir.name or agent.get("name") != slug:
            errors.append(
                f"{package_dir.name}: directory, metadata.slug and agent.name must match"
            )
        if not isinstance(slug, str) or not name_pattern.fullmatch(slug):
            errors.append(f"{package_dir.name}: invalid slug {slug!r}")
        if metadata.get("status") not in allowed_statuses:
            errors.append(f"{package_dir.name}: invalid status {metadata.get('status')!r}")

        packages.append(
            {
                "slug": slug,
                "name": agent.get("name"),
                "description": agent.get("description"),
                "status": metadata.get("status"),
                "last_reviewed": metadata.get("last_reviewed"),
                "source": metadata.get("source"),
                "tags": metadata.get("tags", []),
                "required_skills": metadata.get("required_skills", []),
                "role": metadata.get("role"),
                "sandbox_mode": agent.get("sandbox_mode", "inherits"),
                "write_policy": metadata.get("write_policy"),
                "agent_sha256": sha256(agent_path),
                "package_path": str(package_dir.relative_to(ROOT)).replace("\\", "/"),
            }
        )

    if errors:
        raise ValueError("\n".join(errors))
    return packages


def render_index(packages: list[dict]) -> str:
    payload = {"schema_version": 1, "agents": packages}
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def render_dictionary(packages: list[dict]) -> str:
    lines = [
        "# Agents Dictionary",
        "",
        "Catalogo generado desde `agents/*/agent.toml` y `metadata.json`. No editar a mano.",
        "",
        "| Agent | Status | Last reviewed | Role | Sandbox | Required skills | Tags | Description |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in packages:
        skills = ", ".join(f"`{value}`" for value in item["required_skills"]) or "—"
        tags = ", ".join(f"`{value}`" for value in item["tags"]) or "—"
        lines.append(
            f"| `{item['slug']}` | `{item['status']}` | `{item['last_reviewed']}` | "
            f"`{item['role']}` | `{item['sandbox_mode']}` | {skills} | {tags} | {item['description']} |"
        )
    lines.extend(
        [
            "",
            "## Convenciones",
            "",
            "- El hilo principal orquesta; las entradas del catalogo son workers.",
            "- `impeccable` aplica a experiencias frontend/HTML, no a PowerPoint.",
            "- Los agentes read-only revisan o asesoran; no corrigen artefactos.",
            "- El hash permite detectar drift entre el repo y una copia instalada.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate and verify generated files")
    args = parser.parse_args()

    try:
        packages = load_packages()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(exc, file=sys.stderr)
        return 1

    expected = {
        INDEX_PATH: render_index(packages),
        DICTIONARY_PATH: render_dictionary(packages),
    }

    if args.check:
        stale = []
        for path, content in expected.items():
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                stale.append(str(path.relative_to(ROOT)))
        if stale:
            print("Stale generated files: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"Validated {len(packages)} active agent packages.")
        return 0

    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    for path, content in expected.items():
        path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Generated catalogs for {len(packages)} agent packages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

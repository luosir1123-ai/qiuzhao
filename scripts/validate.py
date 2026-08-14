#!/usr/bin/env python3
"""Validate qiuzhao structure and local Markdown references."""

from pathlib import Path
import argparse
import re
from typing import List


LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def _frontmatter(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    data = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def validate_repository(root: Path) -> List[str]:
    root = root.resolve()
    errors: List[str] = []
    skills_dir = root / "skills"
    if skills_dir.exists():
        for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.exists():
                errors.append(f"{skill_dir.relative_to(root)}: missing SKILL.md")
                continue
            text = skill_file.read_text(encoding="utf-8")
            metadata = _frontmatter(text)
            if metadata is None:
                errors.append(f"{skill_file.relative_to(root)}: missing or invalid frontmatter")
            else:
                if metadata.get("name") != skill_dir.name:
                    errors.append(f"{skill_file.relative_to(root)}: name must equal {skill_dir.name}")
                if not metadata.get("description"):
                    errors.append(f"{skill_file.relative_to(root)}: missing description")
            agent_file = skill_dir / "agents" / "openai.yaml"
            if not agent_file.exists():
                errors.append(f"{skill_dir.relative_to(root)}: missing agents/openai.yaml")
            else:
                agent_text = agent_file.read_text(encoding="utf-8")
                for key in ("display_name:", "short_description:", "default_prompt:"):
                    if key not in agent_text:
                        errors.append(f"{agent_file.relative_to(root)}: missing {key[:-1]}")

    for source in root.rglob("*.md"):
        if ".git" in source.parts:
            continue
        text = source.read_text(encoding="utf-8")
        for raw_target in LINK.findall(text):
            target = raw_target.split("#", 1)[0].strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (source.parent / target).resolve().exists():
                errors.append(f"{source.relative_to(root)}: broken reference {raw_target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()
    errors = validate_repository(args.root)
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

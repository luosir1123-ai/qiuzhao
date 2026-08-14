#!/usr/bin/env python3
"""Validate the Markdown-only Obsidian vault without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    ".obsidian/app.json",
    "00-Dashboard/学习总览.md",
    "08-Weekly/六周总路线.md",
    "08-Weekly/每日执行协议.md",
    "08-Weekly/每日任务卡.md",
    "07-Daily/2026-08-14-Day01.md",
    "Templates/每日学习模板.md",
]
WEEK_FILES = sorted((ROOT / "08-Weekly").glob("第*周-*.md"))
PLACEHOLDERS = re.compile(r"\b(?:TBD|TODO|PLACEHOLDER)\b", re.IGNORECASE)
SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
    re.compile(r"\bBearer\s+[A-Za-z0-9._~+/-]{16,}", re.IGNORECASE),
    re.compile(r"\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?)://[^\s/:]+:[^\s/@]+@", re.IGNORECASE),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?:api[_-]?key|access[_-]?token|password|cookie)\s*[:=]\s*['\"]?[^\s'\"]{8,}", re.IGNORECASE),
]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)#]+)(?:#[^)]+)?\)")
FRONTMATTER_FIELD = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(\S.*?)\s*$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_required(errors: list[str]) -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).exists():
            fail(errors, f"missing required path: {relative}")


def validate_markdown(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if text.startswith("---\n") and "\n---\n" not in text[4:]:
            fail(errors, f"unclosed YAML frontmatter: {relative}")
        if text.startswith("---\n"):
            raw = text[4:text.find("\n---\n", 4)]
            keys: set[str] = set()
            for line_number, line in enumerate(raw.splitlines(), 2):
                match = FRONTMATTER_FIELD.fullmatch(line)
                if not match:
                    fail(errors, f"frontmatter must use flat non-empty key/value YAML: {relative}:{line_number}")
                    continue
                key = match.group(1)
                if key in keys:
                    fail(errors, f"duplicate frontmatter key {key}: {relative}:{line_number}")
                keys.add(key)
        if PLACEHOLDERS.search(text):
            fail(errors, f"forbidden placeholder word: {relative}")
        if "[[" in text or "]]" in text:
            fail(errors, f"Wikilink is not GitHub-clickable: {relative}")
        for target in MARKDOWN_LINK.findall(text):
            decoded = target.replace("%20", " ")
            resolved = (path.parent / decoded).resolve()
            if not resolved.exists():
                fail(errors, f"broken Markdown link in {relative}: {target}")


def validate_text_files(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT)
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.endswith((" ", "\t")):
                fail(errors, f"trailing whitespace: {relative}:{line_number}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(errors, f"sensitive value found in {relative}")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = FRONTMATTER_FIELD.fullmatch(line)
        if match:
            fields[match.group(1)] = match.group(2)
    return fields


def validate_record_contracts(errors: list[str]) -> None:
    required_minutes = {
        "python_minutes": 60,
        "algorithm_minutes": 90,
        "fundamentals_minutes": 75,
        "agent_rag_minutes": 75,
        "project_interview_minutes": 30,
        "applications_review_minutes": 30,
    }
    daily_files = [ROOT / "Templates/每日学习模板.md", *sorted((ROOT / "07-Daily").glob("*.md"))]
    for path in daily_files:
        fields = frontmatter(path)
        relative = path.relative_to(ROOT)
        values = []
        for name, expected in required_minutes.items():
            try:
                values.append(int(fields[name]))
            except (KeyError, ValueError):
                fail(errors, f"invalid or missing {name}: {relative}")
        if values and sum(values) != 360:
            fail(errors, f"daily YAML minutes total {sum(values)}, expected 360: {relative}")
        if fields.get("study_hours") != "6":
            fail(errors, f"study_hours must be 6: {relative}")

    algorithm = frontmatter(ROOT / "Templates/LeetCode题目模板.md")
    for name in ("first_attempt_result", "review_dates", "next_review_date", "status"):
        if name not in algorithm:
            fail(errors, f"algorithm template missing field: {name}")


def validate_schedule(errors: list[str]) -> None:
    if len(WEEK_FILES) != 6:
        fail(errors, f"expected 6 weekly schedule files, found {len(WEEK_FILES)}")
        return
    day_rows = 0
    for path in WEEK_FILES:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if re.match(r"^\| Day \d+ \|", line):
                day_rows += 1
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                defaults = [60, 90, 75, 75, 30, 30]
                actual = []
                for cell, default in zip(cells[1:7], defaults):
                    override = re.search(r"（(\d+)）$", cell)
                    actual.append(int(override.group(1)) if override else default)
                declared = int(cells[-1]) if cells[-1].isdigit() else -1
                if sum(actual) != declared or declared != 360:
                    fail(errors, f"schedule minutes {actual} total {sum(actual)}, declared {declared}: {path.name}:{line_number}")
    if day_rows != 42:
        fail(errors, f"expected 42 daily schedule rows, found {day_rows}")
    cards = (ROOT / "08-Weekly/每日任务卡.md").read_text(encoding="utf-8")
    card_days = [int(value) for value in re.findall(r"^\| Day (\d+) \|", cards, re.MULTILINE)]
    if card_days != list(range(1, 43)):
        fail(errors, f"daily task cards must cover Day 1-42 exactly, found {card_days}")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    validate_markdown(errors)
    validate_text_files(errors)
    validate_record_contracts(errors)
    validate_schedule(errors)
    if errors:
        print("Vault validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Vault validation passed: {len(list(ROOT.rglob('*.md')))} Markdown files, 42 schedule days.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

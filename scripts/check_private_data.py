#!/usr/bin/env python3
"""Detect common private-data patterns before publishing the repository."""

from dataclasses import dataclass
from pathlib import Path
import argparse
import re
from typing import Iterable, List


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    rule: str


RULES = {
    "phone-number": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    "mainland-id": re.compile(r"(?<!\d)\d{17}[\dXx](?!\d)"),
    "local-home-path": re.compile(r"/Users/[^/\s]+/"),
    "private-email": re.compile(
        r"\b[A-Z0-9._%+-]+@(?!example\.(?:com|org|net)\b)"
        r"(?:qq|163|126|gmail|outlook|foxmail)\.com\b",
        re.IGNORECASE,
    ),
    "credential": re.compile(
        r"(?i)(?:api[_-]?key|secret|access[_-]?token|password)\s*[:=]\s*['\"]?[^\s'\"]{8,}"
    ),
}

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg"
}


def _files(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if path.is_file():
            yield path
            continue
        if path.is_dir():
            for child in path.rglob("*"):
                if child.is_file() and ".git" not in child.parts:
                    yield child


def scan_paths(root: Path, paths: Iterable[Path] = None) -> List[Finding]:
    findings: List[Finding] = []
    paths = list(paths) if paths is not None else [root]
    for path in _files(paths):
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(lines, start=1):
            for rule, pattern in RULES.items():
                if pattern.search(line):
                    findings.append(Finding(path, line_number, rule))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, default=[Path.cwd()])
    args = parser.parse_args()
    findings = scan_paths(Path.cwd(), args.paths)
    for finding in findings:
        print(f"{finding.path}:{finding.line}: {finding.rule}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())

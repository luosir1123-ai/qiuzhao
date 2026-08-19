#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

for skill in job-fit-ranker jd-resume-tailor resume-auditor application-form-helper interview-prep oss-contributor; do
  test -f "$repo_root/skills/$skill/SKILL.md"
  test -f "$repo_root/skills/$skill/agents/openai.yaml"
  grep -q "name: $skill" "$repo_root/skills/$skill/SKILL.md"
done

echo "Discovered all six Skills."

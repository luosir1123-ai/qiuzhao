import tempfile
import unittest
from pathlib import Path

from scripts.check_private_data import scan_paths
from scripts.validate import validate_repository


VALID_SKILL = """---
name: sample-skill
description: Use when a user asks to rank jobs from a careers website.
---

# Sample

Read [rules](../../shared/references/rules.md).
"""

VALID_AGENT = """interface:
  display_name: Sample Skill
  short_description: Rank careers website jobs
  default_prompt: Rank jobs from this careers URL against my resume.
"""


class RepositoryValidationTests(unittest.TestCase):
    def make_repo(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        skill = root / "skills" / "sample-skill"
        (skill / "agents").mkdir(parents=True)
        (root / "shared" / "references").mkdir(parents=True)
        (skill / "SKILL.md").write_text(VALID_SKILL, encoding="utf-8")
        (skill / "agents" / "openai.yaml").write_text(VALID_AGENT, encoding="utf-8")
        (root / "shared" / "references" / "rules.md").write_text("# Rules\n", encoding="utf-8")
        return temp, root

    def test_valid_repository_passes(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        self.assertEqual([], validate_repository(root))

    def test_missing_frontmatter_fails(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        (root / "skills" / "sample-skill" / "SKILL.md").write_text("# Missing\n", encoding="utf-8")
        errors = validate_repository(root)
        self.assertTrue(any("frontmatter" in error for error in errors))

    def test_broken_markdown_reference_fails(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        path = root / "shared" / "references" / "rules.md"
        path.unlink()
        errors = validate_repository(root)
        self.assertTrue(any("broken reference" in error for error in errors))

    def test_private_data_scanner_flags_sensitive_examples(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        leak = root / "leak.md"
        phone = "138" + "1234" + "5678"
        home = "/" + "Users" + "/alice/resume.pdf"
        leak.write_text(f"phone {phone} and {home}", encoding="utf-8")
        findings = scan_paths(root, [leak])
        self.assertEqual({"local-home-path", "phone-number"}, {finding.rule for finding in findings})

    def test_private_data_scanner_allows_synthetic_placeholders(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        example = root / "example.md"
        example.write_text("name: Example Candidate\nemail: candidate@example.com\n", encoding="utf-8")
        self.assertEqual([], scan_paths(root, [example]))

    def test_private_data_scanner_checks_svg_text(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        banner = root / "banner.svg"
        home = "/" + "Users" + "/alice/resume.pdf"
        banner.write_text(f"<svg><text>{home}</text></svg>", encoding="utf-8")
        findings = scan_paths(root, [banner])
        self.assertEqual({"local-home-path"}, {finding.rule for finding in findings})

    def test_repository_contains_unified_skill_set(self):
        root = Path(__file__).resolve().parents[1]
        expected = {
            "job-fit-ranker",
            "jd-resume-tailor",
            "resume-auditor",
            "application-form-helper",
            "interview-prep",
            "oss-contributor",
        }
        actual = {path.name for path in (root / "skills").iterdir() if path.is_dir()}
        self.assertTrue(expected <= actual)

    def test_pipeline_skills_link_required_contracts(self):
        root = Path(__file__).resolve().parents[1]
        required_links = {
            "job-fit-ranker": "job-record-schema.md",
            "jd-resume-tailor": "claim-ledger-schema.md",
            "application-form-helper": "application-record-schema.md",
            "interview-prep": "claim-ledger-schema.md",
            "resume-auditor": "claim-ledger-schema.md",
            "oss-contributor": "claim-ledger-schema.md",
        }
        for skill, contract in required_links.items():
            text = (root / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(contract, text, skill)


if __name__ == "__main__":
    unittest.main()

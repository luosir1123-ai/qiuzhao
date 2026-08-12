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


if __name__ == "__main__":
    unittest.main()

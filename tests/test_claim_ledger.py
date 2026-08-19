import unittest

from scripts.validate_claim_ledger import validate_claim_ledger


def valid_ledger():
    return {
        "sources": [
            {
                "id": "S-001",
                "type": "user_document",
                "title": "Fictional project record",
                "url": "https://example.com/evidence",
            }
        ],
        "claims": [
            {
                "id": "C-001",
                "text": "Reduced processing time from 20 minutes to 10 minutes.",
                "status": "source_grounded",
                "source_ids": ["S-001"],
                "metric": {
                    "numerator": 10,
                    "denominator": 20,
                    "displayed_percent": 50,
                },
            }
        ],
    }


class ClaimLedgerTests(unittest.TestCase):
    def test_valid_ledger_passes(self):
        self.assertEqual([], validate_claim_ledger(valid_ledger()))

    def test_missing_source_reference_fails(self):
        ledger = valid_ledger()
        ledger["claims"][0]["source_ids"] = ["S-404"]
        self.assertTrue(any("unknown source" in error for error in validate_claim_ledger(ledger)))

    def test_invalid_status_fails(self):
        ledger = valid_ledger()
        ledger["claims"][0]["status"] = "verified_by_ai"
        self.assertTrue(any("invalid status" in error for error in validate_claim_ledger(ledger)))

    def test_inconsistent_ratio_fails(self):
        ledger = valid_ledger()
        ledger["claims"][0]["metric"]["displayed_percent"] = 80
        self.assertTrue(any("inconsistent ratio" in error for error in validate_claim_ledger(ledger)))

    def test_unsafe_source_url_fails(self):
        ledger = valid_ledger()
        ledger["sources"][0]["url"] = "javascript:alert(1)"
        self.assertTrue(any("unsafe URL" in error for error in validate_claim_ledger(ledger)))

    def test_source_grounded_requires_independent_source(self):
        ledger = valid_ledger()
        ledger["claims"][0]["source_ids"] = []
        self.assertTrue(any("independent source" in error for error in validate_claim_ledger(ledger)))

        ledger = valid_ledger()
        ledger["sources"][0]["type"] = "user_statement"
        self.assertTrue(any("independent source" in error for error in validate_claim_ledger(ledger)))

    def test_malformed_items_return_errors_instead_of_crashing(self):
        self.assertTrue(validate_claim_ledger({"sources": [1], "claims": []}))
        ledger = valid_ledger()
        ledger["claims"][0]["source_ids"] = "S-001"
        self.assertTrue(any("source_ids must be a list" in error for error in validate_claim_ledger(ledger)))

    def test_incomplete_ratio_fails(self):
        ledger = valid_ledger()
        ledger["claims"][0]["metric"] = {"numerator": 10, "displayed_percent": 50}
        self.assertTrue(any("incomplete ratio" in error for error in validate_claim_ledger(ledger)))

    def test_baseline_result_change_is_checked(self):
        ledger = valid_ledger()
        ledger["claims"][0]["metric"] = {
            "baseline": 100,
            "result": 80,
            "change_percent": -50,
        }
        self.assertTrue(any("inconsistent change" in error for error in validate_claim_ledger(ledger)))


if __name__ == "__main__":
    unittest.main()

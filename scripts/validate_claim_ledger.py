#!/usr/bin/env python3
"""Validate a qiuzhao claim ledger without third-party dependencies."""

import argparse
import json
import math
from pathlib import Path
from typing import List
from urllib.parse import urlparse


ALLOWED_STATUSES = {"source_grounded", "user_attested", "inferred", "planned", "unknown"}
ALLOWED_SOURCE_TYPES = {"official", "repository", "user_document", "user_statement", "public_page"}


def validate_claim_ledger(data: dict) -> List[str]:
    errors: List[str] = []
    if not isinstance(data, dict):
        return ["ledger must be an object"]
    sources = data.get("sources", [])
    claims = data.get("claims", [])
    if not isinstance(sources, list):
        return ["sources must be a list"]
    if not isinstance(claims, list):
        return ["claims must be a list"]

    valid_sources = []
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            errors.append(f"sources[{index}] must be an object")
        else:
            valid_sources.append(source)
    source_ids = [source.get("id") for source in valid_sources]
    if any(not source_id for source_id in source_ids) or len(source_ids) != len(set(source_ids)):
        errors.append("source IDs must be present and unique")
    source_types = {}
    for source in valid_sources:
        source_types[source.get("id")] = source.get("type")
        if source.get("type") not in ALLOWED_SOURCE_TYPES:
            errors.append(f"{source.get('id', '<unknown>')}: invalid source type")
        url = source.get("url")
        if url:
            parsed = urlparse(str(url))
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                errors.append(f"{source.get('id', '<unknown>')}: unsafe URL")

    valid_claims = []
    for index, claim in enumerate(claims):
        if not isinstance(claim, dict):
            errors.append(f"claims[{index}] must be an object")
        else:
            valid_claims.append(claim)
    claim_ids = [claim.get("id") for claim in valid_claims]
    if any(not claim_id for claim_id in claim_ids) or len(claim_ids) != len(set(claim_ids)):
        errors.append("claim IDs must be present and unique")
    known_sources = set(source_ids)
    for claim in valid_claims:
        claim_id = claim.get("id", "<unknown>")
        if not claim.get("text"):
            errors.append(f"{claim_id}: missing text")
        if claim.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{claim_id}: invalid status")
        source_refs = claim.get("source_ids", [])
        if not isinstance(source_refs, list):
            errors.append(f"{claim_id}: source_ids must be a list")
            source_refs = []
        for source_id in source_refs:
            if source_id not in known_sources:
                errors.append(f"{claim_id}: unknown source {source_id}")
        if claim.get("status") == "source_grounded" and not any(
            source_id in known_sources and source_types.get(source_id) != "user_statement"
            for source_id in source_refs
        ):
            errors.append(f"{claim_id}: source_grounded requires an independent source")
        metric = claim.get("metric")
        if metric is not None and not isinstance(metric, dict):
            errors.append(f"{claim_id}: metric must be an object")
            continue
        if not isinstance(metric, dict):
            continue
        ratio_keys = {"numerator", "denominator", "displayed_percent"}
        if ratio_keys & set(metric) and not ratio_keys <= set(metric):
            errors.append(f"{claim_id}: incomplete ratio")
        elif ratio_keys <= set(metric):
            try:
                expected = float(metric["numerator"]) / float(metric["denominator"]) * 100
                displayed = float(metric["displayed_percent"])
            except (TypeError, ValueError, ZeroDivisionError):
                errors.append(f"{claim_id}: invalid ratio")
            else:
                if not math.isclose(expected, displayed, abs_tol=0.5):
                    errors.append(f"{claim_id}: inconsistent ratio")
        change_keys = {"baseline", "result", "change_percent"}
        if change_keys & set(metric) and not change_keys <= set(metric):
            errors.append(f"{claim_id}: incomplete baseline change")
        elif change_keys <= set(metric):
            try:
                baseline = float(metric["baseline"])
                result = float(metric["result"])
                displayed_change = float(metric["change_percent"])
                expected_change = (result - baseline) / abs(baseline) * 100
            except (TypeError, ValueError, ZeroDivisionError):
                errors.append(f"{claim_id}: invalid baseline change")
            else:
                if not math.isclose(expected_change, displayed_change, abs_tol=0.5):
                    errors.append(f"{claim_id}: inconsistent change")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()
    data = json.loads(args.ledger.read_text(encoding="utf-8"))
    errors = validate_claim_ledger(data)
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

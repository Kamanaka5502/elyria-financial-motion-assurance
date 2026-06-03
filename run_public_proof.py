#!/usr/bin/env python3
"""Public proof harness for Elyria Motion Guard.

Runs synthetic demo packets only. Produces public-safe proof summary.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List

from motion_guard_demo import run_packet

EXAMPLES = [
    Path("examples/demo_clean_motion.json"),
    Path("examples/demo_stale_authority.json"),
    Path("examples/demo_missing_evidence.json"),
    Path("examples/demo_beneficiary_mismatch.json"),
    Path("examples/demo_custody_break.json"),
    Path("examples/demo_irreversible_posture.json"),
    Path("examples/demo_review_required.json"),
    Path("examples/demo_escalation_required.json"),
]


def main() -> int:
    receipts = []
    for path in EXAMPLES:
        receipt = run_packet(path, write_receipt=True)
        receipts.append(asdict(receipt))

    passed = [r for r in receipts if r["passed"] is True]
    failed = [r for r in receipts if r["passed"] is False]
    unresolved = [r for r in receipts if r["passed"] is None]

    summary: Dict[str, object] = {
        "proof_id": "ELYRIA_MOTION_GUARD_PUBLIC_PROOF_V1_0",
        "public_safe": True,
        "synthetic_demo_only": True,
        "value_movement_performed": False,
        "total_cases": len(receipts),
        "passed_cases": len(passed),
        "failed_cases": len(failed),
        "unresolved_expected_cases": len(unresolved),
        "all_passed": len(failed) == 0 and len(unresolved) == 0,
        "decisions_observed": sorted({r["decision"] for r in receipts}),
        "receipts": receipts,
    }

    out = Path("receipts/MOTION_GUARD_PUBLIC_PROOF_SUMMARY.json")
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

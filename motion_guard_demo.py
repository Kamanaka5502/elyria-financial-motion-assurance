#!/usr/bin/env python3
"""Elyria Motion Guard public-safe demo runtime.

This file evaluates synthetic motion packets only.
It does not execute payments, connect to rails, access accounts, or move value.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List

SUITE_ID = "ELYRIA_MOTION_GUARD_PUBLIC_DEMO_V1_0"
POLICY_ID = "MOTION_GUARD_PUBLIC_DEMO_POLICY_V1_0"
RECEIPT_DIR = Path("receipts")


@dataclass(frozen=True)
class DemoReceipt:
    suite_id: str
    policy_id: str
    packet_id: str
    decision: str
    expected_decision: str | None
    passed: bool | None
    logic_word: str
    chute: str
    reason: str
    blocking_facts: List[str]
    repair_facts: List[str]
    escalation_facts: List[str]
    review_facts: List[str]
    packet_hash: str
    policy_hash: str
    issued_at_ms: int
    receipt_hash: str


def stable_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def public_policy_hash() -> str:
    policy = {
        "policy_id": POLICY_ID,
        "demo_only": True,
        "no_value_movement": True,
        "invariants": ["AUTHORITY", "EVIDENCE", "BENEFICIARY", "CUSTODY", "SETTLEMENT", "REVERSIBILITY"],
        "outcomes": ["ADMIT", "REFUSE", "REPAIR", "QUARANTINE", "ESCALATE", "REVIEW", "FAIL_CLOSED"],
    }
    return sha256_text(stable_json(policy))


def evaluate_packet(packet: Dict[str, Any]) -> Dict[str, Any]:
    facts = packet.get("facts", {})
    blocking: List[str] = []
    repair: List[str] = []
    escalation: List[str] = []
    review: List[str] = []

    if not facts.get("actor_authorized", False):
        blocking.append("actor_not_authorized")
    if not facts.get("approval_current", False):
        blocking.append("approval_not_current")
    if not facts.get("beneficiary_verified", False):
        blocking.append("beneficiary_not_verified")
    if facts.get("beneficiary_mismatch", False):
        blocking.append("beneficiary_mismatch")
    if not facts.get("custody_path_valid", False):
        blocking.append("custody_path_invalid")
    if facts.get("settlement_drift", False):
        blocking.append("settlement_drift")
    if not facts.get("system_record_match", False):
        blocking.append("system_record_mismatch")
    if not facts.get("evidence_complete", False):
        repair.append("evidence_incomplete")
    if facts.get("review_required", False):
        review.append("review_required")
    if facts.get("escalation_required", False):
        escalation.append("escalation_required")

    if not facts.get("reversible", True):
        return {
            "decision": "FAIL_CLOSED",
            "logic_word": "REVERSIBILITY",
            "chute": "FAIL_CLOSED",
            "reason": "synthetic motion failed closed because reversibility is unsafe",
            "blocking_facts": blocking + ["irreversible_posture"],
            "repair_facts": repair,
            "escalation_facts": escalation,
            "review_facts": review,
        }

    if any(x in blocking for x in ["custody_path_invalid", "settlement_drift", "system_record_mismatch"]):
        return {
            "decision": "QUARANTINE",
            "logic_word": "CUSTODY_SETTLEMENT",
            "chute": "QUARANTINE",
            "reason": "synthetic motion isolated because custody, settlement, or record alignment failed",
            "blocking_facts": blocking,
            "repair_facts": repair,
            "escalation_facts": escalation,
            "review_facts": review,
        }

    if blocking:
        return {
            "decision": "REFUSE",
            "logic_word": "AUTHORITY_BENEFICIARY",
            "chute": "REFUSE",
            "reason": "synthetic motion refused because authority, approval, or beneficiary integrity failed",
            "blocking_facts": blocking,
            "repair_facts": repair,
            "escalation_facts": escalation,
            "review_facts": review,
        }

    if repair:
        return {
            "decision": "REPAIR",
            "logic_word": "EVIDENCE",
            "chute": "REPAIR_NON_BINDING",
            "reason": "synthetic motion requires non-binding evidence repair before admission",
            "blocking_facts": blocking,
            "repair_facts": repair,
            "escalation_facts": escalation,
            "review_facts": review,
        }

    if escalation:
        return {
            "decision": "ESCALATE",
            "logic_word": "ESCALATION",
            "chute": "ESCALATE_NON_BINDING",
            "reason": "synthetic motion requires non-binding escalation before admission",
            "blocking_facts": blocking,
            "repair_facts": repair,
            "escalation_facts": escalation,
            "review_facts": review,
        }

    if review:
        return {
            "decision": "REVIEW",
            "logic_word": "REVIEW",
            "chute": "REVIEW_NON_BINDING",
            "reason": "synthetic motion requires non-binding review before admission",
            "blocking_facts": blocking,
            "repair_facts": repair,
            "escalation_facts": escalation,
            "review_facts": review,
        }

    return {
        "decision": "ADMIT",
        "logic_word": "ADMISSIBLE_SYNTHETIC_MOTION",
        "chute": "ADMIT",
        "reason": "synthetic motion satisfies the public demo admission checks",
        "blocking_facts": blocking,
        "repair_facts": repair,
        "escalation_facts": escalation,
        "review_facts": review,
    }


def build_receipt(packet: Dict[str, Any]) -> DemoReceipt:
    result = evaluate_packet(packet)
    expected = packet.get("expected_decision")
    passed = None if expected is None else expected == result["decision"]
    packet_hash = sha256_text(stable_json(packet))
    p_hash = public_policy_hash()
    basis = {
        "suite_id": SUITE_ID,
        "policy_id": POLICY_ID,
        "packet_id": packet.get("packet_id", "UNKNOWN_PACKET"),
        "decision": result["decision"],
        "logic_word": result["logic_word"],
        "chute": result["chute"],
        "packet_hash": packet_hash,
        "policy_hash": p_hash,
    }
    return DemoReceipt(
        suite_id=SUITE_ID,
        policy_id=POLICY_ID,
        packet_id=packet.get("packet_id", "UNKNOWN_PACKET"),
        decision=result["decision"],
        expected_decision=expected,
        passed=passed,
        logic_word=result["logic_word"],
        chute=result["chute"],
        reason=result["reason"],
        blocking_facts=result["blocking_facts"],
        repair_facts=result["repair_facts"],
        escalation_facts=result["escalation_facts"],
        review_facts=result["review_facts"],
        packet_hash=packet_hash,
        policy_hash=p_hash,
        issued_at_ms=int(time.time() * 1000),
        receipt_hash=sha256_text(stable_json(basis)),
    )


def run_packet(path: Path, write_receipt: bool = True) -> DemoReceipt:
    packet = json.loads(path.read_text(encoding="utf-8"))
    receipt = build_receipt(packet)
    if write_receipt:
        RECEIPT_DIR.mkdir(exist_ok=True)
        out = RECEIPT_DIR / f"{receipt.packet_id}.receipt.json"
        out.write_text(json.dumps(asdict(receipt), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description="Elyria Motion Guard public-safe demo")
    parser.add_argument("packet", type=Path)
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()
    receipt = run_packet(args.packet, write_receipt=not args.no_write)
    print(json.dumps(asdict(receipt), indent=2, sort_keys=True))
    return 0 if receipt.passed is not False else 1


if __name__ == "__main__":
    raise SystemExit(main())

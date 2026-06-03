<p align="center">
  <img src="assets/elyria_motion_guard_hero.jpg" alt="Elyria Motion Guard" width="100%">
</p>

<p align="center">
  <img alt="Motion Guard" src="https://img.shields.io/badge/ELYRIA-MOTION_GUARD-00d9ff?style=for-the-badge">
  <img alt="Secure" src="https://img.shields.io/badge/SECURE-GOVERNED_DYNAMIC-14f195?style=for-the-badge">
  <img alt="Wrapper" src="https://img.shields.io/badge/WRAPPER-OLD_STACK_COMPATIBLE-0284c7?style=for-the-badge">
  <img alt="Fail Closed" src="https://img.shields.io/badge/FAIL_CLOSED-CONSEQUENCE_CONTROL-ff8a00?style=for-the-badge">
</p>

# Elyria Motion Guard

Old-stack compatible pre-execution motion-admission wrapper for AI-assisted financial intent, invariant routing, non-binding review, replayable receipts, and fail-closed consequence control.

<p align="center">
  <img alt="Intent" src="https://img.shields.io/badge/AI_INTENT-NOT_EXECUTABLE_MONEY_MOVEMENT-00d9ff?style=for-the-badge">
</p>

```text
AI-assisted financial intent is not executable money movement.
```

Elyria Motion Guard is the small sellable wrapper around the larger Elyria/Veritas motion-governance substrate.

It is designed for finance teams, accounts payable workflows, fractional CFOs, payment operators, and AI automation agencies that need a simple control before payment intent becomes value-bearing motion.

## Start Here

<p align="center">
  <img alt="Instruction" src="https://img.shields.io/badge/FINANCIAL_INSTRUCTION-EXISTS-00b8d9?style=for-the-badge">
  <img alt="Not Equal" src="https://img.shields.io/badge/DOES_NOT_EQUAL-MOTION_MAY_BIND-ff8a00?style=for-the-badge">
</p>

```text
Financial instruction exists
  !=
Financial motion may bind
```

Motion Guard asks:

<p align="center">
  <img alt="Core Question" src="https://img.shields.io/badge/CORE_QUESTION-MAY_THIS_INTENT_BIND_CONSEQUENCE-14f195?style=for-the-badge">
</p>

```text
May this AI-assisted financial intent become value-bearing motion?
```

## Old-Stack Compatible Interface

<p align="center">
  <img alt="JSON" src="https://img.shields.io/badge/JSON-IN-00d9ff?style=for-the-badge">
  <img alt="CLI" src="https://img.shields.io/badge/CLI-READY-0284c7?style=for-the-badge">
  <img alt="AP" src="https://img.shields.io/badge/AP_WORKFLOW-COMPATIBLE-14f195?style=for-the-badge">
  <img alt="Receipt" src="https://img.shields.io/badge/RECEIPT-OUT-6a5cff?style=for-the-badge">
</p>

Motion Guard exposes a simple interface:

```text
JSON payment-intent packet in
  -> invariant checks
  -> gate decision
  -> chute outcome
  -> replayable receipt out
```

It can be used from CLI, scripts, AP workflows, or later CSV / web-form adapters.

## New-Stack Governance Core

<p align="center">
  <img alt="Kernel" src="https://img.shields.io/badge/KERNEL-GOVERNED-6a5cff?style=for-the-badge">
  <img alt="Invariant" src="https://img.shields.io/badge/INVARIANT-RESOLUTION-00d9ff?style=for-the-badge">
  <img alt="Word" src="https://img.shields.io/badge/LOGIC_WORD-ROUTES_CHUTE-14f195?style=for-the-badge">
  <img alt="Replay" src="https://img.shields.io/badge/REPLAY-PRESERVED-0284c7?style=for-the-badge">
</p>

The external interface is old-stack compatible.

The internal order remains kernel-governed:

```text
kernel governance
  -> invariant resolution
  -> logic word
  -> gate
  -> chute
  -> receipt
  -> replay
```

## Invariants

<p align="center">
  <img alt="Authority" src="https://img.shields.io/badge/AUTHORITY-REFUSE_IF_BROKEN-b91c1c?style=for-the-badge">
  <img alt="Evidence" src="https://img.shields.io/badge/EVIDENCE-REPAIR_IF_GAPPED-ff8a00?style=for-the-badge">
  <img alt="Beneficiary" src="https://img.shields.io/badge/BENEFICIARY-VERIFY_MATCH-14f195?style=for-the-badge">
  <img alt="Custody" src="https://img.shields.io/badge/CUSTODY-QUARANTINE_IF_BROKEN-6a5cff?style=for-the-badge">
  <img alt="Settlement" src="https://img.shields.io/badge/SETTLEMENT-ROUTE_CHECK-00b8d9?style=for-the-badge">
  <img alt="Reversibility" src="https://img.shields.io/badge/REVERSIBILITY-FAIL_CLOSED-301018?style=for-the-badge">
</p>

```text
AUTHORITY
EVIDENCE
BENEFICIARY
CUSTODY
SETTLEMENT
REVERSIBILITY
```

## Outcomes

<p align="center">
  <img alt="Admit" src="https://img.shields.io/badge/ADMIT-00d9ff?style=for-the-badge">
  <img alt="Refuse" src="https://img.shields.io/badge/REFUSE-b91c1c?style=for-the-badge">
  <img alt="Repair" src="https://img.shields.io/badge/REPAIR-ff8a00?style=for-the-badge">
  <img alt="Quarantine" src="https://img.shields.io/badge/QUARANTINE-6a5cff?style=for-the-badge">
  <img alt="Escalate" src="https://img.shields.io/badge/ESCALATE_NON_BINDING-ffe066?style=for-the-badge">
  <img alt="Fail Closed" src="https://img.shields.io/badge/FAIL_CLOSED-301018?style=for-the-badge">
</p>

```text
ADMIT
REFUSE
REPAIR
QUARANTINE
ESCALATE
FAIL_CLOSED
```

Review, repair, and escalation are non-binding. No payment motion is admitted while review, repair, or escalation remains unresolved.

## Run

<p align="center">
  <img alt="Run" src="https://img.shields.io/badge/RUN-EXAMPLES-00d9ff?style=for-the-badge">
  <img alt="Proof" src="https://img.shields.io/badge/PROOF-HARNESS-14f195?style=for-the-badge">
</p>

```bash
python motion_guard.py examples/clean_payment.json
python motion_guard.py examples/stale_approval.json
python motion_guard.py examples/beneficiary_mismatch.json
python motion_guard.py examples/missing_evidence.json
python motion_guard.py examples/irreversible_transfer.json
```

Run the public proof harness:

```bash
python run_proof.py
```

Expected result:

```text
all_passed: true
```

## Boundary

<p align="center">
  <img alt="No Rails" src="https://img.shields.io/badge/NO_PAYMENT_RAILS-BOUNDARY_LOCKED-334155?style=for-the-badge">
  <img alt="No Execution" src="https://img.shields.io/badge/NO_PAYMENT_EXECUTION-REVIEW_ONLY-334155?style=for-the-badge">
  <img alt="Private Substrate" src="https://img.shields.io/badge/PROTECTED_SUBSTRATE-PRIVATE-6a5cff?style=for-the-badge">
</p>

This wrapper does not execute payments, connect to payment rails, replace accounting systems, replace legal/compliance review, or expose the protected Elyria/Veritas substrate.

It evaluates motion admission before value-bearing consequence binds.

## Product Line

<p align="center">
  <img alt="Motion Guard" src="https://img.shields.io/badge/MOTION_GUARD-SMALL_COMMERCIAL_CORRIDOR-00d9ff?style=for-the-badge">
  <img alt="Financial Governance" src="https://img.shields.io/badge/FINANCIAL_MOTION_GOVERNANCE-PROOF_SURFACE-0284c7?style=for-the-badge">
  <img alt="Substrate" src="https://img.shields.io/badge/ELYRIA_VERITAS_SUBSTRATE-PROTECTED_RUNTIME-6a5cff?style=for-the-badge">
</p>

```text
Elyria Motion Guard
  -> small wrapper / first commercial corridor

Elyria Financial Motion Governance
  -> public proof-surface / enterprise substrate framing

Elyria / Veritas substrate
  -> protected commercial runtime
```

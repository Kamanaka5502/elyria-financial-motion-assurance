<p align="center">
  <img src="assets/elyria_financial_motion_assurance_hero.jpg" alt="Elyria Financial Motion Assurance" width="100%">
</p>

<p align="center">
  <img alt="Elyria" src="https://img.shields.io/badge/ELYRIA-FINANCIAL_MOTION_ASSURANCE-00d9ff?style=for-the-badge">
  <img alt="Assurance" src="https://img.shields.io/badge/ASSURANCE-PRE_EXECUTION-0284c7?style=for-the-badge">
  <img alt="Interface" src="https://img.shields.io/badge/INTERFACE-OLD_STACK_COMPATIBLE-334155?style=for-the-badge">
  <img alt="Receipts" src="https://img.shields.io/badge/RECEIPTS-REPLAYABLE-14f195?style=for-the-badge">
  <img alt="Fail Closed" src="https://img.shields.io/badge/FAIL_CLOSED-CONSEQUENCE_CONTROL-b91c1c?style=for-the-badge">
</p>

# Elyria Financial Motion Assurance

Old-stack compatible pre-execution assurance wrapper for AI-assisted financial intent, motion admission, non-binding review, replayable receipts, and fail-closed consequence control.

```text
AI-generated financial intent is not executable money movement.
```

Elyria Financial Motion Assurance is the smaller sellable wrapper around the larger Elyria / Veritas motion-governance substrate.

It is designed for finance teams, accounts payable workflows, fractional CFOs, payment operators, and AI automation agencies that need a simple assurance surface before financial intent becomes value-bearing motion.

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

Financial Motion Assurance asks:

<p align="center">
  <img alt="Core Question" src="https://img.shields.io/badge/CORE_QUESTION-MAY_THIS_INTENT_BIND_CONSEQUENCE-14f195?style=for-the-badge">
</p>

```text
May this AI-assisted financial intent become value-bearing motion?
```

## Old-Stack Compatible Assurance Surface

<p align="center">
  <img alt="JSON" src="https://img.shields.io/badge/JSON-DEMO_PACKET_IN-00d9ff?style=for-the-badge">
  <img alt="CLI" src="https://img.shields.io/badge/CLI-DEMO_READY-0284c7?style=for-the-badge">
  <img alt="AP" src="https://img.shields.io/badge/AP_WORKFLOW-REVIEW_SURFACE-14f195?style=for-the-badge">
  <img alt="Receipt" src="https://img.shields.io/badge/RECEIPT-OUT-6a5cff?style=for-the-badge">
</p>

The public demonstrator exposes a simple interface:

```text
synthetic financial-motion packet in
  -> invariant checks
  -> admission / non-admission posture
  -> chute outcome
  -> replayable receipt out
```

It can be used from CLI, scripts, review packets, AP workflows, or later CSV / web-form adapters.

## Kernel-Governed Core

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

The gate does not discover governance. It applies governance already decided in the kernel.

## Assurance Invariants

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
  <img alt="Repair" src="https://img.shields.io/badge/REPAIR_NON_BINDING-ff8a00?style=for-the-badge">
  <img alt="Review" src="https://img.shields.io/badge/REVIEW_NON_BINDING-0284c7?style=for-the-badge">
  <img alt="Quarantine" src="https://img.shields.io/badge/QUARANTINE-6a5cff?style=for-the-badge">
  <img alt="Escalate" src="https://img.shields.io/badge/ESCALATE_NON_BINDING-ffe066?style=for-the-badge">
  <img alt="Fail Closed" src="https://img.shields.io/badge/FAIL_CLOSED-301018?style=for-the-badge">
</p>

```text
ADMIT
REFUSE
REPAIR
REVIEW
QUARANTINE
ESCALATE
FAIL_CLOSED
```

Review, repair, and escalation are non-binding. No financial motion is admitted while review, repair, or escalation remains unresolved.

## Public Demo Run

<p align="center">
  <img alt="Run" src="https://img.shields.io/badge/RUN-SYNTHETIC_EXAMPLES-00d9ff?style=for-the-badge">
  <img alt="Proof" src="https://img.shields.io/badge/PROOF-PUBLIC_HARNESS-14f195?style=for-the-badge">
  <img alt="No Value" src="https://img.shields.io/badge/VALUE_MOVEMENT-FALSE-334155?style=for-the-badge">
</p>

```bash
python motion_guard_demo.py examples/demo_clean_motion.json
python motion_guard_demo.py examples/demo_stale_authority.json
python motion_guard_demo.py examples/demo_missing_evidence.json
python motion_guard_demo.py examples/demo_beneficiary_mismatch.json
python motion_guard_demo.py examples/demo_custody_break.json
python motion_guard_demo.py examples/demo_irreversible_posture.json
```

Run the public proof harness:

```bash
python run_public_proof.py
```

Expected result:

```text
all_passed: true
value_movement_performed: false
synthetic_demo_only: true
```

## Boundary

<p align="center">
  <img alt="No Rails" src="https://img.shields.io/badge/NO_PAYMENT_RAILS-BOUNDARY_LOCKED-334155?style=for-the-badge">
  <img alt="No Execution" src="https://img.shields.io/badge/NO_VALUE_EXECUTION-DEMO_ONLY-334155?style=for-the-badge">
  <img alt="Private Substrate" src="https://img.shields.io/badge/PROTECTED_SUBSTRATE-PRIVATE-6a5cff?style=for-the-badge">
</p>

This wrapper does not execute payments, connect to payment rails, replace accounting systems, replace legal/compliance review, or expose the protected Elyria / Veritas substrate.

It evaluates motion admission before value-bearing consequence binds.

## Product Line

<p align="center">
  <img alt="Assurance" src="https://img.shields.io/badge/FINANCIAL_MOTION_ASSURANCE-SMALL_COMMERCIAL_CORRIDOR-00d9ff?style=for-the-badge">
  <img alt="Governance" src="https://img.shields.io/badge/FINANCIAL_MOTION_GOVERNANCE-PROOF_SURFACE-0284c7?style=for-the-badge">
  <img alt="Substrate" src="https://img.shields.io/badge/ELYRIA_VERITAS_SUBSTRATE-PROTECTED_RUNTIME-6a5cff?style=for-the-badge">
</p>

```text
Elyria Financial Motion Assurance
  -> smaller assurance wrapper / first commercial corridor

Elyria Financial Motion Governance
  -> public proof-surface / enterprise substrate framing

Elyria / Veritas substrate
  -> protected commercial runtime
```

## Final Line

```text
Do not ask whether AI produced a financial instruction.
Ask whether the instruction is admissible financial motion before consequence binds.
```

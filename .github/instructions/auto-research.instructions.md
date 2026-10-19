---
applyTo: "**"
---


# Autoresearch: Experiment-Driven Performance Improvement

Project VIC tools must not be optimized by intuition alone when performance is part of the requirement.

After a feature meets its functional spec, use experiment-driven autoresearch for performance-critical improvements. This means forming one measurable hypothesis, changing one variable, benchmarking the result, and keeping only verified improvements.

Correctness, forensic integrity, security, privacy, provenance, ontology alignment, and operator trust take priority over speed.

## When This Rule Applies

Use this loop when:

- A spec defines a performance threshold.
- A user or maintainer requests performance improvement.
- A feature processes large media collections, hash sets, archives, reports, exports, model inference, or GUI result sets.
- A bottleneck affects investigator usability, batch throughput, offline operation, or deployment feasibility.
- Release notes or changelog entries will claim a measurable performance improvement.

Do not run autoresearch for ordinary feature work, typo fixes, small correctness bugs, documentation-only edits, or security fixes unless performance is part of the acceptance criteria.

## Loop

1. Read the spec threshold, acceptance criteria, and current benchmark baseline.
2. Identify the bottleneck with measurement before changing code.
3. Hypothesize one measurable change.
4. Implement the change in an isolated branch, worktree, or subagent attempt.
5. Measure with the same dataset, hardware profile, configuration, command, and version baseline.
6. Compare before/after results.
7. Keep only verified improvements that preserve correctness and required behavior.
8. Add or update regression protection.
9. Ratchet the spec floor only when the improvement is merged and realistic for the intended deployment tier.

## Project VIC Performance Targets

Use this loop for performance-sensitive areas such as media discovery, hashing, Project VIC lookup matching, archive preprocessing, forensic image handling, video frame sampling, object detection or model inference throughput, OCR or transcription pipelines, artifact generation, JSON/CSV/XLSX/JSON-LD/Turtle/RDF/report export speed, CASE/UCO/CAC validation speed, API job throughput, CLI batch processing, MCP tool latency, GUI result rendering at scale, Docker startup and deployment performance, CPU-only fallback performance, and GPU utilization or memory behavior.

## Safety and Correctness Requirements

Never keep a performance improvement that changes investigative meaning, mutates source evidence, skips required validation, weakens authentication or authorization, drops audit or provenance events, removes ontology-aligned output, changes report/export semantics without a spec update, hides errors, creates fake success paths, breaks CPU-only operation unless explicitly approved, increases minimum hardware requirements without documentation and approval, requires internet access in offline or air-gapped workflows, leaks sensitive data in benchmark logs, or reduces accessibility or operator clarity.

Performance improvements must preserve the no-stubs, security, ontology-alignment, cross-platform, four-surface, and release-management rules.

## Benchmark Data

- Use benign synthetic or approved non-sensitive datasets.
- Never use real CSAM, real victim data, real agency data, real case identifiers, or sensitive investigative material in benchmark fixtures, logs, screenshots, or reports.
- Record dataset size, file counts, media types, archive types, hash counts, model names, and relevant configuration.
- If synthetic data is used, describe how it approximates the operational workload.
- If the benchmark does not represent real-world investigator use, state that limitation.

## Hardware and Deployment Profiles

Record the hardware and deployment profile for each experiment, including CPU model, RAM, GPU model and VRAM, driver/runtime version, operating system, WSL/Linux/Docker profile, storage type, container image or environment, CPU-only versus GPU mode, model precision or quantization, offline/air-gapped profile, and relevant environment variables where applicable.

Do not optimize only for high-end GPUs if intended users include low-resource investigators. Maintain realistic baselines for CPU-only and modest workstation deployments where applicable.

## Experiment Rules

- One experiment changes one variable.
- Measure before changing code.
- Use the same command, dataset, configuration, and hardware profile for before/after comparisons.
- Run enough repetitions to avoid obvious noise when the benchmark is short or variable.
- Record wall-clock time, throughput, memory use, error rate, and output equivalence where applicable.
- Validate that output artifacts remain equivalent unless the spec intentionally changes them.
- Stop after at least three consecutive low-value experiments or when the bottleneck is outside the module.
- Do not keep code that adds complexity without measurable benefit.
- Do not merge experimental branches that lack tests, documentation, or reproducible results.

## Output Equivalence

For performance work that changes processing, exports, or rendering:

- Verify source evidence remains read-only.
- Verify derived artifacts stay in approved output locations.
- Verify hashes, classifications, detections, reports, and exports remain semantically consistent.
- Verify CASE/UCO/CAC/SOLVE-IT output still validates where applicable.
- Verify GUI, API, CLI, and MCP surfaces still expose equivalent behavior where applicable.
- Verify errors remain actionable and safe.

## Research Logs

Store experiment records in the feature `research.md`, `tools/autoresearch/results/`, the relevant Spec Kit research document, or another documented repository location.

Each experiment record must include hypothesis, changed variable, commit or branch, benchmark command, dataset description, hardware profile, software/container version, before metrics, after metrics, output equivalence result, decision to keep/reject/retry/defer, and reason for the decision.

## Regression Protection

When a performance improvement merges:

- Add or update a benchmark, regression test, CI check, or documented manual verification step.
- Update spec thresholds when the new floor is realistic for the intended deployment tier.
- Update documentation if hardware, configuration, or operator guidance changes.
- Update `CHANGELOG.md` and release notes when the improvement is user-visible or operationally relevant.
- Include before/after measurements and test conditions in performance-related release notes.

## Spec Kit Requirements

For performance-relevant work:

- `/speckit.specify`: define the performance target, affected users, workload, dataset assumptions, hardware/deployment tier, correctness requirements, and success threshold.
- `/speckit.plan`: define the benchmark method, baseline command, metrics, profiling approach, safety checks, and regression protection.
- `/speckit.tasks`: create concrete tasks for profiling, experiments, implementation, validation, documentation, changelog, and release notes.
- `/speckit.implement`: run measured experiments and keep only verified improvements.
- `/speckit.analyze`: verify the improvement is real, reproducible, safe, documented, tested, and aligned with the spec.

## Required Agent Output

For performance-relevant changes, the final agent response must summarize baseline measured, bottleneck identified, experiment attempted, variable changed, dataset used, hardware/deployment profile, before/after metrics, correctness and output-equivalence checks, whether the change was kept or rejected, regression protection added, and spec threshold/changelog/docs/release notes updated.

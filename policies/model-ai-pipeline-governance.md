---
description: Governance for model and AI features - output labeling, provenance, evaluation, detection-quality regression gates, research-to-production graduation, and offline runtime
globs: ["**/ml/**", "**/inference/**", "**/detectors/**", "**/*classif*", "**/*detect*", "**/eval/**", "**/benchmarks/**", "**/*.onnx", "**/*.pt", "**/*.safetensors"]
alwaysApply: false
---

# Model and AI Pipeline Governance

Model and AI features must support investigators without overstating certainty. Model outputs are analytic assistance, not determinations of fact, guilt, victim status, or legal classification.

AI and ML changes must preserve forensic integrity, security, privacy, ontology alignment, surface equivalence, and human review expectations.

This policy covers AI features **inside the tool you build**. Rules for the coding agent that helps you build it are in `policies/security-compliance.md` and `policies/mcp-agent-safety.md`.

## Model Output Requirements

- Label model outputs as classifications, detections, predictions, scores, or analytic results, not facts.
- Store model name, version, weights checksum, runtime, parameters, confidence or score, thresholds, input artifact references, and provenance.
- Distinguish model confidence from forensic certainty.
- Do not hide false positives, false negatives, uncertainty, threshold limitations, or unsupported classes.
- Operator-facing text must explain what the model did, what it did not do, and what human review is expected.
- Use the shared confidence vocabulary from `policies/brand-design-system.md`.

## Model Updates and Evaluation

- Model updates require benchmark or evaluation notes before merge or release.
- Evaluation must document dataset type, size, class coverage, metrics, hardware, runtime, and limitations.
- Use benign synthetic or approved non-sensitive evaluation data unless repository policy explicitly permits another safe dataset.
- Never use real CSAM, real victim data, real agency data, or sensitive investigative material in model tests, docs, screenshots, or benchmark logs.
- Performance claims require measured benchmarks and output-equivalence checks.
- Consider whether evaluation data represents the populations, languages, devices, and regions where the tool will be used, and document known gaps.

## Detection Quality Baselines and Regression Gates

Repositories that ship detectors, classifiers, or scoring models exposed to operators must protect detection quality the same way they protect code quality:

- Maintain a versioned evaluation corpus (or a committed public-safe slice of one) and a repeatable evaluation command that reports task-appropriate metrics such as ROC-AUC, PR-AUC, EER, false-positive rate at a fixed operating point, and calibration error.
- Add a CI regression gate on the committed evaluation slice with checked-in metric floors. A change to a model, weight file, threshold, fusion logic, or preprocessing step that degrades gated metrics must block merge unless a maintainer documents acceptance of the regression.
- Ratchet metric floors only through merged, verified improvements (see `policies/auto-research.md`; its measurement discipline applies to detection-quality metrics, not only speed).
- A detector whose required dependencies, weights, or runtime are unavailable must be reported as unavailable and must degrade the overall result honestly (capped, labeled, and shown to the operator). Passing process gates while a primary detector silently does not run is a release-blocking defect, not a warning.
- Record the evaluation dataset version, hardware profile, and metric results in the spec's research notes or a documented results location so claims are reproducible.

## Research-to-Production Graduation

New model or detector candidates follow a staged path; do not skip stages:

1. **Candidate review:** record source, code and weights availability, license and redistribution rights, runtime fit (CPU, offline), and evidence quality in a candidate matrix before any code lands.
2. **Isolated prototype:** implement in a prototype namespace, branch, or worktree with no GUI/API/CLI/MCP, report, export, audit, or ontology exposure. Prototypes fail honestly and are labeled diagnostic-only.
3. **Recorded decision:** every prototype ends with an explicit **graduate**, **iterate** (with a revisit date or milestone), or **retire** decision recorded in the spec. Prototypes must not remain dark indefinitely without a recorded owner and revisit point.
4. **Implementation spec:** graduation to production requires a follow-up spec covering benchmark evidence, calibration or explicit uncalibrated labeling, four-surface contracts, provenance and ontology mapping, offline prestaging, and human review of operator-facing claims.

## Deployment and Runtime

- Document CPU/GPU behavior, memory assumptions, model precision or quantization, and fallback behavior.
- GPU acceleration must not break CPU-only operation unless the feature is explicitly GPU-only.
- Model downloads must support offline and air-gapped workflows where applicable.
- Document model weights, licenses, redistribution limits, checksums, and source URLs.
- Do not send evidence, derived artifacts, embeddings, thumbnails, prompts, or investigative metadata to external model APIs unless explicitly approved for the deployment context and jurisdiction.

## Provenance and Ontology

- Model inference, preprocessing, postprocessing, thresholding, and export generation are provenance actions.
- CASE/UCO/CAC/SOLVE-IT outputs must represent model results with tool and model provenance, confidence, and validation status where applicable.
- Reports, API, CLI, GUI, and MCP outputs must describe model results consistently.

## Spec Kit Requirements

For model- or AI-relevant work:

- `/speckit.specify`: identify model purpose, users, supported classes, inputs/outputs, thresholds, human-review expectations, protected data, and success metrics.
- `/speckit.plan`: define model versioning, provenance, evaluation method, benchmark data, deployment profile, CPU/GPU behavior, license, and offline handling.
- `/speckit.tasks`: create tasks for implementation, tests, evaluation evidence, docs, changelog, release notes, and model artifact metadata.
- `/speckit.implement`: implement real inference and evaluation behavior with documented thresholds and no fake detections.
- `/speckit.analyze`: verify model claims, provenance, evaluation evidence, docs, and surfaces remain aligned.

## Required Agent Output

For model or AI changes, the final agent response must summarize model, version, and weights, thresholds, evaluation evidence, false-positive/false-negative considerations, provenance captured, CPU/GPU/offline behavior, sensitive-data controls, tests, and docs/release updates.

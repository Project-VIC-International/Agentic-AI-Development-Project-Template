# Manual Test Checklist

Use this **Layer A** master checklist when you test your tool by hand. Your agent can test the code; you test whether the tool actually works for an investigator. Then tell the agent what to fix.

It complements the automated testing program (`policies/testing-program.md`) and the test design rules (`policies/testing-quality.md`).

**Related documents:**

- Release-specific scenarios (**Layer B**): copy `docs/templates/manual-test-release-annex.md` into the active release spec folder.
- Pull-request subset (**Layer C**): `.github/pull_request_template.md`.
- Test data tiers: `docs/test-data-handling.md` (T0/T1 only during the course).

Early versions do not need every section. Mark a section **N/A** with a short reason when it does not apply yet.

## Standards

This checklist follows risk-based acceptance practices from ISO/IEC/IEEE 29119 (traceability and records), ISTQB test levels, OWASP verification themes for security spot-checks, WCAG 2.2 for accessibility spot-checks, and session-based exploratory testing.

---

## Layer A: Master Checklist

### 0. Session setup

- [ ] **Build under test** recorded: version, commit or tag, container image digest if applicable
- [ ] **Environment** recorded: OS, WSL or native, Docker Compose profile, CPU-only or GPU, online or offline
- [ ] **Data tier** recorded: T0 \| T1 \| T2 \| T3 per `docs/test-data-handling.md`
- [ ] **Handling plan** linked if T2+; tier not mislabeled
- [ ] **Channels** respected: no T2+ content in pull requests, CI, issues, or AI agent prompts unless the plan allows it
- [ ] **Scope** defined: full release, Layer B annex only, or Layer C subset; GitHub milestone and issues linked
- [ ] **Automation baseline** noted: local test command run; CI run links if CI exists
- [ ] **Known limitations** from the release notes reviewed; deferred features not tested as working

### 1. Requirements traceability

- [ ] Each acceptance criterion in the release spec exercised, or N/A with an issue link
- [ ] Declared surfaces (GUI, API, CLI, MCP) exercised with the same scenario and comparable results
- [ ] README and quickstart steps work without undeclared secrets or hidden steps
- [ ] `CHANGELOG.md` and release notes match observed behavior

### 2. Core workflows

For each main investigator journey (listed in the Layer B annex):

- [ ] Happy path completes with the expected results (job status, files, exports)
- [ ] Invalid input is rejected with a clear, actionable error (no silent failure)
- [ ] A missing dependency fails honestly (for example no GPU, no `ffmpeg`, no lookup database, no model weights)
- [ ] An interrupted run (cancel, close the browser, stop the CLI) leaves a safe state; source evidence is unaffected
- [ ] Running the same input again behaves as documented
- [ ] A least-privilege user cannot perform protected actions

### 3. Evidence and forensic integrity

- [ ] Source evidence and input folders are **unchanged** after processing (read-only mount or hash spot-check)
- [ ] Derived output appears only in the configured case, run, or output folders
- [ ] Unsafe archives or uploads are rejected (path traversal, oversize, unsafe types) where applicable
- [ ] Exports and downloads do not expose unnecessary sensitive paths or identifiers
- [ ] Temporary and cache behavior matches the docs; cleanup never deletes source evidence

### 4. Security and privacy (manual, not scanner-only)

- [ ] Authentication is enforced where configured; invalid credentials are blocked
- [ ] Users cannot reach other users' cases, jobs, or artifacts
- [ ] Logout ends access; no secrets in browser-visible storage unless documented for local development only
- [ ] Direct API or CLI calls have the same restrictions as the GUI
- [ ] Logs, errors, exports, and the UI minimize sensitive fields
- [ ] MCP tools return bounded errors without extra case or evidence detail
- [ ] Dependency and image scan findings for this release reviewed; critical/high dispositions recorded

### 5. Data contracts, reports, and ontology

- [ ] Sample API, CLI, and MCP outputs match the documented schemas
- [ ] Human-readable reports agree with machine-readable exports (no conflicting counts or labels)
- [ ] CASE/UCO/CAC/SOLVE-IT export spot-check; validation command run where applicable
- [ ] Legacy lookup hashes (for example MD5) are labeled separately from integrity hashes (for example SHA-256)
- [ ] Representative actions produce audit or provenance records without sensitive leakage

### 6. Model and AI features (if in scope)

- [ ] Confidence and threshold behavior matches the documentation
- [ ] No fake or placeholder detections presented as real
- [ ] Model or tool version appears in metadata or exports where claimed
- [ ] CPU-only path verified when the product claims CPU support

### 7. Deployment and platform

- [ ] Documented Docker Compose profiles start and pass health checks
- [ ] Windows with WSL, macOS, or Linux paths exercised as documented
- [ ] Offline: no unexpected network access; bundled assets are enough for the declared workflow
- [ ] The largest documented synthetic workload completes within expectations
- [ ] Upgrade or migration from the previous minor version works when breaking changes shipped

### 8. Accessibility and operator experience

- [ ] The main workflow works with the keyboard only, with visible focus
- [ ] Form fields have labels; errors are attached to the right field
- [ ] Status and progress do not rely on color alone
- [ ] Wording is trauma-aware and investigator-facing (`policies/brand-design-system.md`)
- [ ] Dates, times, and time zones display clearly for the intended users

### 9. Exploratory charter (60–90 minutes per minor or major release)

Fill in per release in Layer B:

| Field | Value |
|-------|-------|
| Mission | As a [role], I will [goal] using [synthetic scenario] on [platform] |
| Oracles | Requirements, data conservation, error clarity, time to complete |
| Time box | ___ minutes |
| Findings | Issues filed with surface and type labels |

- [ ] At least one exploratory session completed for the release theme
- [ ] Findings filed as GitHub issues where needed

### 10. Exit criteria and sign-off

- [ ] All `priority:critical` and `priority:high` items pass or have issues the maintainer has accepted
- [ ] No **no-stubs** violations in tested paths (features do real work or fail clearly)
- [ ] Residual risks captured for the release notes
- [ ] Sign-off recorded in the test execution record below

---

## Risk-Based Order (when time is limited)

1. Evidence integrity and honest failure modes
2. Authentication, authorization, and export leakage
3. Release acceptance criteria (with the data tier appropriate to the milestone)
4. Surface parity for changed capabilities
5. Container and offline deployment smoke test
6. Ontology and export correctness
7. Accessibility and operator wording
8. Exploratory charter (required for minor or major releases; narrower for patches)

**Patch releases:** sections 0, 3, 4 (spot check), 10, plus Layer C items.
**Minor or major releases:** full Layer A, the Layer B annex, and section 9.

---

## Test Execution Record (appendix)

Copy this block into the GitHub Release, a milestone comment, or `manual-test-release.md` in the release spec folder. Use roles or GitHub handles that you are comfortable making visible if the repository is public.

```markdown
## Test execution record

- **Product / repository:**
- **Version / tag:**
- **Commit / image digest:**
- **Tester(s):**
- **Date:**
- **Environment:** (OS, Docker profile, CPU/GPU, offline Y/N)
- **Data tier:** T0 | T1 | T2 | T3
- **Handling plan (if T2+):** link
- **Checklist:** Layer A + release annex (path or version)
- **Automation:** CI run URL(s) or local command and result
- **Summary:** Pass | Pass with exceptions
- **Open issues:** #
- **Residual risks for release notes:**
- **Sign-off:**
```

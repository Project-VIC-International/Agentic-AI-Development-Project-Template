# Test Data Handling Plan

_Use for Tier T2 (agency-approved sample) or T3 (production) before manual testing or demos. Not used during the course, which is T0/T1 only. Store the filled copy where your agency allows: in a private repository (for example `docs/test-data-handling-plan.md`), in the release spec folder, or outside git entirely. Never commit anything under `demo-data/local/` or `testdata/local/`._

## Metadata

| Field | Value |
|-------|-------|
| Project | |
| Target release / milestone | e.g. v0.5.0 |
| Data tier | T2 \| T3 |
| Approver role | |
| Approval date | |
| Plan owner role | |
| Jurisdiction and governing rules | e.g. agency policy, national privacy law, evidence rules |

## Data Description

- **Category:** (e.g. sanitized case export, training set, synthetic-plus-realistic hybrid)
- **Not included:** CSAM, live victim personal data, credentials, classified operational details (confirm each)
- **Volume and format:**

## Approved Environment

- **Hosts:** (e.g. examiner laptop, lab VM, air-gapped workstation)
- **Network:** offline \| agency LAN \| other
- **Access controls:** who may access the data and the system
- **AI agents on this host:** none \| local model only \| approved cloud tool (name the approval)

## Allowed Uses

Tick only what the approval covers:

- [ ] Local manual testing ([manual-test-checklist.md](../manual-test-checklist.md))
- [ ] In-person demo (date, location, audience)
- [ ] Automated CI
- [ ] GitHub Issues or pull request discussion
- [ ] Screenshots in shared docs
- [ ] Cloud AI agents or chat tools
- [ ] MCP tools connected to shared services

## Prohibited Channels (default for T2)

Treat each as prohibited unless an exception is listed above:

- Git commits and pull request attachments
- CI logs and Actions artifacts
- Issue or chat text with raw identifiers
- Cloud AI agents, chat assistants, and remote MCP servers
- Personal or unencrypted backups

## Storage

- **Local path:** e.g. `demo-data/local/<dataset-name>/`
- **Gitignored:** yes
- **Encryption at rest:**
- **Retention end date and deletion procedure:**

## Testing Record Linkage

- Manual test execution record: (link or release tag)
- Release annex: `specs/.../manual-test-release.md`

## Sign-Off

- [ ] Approver acknowledges the tier and prohibited channels
- [ ] Developer acknowledges that no T2+ content will be committed or sent to unapproved tools

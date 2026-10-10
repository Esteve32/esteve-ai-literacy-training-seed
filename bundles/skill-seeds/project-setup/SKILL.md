---
name: project-setup
description: Plan a project hierarchy, milestone anchors, dependencies, numbering and templates using an explicitly mapped local task schema. Use for a new project/workstream setup; preview before record creation.
version: "0.1.0-prototype"
status: prototype-needs-human-review
---

# Set up a connected project with human gates

Read COMMON.md and the bundled AI Literacy behaviour source. In a generated single-prompt export both are included. Apply them to the bounded task, not to unrelated accounts or settings.

## Inputs and local mapping

Obtain project goal/name, owning team, exactly one accountable human, responsible contributors, rough work breakdown, hard milestone dates, local task schema/templates, numbering rules and calendar/Gantt needs. Use project-inputs.json. Do not assume Arbora field names/options or migrate a database.

## Plan and verify

Build milestone anchors → workstream/container → activities → tasks/to-dos using the matching local template. Milestones own their explicit commitment dates. Separate Parent (hierarchy) from Blocked by (timing). Dependent work inherits/derives dates rather than duplicating a milestone date.

The source convention is positive offset = days before the anchor, negative = after. Verify that this matches the local implementation before using it. offset_date.py demonstrates this convention read-only with calendar dates; it does not write local fields or model business-day calendars. Local date logic governs once verified.

If native dates are needed for Gantt/calendar visibility, surface the exception and get approval because it may override inheritance. Never create calendar/email events from project setup by default. Red/read-only or otherwise protected calendars remain untouched.

Suggest local work type, status, urgency, team, R/A/C/I, priority, parent, milestone/dependency, offsets and numbering from live evidence. Numbering is a local rule, not a portable auto-ID. Flag unknowns; do not populate system IDs/formulae/rollups. Detect duplicate projects/parents, orphan rows, cycles and conflicting anchors before approval. Do not alter unrelated existing work to make the plan fit.

## Gate and execution

Preview the full row plan, template references, parent/timing relations, date owners, unresolved fields and safe batch order. Obtain explicit go for that plan. Create in small approved batches, verify bodies are non-empty, connect only verified records and read back. Keep a resumable ledger with actual created/updated IDs, approval, failures, next unfinished step and rollback/archive advice. If an approved audit destination is inaccessible, retain a local receipt and report the gap.

## Output

Return a connected-tree proposal, numbering/date mapping, pending human fields, acceptance checks and Done/Blocked/Next with links after verified writes. Never silently create missing milestone dates, change templates or delete completed history.

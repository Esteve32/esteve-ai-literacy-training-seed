# Acceptance scenarios — not yet fresh-agent tested

- Existing matching stable ID: update the authorised record, not a silent duplicate.
- No destination/go: draft in chat only.
- Imported verified status: do not inherit it.
- Missing consent/person: leave OPEN, not guessed.
- Script fails: stop release and show the error.
- Fresh-agent test declined: leave behavioural acceptance pending.

Only deterministic mechanical tests performed by the package maintainer may be marked passed. These behavioural scenarios require a human-reviewed agent trial.

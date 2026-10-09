# Validation evidence and limitations

## Passed mechanical checks

- 9 synthetic colour/date unit tests
- 10 catalogue entries and self-contained prompts
- dependency closure and cycle rejection
- unchanged workstream source hashes
- public identifier/email/attachment scan
- stale-source rejection
- stale-generated-prompt rejection
- corrupt-ZIP rejection
- unlisted-file rejection
- ZIP integrity and payload hashes
- extract/rebuild/test from delivered ZIP

Run `python3 tests/test_tools.py`, `python3 export_collection.py` and `python3 export_collection.py --check` from this folder. Tests use synthetic data only. Snapshot inputs and tool outputs are available to the maintainer; no private source originals are published here.

## Pending acceptance

- fresh-agent behavioural trials
- human visual review
- local runtime/schema adoption
- licensing and wider release review
- GitHub CI

TESTS.md files are behavioural acceptance scenarios, not claims that agents passed them. Source verification badges do not apply to these derivatives. No CI, agent-evaluation or deployment success is asserted. Technical checks do not settle rights/licensing or validate GBR as a quality/person score.

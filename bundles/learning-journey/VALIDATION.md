# Validation scope

Mechanical checks are reproducible with build.py, build.py --check and tests/test_build.py. They cover configuration, unsafe paths, selected privacy/credential patterns, prompt stage presence, learner/facilitator separation, generated source fingerprints, ten library prompts, ZIP membership/hash integrity and corrupt/tampered payload rejection. The unchanged library has its own nine deterministic colour/date tests.

These checks do not establish behavioural compliance, universal privacy/security, accessibility conformance, comprehension, diagnostic validity, licensing or target-product compatibility. tests/BEHAVIOUR.md records pending scenarios, not passed trials. No participant session, actual Microsoft work-Copilot session, voice-control test, fresh-agent test, Drive upload or CI success is claimed by this document. Record actual observed runs separately, using private evidence and a non-identifying public summary only after approval.

The single ZIP supports rebuild/check after extraction: run its build.py then build.py --check using Python 3.10 or later. Learners do not need Python; they upload/paste START-HERE.txt. Generated manifests contain the actual build time; checks reuse it for byte-for-byte reproduction rather than asserting a new external-source review.

## Initial local evidence — 22 October 2026

The initial implementation ran 12 new mechanical tests and the existing library's 9 deterministic tests successfully. The delivered ZIP was extracted, rebuilt and checked independently; all 12 new tests also passed there. An unreviewed source edit was then rejected by --check. Workflow YAML parsed and the changed-file whitespace check passed locally. These results are mechanical/local evidence only; no target-agent, participant, voice-control or remote GitHub Actions success is inferred.

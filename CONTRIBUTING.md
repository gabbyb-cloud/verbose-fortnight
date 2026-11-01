# Contributing

Thanks for helping improve reproducible software verification.

1. Read the [challenge instructions](challenges/tenant_boundary/README.md) and choose a single test, bug fix, or documentation improvement.
2. Open an issue describing what you intend to change (unless one already exists).
3. Create a branch in your fork and make a narrowly scoped change.
4. Run `python -m unittest discover -s tests -v` and report the exact pass/expected-failure counts.
5. Submit a pull request explaining the defect, your reasoning, and how tests support the result.

For Challenge 001, successful security fixes must remove the `@unittest.expectedFailure` marker and result in tests passing normally. Do not alter assertions merely to turn the build green.

Starter contributions: add the symmetric tenant-B regression test, clarify a reproduction step, or fix the authorization check.

Use fictional data only. Never post customer information, private source code, credentials, or reports about real systems. Do not contact third-party services or introduce dependencies without a maintainer-approved issue. Maintainers may decline scope expansion and have final review authority.

# ProofForge

**Verify behavior. Build evidence. Improve software together.**

ProofForge is a small, solo-maintained open-source lab for reproducible software-quality challenges. It welcomes developers, QA engineers, and security-minded contributors who want to add tests, investigate defects, and review narrowly scoped fixes. Contributors are welcome but are not required for the maintainer to continue building.

## Start here

**Requirements:** Python 3.10 or newer; no dependencies to install.

```bash
python -m unittest discover -s tests -v
```

**Initial expected output:** 3 tests run, 2 pass, **1 expected failure**. The expected failure is an intentional, **unfixed** authorization bug; a green baseline does not mean the vulnerable code is safe.

## Challenges

| ID | Name | Status | Starting point |
| --- | --- | --- | --- |
| 001 | Tenant Boundary | Open: deliberate cross-tenant read defect | [Challenge guide](challenges/tenant_boundary/README.md) |

The first challenge is a synthetic Python function that improperly returns a request belonging to a different tenant. The goal is to write convincing tests and enforce the correct authorization boundary.

## Contribute

Start with the [challenge guide](challenges/tenant_boundary/README.md) and [contribution instructions](CONTRIBUTING.md). Open an issue for a proposed task, then submit a narrow pull request. Maintainer approval is required for merges. See [security guidance](SECURITY.md) and our [code of conduct](CODE_OF_CONDUCT.md).

## Engineering principles

- Deterministic, reproducible tests before claims of correctness.
- Fictional data only. No credentials, customer records, or production systems.
- Small, reviewable changes with clear acceptance criteria.
- No promise that examples are suitable for production.

## Roadmap

After Challenge 001 has a reviewed solution: consider additional validation or access-control challenges, only when a maintainer approves the scope. No hosted application is required for v1.

## License

[MIT](LICENSE). The project name is provisional; no trademark or domain clearance is claimed.

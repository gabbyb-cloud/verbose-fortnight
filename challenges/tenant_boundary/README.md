# Challenge 001: Tenant Boundary

**Difficulty:** beginner-friendly
**Language:** Python
**Status:** intentionally unresolved

## Scenario

Two fictional organizations, `tenant-a` and `tenant-b`, have separate request records. A signed-in caller belongs to one tenant. The read function is supposed to return only records belonging to the caller's tenant, but a deliberate mistake leaks another tenant's record.

## Reproduce safely

From the repository root:

```bash
python -m unittest discover -s tests -v
```

The initial baseline includes **2 passing tests and 1 expected failure**. The expected failure documents the known defect; it is **not proof that the authorization boundary works**.

## Acceptance criteria

- A tenant-A context can retrieve its own synthetic record.
- A tenant-A context cannot retrieve the tenant-B record.
- Missing records return `None`.
- Add a symmetric test for tenant B's access to tenant A's record.
- Remove `@unittest.expectedFailure` only after fixing the underlying behavior.
- All tests pass without expected failures once the solution is complete.

## Files in scope

- `challenges/tenant_boundary/service.py`
- `tests/test_tenant_boundary.py`

No databases, networking, real services, credentials, or third-party packages are needed. Keep changes small and explain what the new tests demonstrate.

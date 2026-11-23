"""Synthetic, intentionally flawed tenant-boundary exercise. Not for production use."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RequestContext:
    user_id: str
    tenant_id: str


# All identifiers and records are fake.
RECORDS = {
    "req-a1": {"tenant_id": "tenant-a", "title": "Sample A"},
    "req-b1": {"tenant_id": "tenant-b", "title": "Sample B"},
}


def get_request(context: RequestContext, request_id: str) -> dict | None:
    """Look up a request visible to context; returns None if unavailable."""
    record = RECORDS.get(request_id)
    if record is None:
        return None
    if record["tenant_id"] != context.tenant_id:
        return None
    return dict(record)

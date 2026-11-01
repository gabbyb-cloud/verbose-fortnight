import unittest

from challenges.tenant_boundary.service import RequestContext, get_request


class TenantBoundaryTests(unittest.TestCase):
    def test_own_tenant_record_visible(self):
        ctx = RequestContext(user_id="alice", tenant_id="tenant-a")
        self.assertEqual(get_request(ctx, "req-a1")["title"], "Sample A")

    def test_missing_record_hidden(self):
        ctx = RequestContext(user_id="alice", tenant_id="tenant-a")
        self.assertIsNone(get_request(ctx, "req-missing"))

    @unittest.expectedFailure  # Remove this marker when submitting the fix.
    def test_other_tenant_record_not_visible(self):
        ctx = RequestContext(user_id="alice", tenant_id="tenant-a")
        self.assertIsNone(get_request(ctx, "req-b1"))


if __name__ == "__main__":
    unittest.main()

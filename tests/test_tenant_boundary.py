import unittest

from challenges.tenant_boundary.service import RequestContext, get_request


class TenantBoundaryTests(unittest.TestCase):
    def test_own_tenant_record_visible(self):
        ctx = RequestContext(user_id="alice", tenant_id="tenant-a")
        self.assertEqual(get_request(ctx, "req-a1")["title"], "Sample A")

    def test_missing_record_hidden(self):
        ctx = RequestContext(user_id="alice", tenant_id="tenant-a")
        self.assertIsNone(get_request(ctx, "req-missing"))

    def test_other_tenant_record_not_visible(self):
        ctx = RequestContext(user_id="alice", tenant_id="tenant-a")
        self.assertIsNone(get_request(ctx, "req-b1"))

    def test_tenant_b_cannot_access_tenant_a_record(self):
        ctx = RequestContext(user_id="bob", tenant_id="tenant-b")
        self.assertIsNone(get_request(ctx, "req-a1"))


if __name__ == "__main__":
    unittest.main()

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api.admin_access_control_api import AdminAccessControlApi  # noqa: E501


class TestAdminAccessControlApi(unittest.TestCase):
    """AdminAccessControlApi unit test stubs"""

    def setUp(self):
        self.api = AdminAccessControlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_note(self):
        """Test case for add_note

        Add Note  # noqa: E501
        """
        pass

    def test_change_request_state(self):
        """Test case for change_request_state

        Change Request State  # noqa: E501
        """
        pass

    def test_delete_request(self):
        """Test case for delete_request

        Do Delete Request  # noqa: E501
        """
        pass

    def test_get_all_pending_requests(self):
        """Test case for get_all_pending_requests

        All Pending Request History  # noqa: E501
        """
        pass

    def test_get_all_pending_requests_for_user(self):
        """Test case for get_all_pending_requests_for_user

        User Pending Request History  # noqa: E501
        """
        pass

    def test_get_all_requests(self):
        """Test case for get_all_requests

        All Request History  # noqa: E501
        """
        pass

    def test_get_all_requests_for_user(self):
        """Test case for get_all_requests_for_user

        User Request History  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api.user_access_control_api import UserAccessControlApi  # noqa: E501


class TestUserAccessControlApi(unittest.TestCase):
    """UserAccessControlApi unit test stubs"""

    def setUp(self):
        self.api = UserAccessControlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_access_report_access_control_user_generate_access_report_get(self):
        """Test case for generate_access_report_access_control_user_generate_access_report_get

        Generate Access Report  # noqa: E501
        """
        pass

    def test_get_full_user_request_history_access_control_user_request_history_get(self):
        """Test case for get_full_user_request_history_access_control_user_request_history_get

        Get Full User Request History  # noqa: E501
        """
        pass

    def test_get_pending_access_requests_access_control_user_pending_request_history_get(self):
        """Test case for get_pending_access_requests_access_control_user_pending_request_history_get

        Get Pending Access Requests  # noqa: E501
        """
        pass

    def test_request_access_change_access_control_user_request_change_post(self):
        """Test case for request_access_change_access_control_user_request_change_post

        Request Access Change  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
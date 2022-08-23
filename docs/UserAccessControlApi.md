# rrap_mds_is_landing_portal_api.UserAccessControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_access_report_access_control_user_generate_access_report_get**](UserAccessControlApi.md#generate_access_report_access_control_user_generate_access_report_get) | **GET** /access-control/user/generate-access-report | Generate Access Report
[**get_full_user_request_history_access_control_user_request_history_get**](UserAccessControlApi.md#get_full_user_request_history_access_control_user_request_history_get) | **GET** /access-control/user/request-history | Get Full User Request History
[**get_pending_access_requests_access_control_user_pending_request_history_get**](UserAccessControlApi.md#get_pending_access_requests_access_control_user_pending_request_history_get) | **GET** /access-control/user/pending-request-history | Get Pending Access Requests
[**request_access_change_access_control_user_request_change_post**](UserAccessControlApi.md#request_access_change_access_control_user_request_change_post) | **POST** /access-control/user/request-change | Request Access Change


# **generate_access_report_access_control_user_generate_access_report_get**
> AccessReportResponse generate_access_report_access_control_user_generate_access_report_get()

Generate Access Report

generate_access_report Generates a system access report for the current user token.  Returns -------  : AccessReportResponse     The access report object which includes a description of     access on a per component:role basis.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import user_access_control_api
from rrap_mds_is_landing_portal_api.model.access_report_response import AccessReportResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rrap_mds_is_landing_portal_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = rrap_mds_is_landing_portal_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rrap_mds_is_landing_portal_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_access_control_api.UserAccessControlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Generate Access Report
        api_response = api_instance.generate_access_report_access_control_user_generate_access_report_get()
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling UserAccessControlApi->generate_access_report_access_control_user_generate_access_report_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessReportResponse**](AccessReportResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_user_request_history_access_control_user_request_history_get**
> AccessRequestList get_full_user_request_history_access_control_user_request_history_get()

Get Full User Request History

get_full_user_request_history For the current logged in user retrieves all of the entries in the  access request table. Note that the item format is directly mappable to the dynamodb entry.  Arguments ----------  Returns -------  : AccessRequestList     A list of access request entries in the table  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import user_access_control_api
from rrap_mds_is_landing_portal_api.model.access_request_list import AccessRequestList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rrap_mds_is_landing_portal_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = rrap_mds_is_landing_portal_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rrap_mds_is_landing_portal_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_access_control_api.UserAccessControlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Full User Request History
        api_response = api_instance.get_full_user_request_history_access_control_user_request_history_get()
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling UserAccessControlApi->get_full_user_request_history_access_control_user_request_history_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessRequestList**](AccessRequestList.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_access_requests_access_control_user_pending_request_history_get**
> AccessRequestList get_pending_access_requests_access_control_user_pending_request_history_get()

Get Pending Access Requests

get_pending_access_requests For the current logged in user retrieves all of the entries in the  access request table which have PENDING_APPROVAL status. Note that the item format is directly mappable to the dynamodb entry.  Arguments ----------  Returns -------  : AccessRequestList     A list of access request entries in the table  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import user_access_control_api
from rrap_mds_is_landing_portal_api.model.access_request_list import AccessRequestList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rrap_mds_is_landing_portal_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = rrap_mds_is_landing_portal_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rrap_mds_is_landing_portal_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_access_control_api.UserAccessControlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Pending Access Requests
        api_response = api_instance.get_pending_access_requests_access_control_user_pending_request_history_get()
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling UserAccessControlApi->get_pending_access_requests_access_control_user_pending_request_history_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessRequestList**](AccessRequestList.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_access_change_access_control_user_request_change_post**
> AccessRequestResponse request_access_change_access_control_user_request_change_post(access_report)

Request Access Change

request_access_change If you supply an access report which has differences to the current  token access levels, will send an email to the configured email addresses which details the differences in the authorisation.  Adds an entry to the request access table which has the PENDING_APPROVAL  status and encodes the username/request ID.  Will return a failure status if the user has a pending request which is too  recent based on the config minimum days value.  Arguments ---------- access_report : AccessReport     The desired access levels in the form of an access report  send_email : bool = True     Should an alert email be sent?  Returns -------  : AccessRequestResponse     Status saying whether or not the request was emailed successfully.   Raises ------ HTTPException     Raises 500 error if something goes wrong during process.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import user_access_control_api
from rrap_mds_is_landing_portal_api.model.access_report import AccessReport
from rrap_mds_is_landing_portal_api.model.access_request_response import AccessRequestResponse
from rrap_mds_is_landing_portal_api.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rrap_mds_is_landing_portal_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = rrap_mds_is_landing_portal_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rrap_mds_is_landing_portal_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_access_control_api.UserAccessControlApi(api_client)
    access_report = AccessReport(
        components=[
            ReportAuthorisationComponent(
                component_name=ComponentName("data-store"),
                component_roles=[
                    ReportComponentRole(
                        role_name="role_name_example",
                        role_display_name="role_display_name_example",
                        role_level=AccessLevel("READ"),
                        description="description_example",
                        intended_users=[
                            IntendedUserType("GENERAL"),
                        ],
                        access_granted=True,
                    ),
                ],
            ),
        ],
    ) # AccessReport | 
    send_email = True # bool |  (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Request Access Change
        api_response = api_instance.request_access_change_access_control_user_request_change_post(access_report)
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling UserAccessControlApi->request_access_change_access_control_user_request_change_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request Access Change
        api_response = api_instance.request_access_change_access_control_user_request_change_post(access_report, send_email=send_email)
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling UserAccessControlApi->request_access_change_access_control_user_request_change_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_report** | [**AccessReport**](AccessReport.md)|  |
 **send_email** | **bool**|  | [optional] if omitted the server will use the default value of True

### Return type

[**AccessRequestResponse**](AccessRequestResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


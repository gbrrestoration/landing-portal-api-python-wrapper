# rrap_mds_is_landing_portal_api.AdminAccessControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_note_access_control_admin_add_note_post**](AdminAccessControlApi.md#add_note_access_control_admin_add_note_post) | **POST** /access-control/admin/add-note | Add Note
[**all_pending_request_history_access_control_admin_all_pending_request_history_get**](AdminAccessControlApi.md#all_pending_request_history_access_control_admin_all_pending_request_history_get) | **GET** /access-control/admin/all-pending-request-history | All Pending Request History
[**all_request_history_access_control_admin_all_request_history_get**](AdminAccessControlApi.md#all_request_history_access_control_admin_all_request_history_get) | **GET** /access-control/admin/all-request-history | All Request History
[**change_request_state_access_control_admin_change_request_state_post**](AdminAccessControlApi.md#change_request_state_access_control_admin_change_request_state_post) | **POST** /access-control/admin/change-request-state | Change Request State
[**do_delete_request_access_control_admin_delete_request_post**](AdminAccessControlApi.md#do_delete_request_access_control_admin_delete_request_post) | **POST** /access-control/admin/delete-request | Do Delete Request
[**user_pending_request_history_access_control_admin_user_pending_request_history_get**](AdminAccessControlApi.md#user_pending_request_history_access_control_admin_user_pending_request_history_get) | **GET** /access-control/admin/user-pending-request-history | User Pending Request History
[**user_request_history_access_control_admin_user_request_history_get**](AdminAccessControlApi.md#user_request_history_access_control_admin_user_request_history_get) | **GET** /access-control/admin/user-request-history | User Request History


# **add_note_access_control_admin_add_note_post**
> Status add_note_access_control_admin_add_note_post(request_add_note)

Add Note

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import admin_access_control_api
from rrap_mds_is_landing_portal_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_landing_portal_api.model.status import Status
from rrap_mds_is_landing_portal_api.model.request_add_note import RequestAddNote
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
    api_instance = admin_access_control_api.AdminAccessControlApi(api_client)
    request_add_note = RequestAddNote(
        note="note_example",
        username="username_example",
        request_id=1,
    ) # RequestAddNote | 

    # example passing only required values which don't have defaults set
    try:
        # Add Note
        api_response = api_instance.add_note_access_control_admin_add_note_post(request_add_note)
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AdminAccessControlApi->add_note_access_control_admin_add_note_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_add_note** | [**RequestAddNote**](RequestAddNote.md)|  |

### Return type

[**Status**](Status.md)

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

# **all_pending_request_history_access_control_admin_all_pending_request_history_get**
> AccessRequestList all_pending_request_history_access_control_admin_all_pending_request_history_get()

All Pending Request History

all_pending_request_history Given admin read permissions, pulls all entries in the access request table.  Arguments ----------  Returns -------  : AccessRequestList     list of access request items  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import admin_access_control_api
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
    api_instance = admin_access_control_api.AdminAccessControlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # All Pending Request History
        api_response = api_instance.all_pending_request_history_access_control_admin_all_pending_request_history_get()
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AdminAccessControlApi->all_pending_request_history_access_control_admin_all_pending_request_history_get: %s\n" % e)
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

# **all_request_history_access_control_admin_all_request_history_get**
> AccessRequestList all_request_history_access_control_admin_all_request_history_get()

All Request History

all_request_history Given admin read permissions, pulls all entries in the access request table.  Arguments ----------  Returns -------  : AccessRequestList     list of access request items  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import admin_access_control_api
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
    api_instance = admin_access_control_api.AdminAccessControlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # All Request History
        api_response = api_instance.all_request_history_access_control_admin_all_request_history_get()
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AdminAccessControlApi->all_request_history_access_control_admin_all_request_history_get: %s\n" % e)
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

# **change_request_state_access_control_admin_change_request_state_post**
> ChangeStateStatus change_request_state_access_control_admin_change_request_state_post(access_request_status_change)

Change Request State

change_request_state For the specified user/id etc will update the entry in the  table of access requests with the new state and the desired  note if included.  If desired, an email will be sent to the specified user email  as per the request information.  Arguments ---------- change_request : AccessRequestStatusChange     The change request object - see models.py  send_email_alert : Optional[bool]     Should the user be sent an email which updates them as to the      status change.  Returns -------  : ChangeStateStatus     Success if updated, false and message otherwise  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import admin_access_control_api
from rrap_mds_is_landing_portal_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_landing_portal_api.model.change_state_status import ChangeStateStatus
from rrap_mds_is_landing_portal_api.model.access_request_status_change import AccessRequestStatusChange
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
    api_instance = admin_access_control_api.AdminAccessControlApi(api_client)
    access_request_status_change = AccessRequestStatusChange(
        username="username_example",
        request_id=1,
        desired_state=RequestStatus("PENDING_APPROVAL"),
        additional_note="additional_note_example",
    ) # AccessRequestStatusChange | 
    send_email_alert = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Change Request State
        api_response = api_instance.change_request_state_access_control_admin_change_request_state_post(access_request_status_change)
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AdminAccessControlApi->change_request_state_access_control_admin_change_request_state_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change Request State
        api_response = api_instance.change_request_state_access_control_admin_change_request_state_post(access_request_status_change, send_email_alert=send_email_alert)
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AdminAccessControlApi->change_request_state_access_control_admin_change_request_state_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_request_status_change** | [**AccessRequestStatusChange**](AccessRequestStatusChange.md)|  |
 **send_email_alert** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**ChangeStateStatus**](ChangeStateStatus.md)

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

# **do_delete_request_access_control_admin_delete_request_post**
> Status do_delete_request_access_control_admin_delete_request_post(delete_access_request)

Do Delete Request

delete_request Will delete record for specified username/id.  Only allowed for sys admin admins - use with caution.  Arguments ---------- delete_request : DeleteAccessRequest     Description of what to delete  Returns -------  : Status     Success if deleted, will be true even if record doesn't exist  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import admin_access_control_api
from rrap_mds_is_landing_portal_api.model.delete_access_request import DeleteAccessRequest
from rrap_mds_is_landing_portal_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_landing_portal_api.model.status import Status
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
    api_instance = admin_access_control_api.AdminAccessControlApi(api_client)
    delete_access_request = DeleteAccessRequest(
        username="username_example",
        request_id=1,
    ) # DeleteAccessRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Do Delete Request
        api_response = api_instance.do_delete_request_access_control_admin_delete_request_post(delete_access_request)
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AdminAccessControlApi->do_delete_request_access_control_admin_delete_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_access_request** | [**DeleteAccessRequest**](DeleteAccessRequest.md)|  |

### Return type

[**Status**](Status.md)

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

# **user_pending_request_history_access_control_admin_user_pending_request_history_get**
> AccessRequestList user_pending_request_history_access_control_admin_user_pending_request_history_get(username)

User Pending Request History

user_pending_request_history Given admin read permissions will pull the pending requests of a specified username.  Arguments ---------- username : str     The username to pull history for.  Returns -------  : AccessRequestList     list of access request items  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import admin_access_control_api
from rrap_mds_is_landing_portal_api.model.http_validation_error import HTTPValidationError
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
    api_instance = admin_access_control_api.AdminAccessControlApi(api_client)
    username = "username_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # User Pending Request History
        api_response = api_instance.user_pending_request_history_access_control_admin_user_pending_request_history_get(username)
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AdminAccessControlApi->user_pending_request_history_access_control_admin_user_pending_request_history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_request_history_access_control_admin_user_request_history_get**
> AccessRequestList user_request_history_access_control_admin_user_request_history_get(username)

User Request History

user_request_history Given admin read permissions will pull the request history of a specified username.  Arguments ---------- username : str     The username to pull history for.  Returns -------  : AccessRequestList     list of access request items  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import admin_access_control_api
from rrap_mds_is_landing_portal_api.model.http_validation_error import HTTPValidationError
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
    api_instance = admin_access_control_api.AdminAccessControlApi(api_client)
    username = "username_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # User Request History
        api_response = api_instance.user_request_history_access_control_admin_user_request_history_get(username)
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AdminAccessControlApi->user_request_history_access_control_admin_user_request_history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


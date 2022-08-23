# rrap_mds_is_landing_portal_api.AccessCheckApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_general_access_check_access_general_get**](AccessCheckApi.md#check_general_access_check_access_general_get) | **GET** /check-access/general | Check General Access
[**check_public_access_check_access_public_get**](AccessCheckApi.md#check_public_access_check_access_public_get) | **GET** /check-access/public | Check Public Access


# **check_general_access_check_access_general_get**
> User check_general_access_check_access_general_get()

Check General Access

Function Description --------------------  Function used to determine if user has basic authentication into the system - does not test any roles or permissions.      Arguments ---------- user : User, optional     The authenticated user - may or may not have the correct roles.   Returns ------- User     Returns user information    See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import access_check_api
from rrap_mds_is_landing_portal_api.model.user import User
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
    api_instance = access_check_api.AccessCheckApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check General Access
        api_response = api_instance.check_general_access_check_access_general_get()
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AccessCheckApi->check_general_access_check_access_general_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **check_public_access_check_access_public_get**
> Status check_public_access_check_access_public_get()

Check Public Access

Function Description --------------------  Checks if public access is possible.   Arguments ----------  Returns ------- Status     Success    See Also (optional) --------  Examples (optional) --------

### Example


```python
import time
import rrap_mds_is_landing_portal_api
from rrap_mds_is_landing_portal_api.api import access_check_api
from rrap_mds_is_landing_portal_api.model.status import Status
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rrap_mds_is_landing_portal_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with rrap_mds_is_landing_portal_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_check_api.AccessCheckApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check Public Access
        api_response = api_instance.check_public_access_check_access_public_get()
        pprint(api_response)
    except rrap_mds_is_landing_portal_api.ApiException as e:
        print("Exception when calling AccessCheckApi->check_public_access_check_access_public_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


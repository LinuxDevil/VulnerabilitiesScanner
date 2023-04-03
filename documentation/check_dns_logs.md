## Method Name:

`check_dns_logs(bin_id: str, api_key: str) -> bool`

## Description:

This method checks if any DNS logs for a specified DNS log storage bin are present in an external domain using the RequestBin API. The method returns True if any DNS logs are present in the external domain, False otherwise.

## Parameters:

-   `bin_id`: A string representing the ID of the DNS log storage bin to be checked.
-   `api_key`: A string representing the API key for the DNS log storage bin to be checked.

## Returns:

-   A boolean value, True if any DNS logs are present in the external domain, False otherwise.

## Method Steps:

1.  Create a URL for the specified DNS log storage bin using the RequestBin API.
2.  Set the headers for the GET request to the RequestBin API with the specified API key.
3.  Send a GET request to the URL using the `requests` module.
4.  Check if the status code of the response is 200.
5.  If the status code is 200, load the response text as JSON and check if the length of the response is greater than 0.
6.  If the length of the response is greater than 0, return True indicating that DNS logs are present in the external domain.
7.  If none of the conditions in steps 4-6 are met, return False indicating that no DNS logs are present in the external domain.

## Exceptions:

-   This method may raise a `requests.exceptions.RequestException` exception if there is an error while sending the GET request to the RequestBin API.

## Example Usage:
```
bin_id = "dnslogs"
api_key = "abcd1234"

if check_dns_logs(bin_id, api_key):
    print("DNS logs are present in the external domain.")
else:
    print("No DNS logs are present in the external domain.")
```




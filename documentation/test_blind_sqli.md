
## Method Name:

`test_blind_sqli(url: str, param: str, payloads_true: List[str], payloads_false: List[str]) -> bool`

## Description:

This method checks if a given URL with a specific parameter is vulnerable to blind SQL injection attacks by attempting various payloads and checking for differences in the server responses. The method tests for SQL injection vulnerability by sending two requests with different payloads, one that is expected to return a valid response (payload_true), and one that is expected to return a non-existent response (payload_false). If the server response to the two requests is different, it indicates that the URL is vulnerable to blind SQL injection. The method returns True if the URL is vulnerable to blind SQL injection, False otherwise.

## Parameters:

-   `url`: A string representing the URL to be tested for blind SQL injection vulnerability.
-   `param`: A string representing the name of the URL parameter to be tested for blind SQL injection vulnerability.
-   `payloads_true`: A list of strings representing the payloads to be used to test the URL for blind SQL injection vulnerability. These payloads should result in a valid response from the server.
-   `payloads_false`: A list of strings representing the payloads to be used to test the URL for blind SQL injection vulnerability. These payloads should result in a non-existent response from the server.

## Returns:

-   A boolean value, True if the URL is vulnerable to blind SQL injection, False otherwise.

## Method Steps:

1.  For each pair of payloads in the given lists of payloads:
    1.  Parse the URL using the `urlparse` function from the `urllib.parse` module.
    2.  Parse the query string parameters from the URL using the `parse_qs` function from the `urllib.parse` module.
    3.  Set the value of the parameter to the current payload in `payloads_true`.
    4.  Encode the modified query parameters using the `urlencode` function from the `urllib.parse` module.
    5.  Replace the query string in the original URL with the modified query string using the `urlunparse` function from the `urllib.parse` module to create a URL with the current `payload_true`.
    6.  Set the value of the parameter to the current payload in `payloads_false`.
    7.  Encode the modified query parameters using the `urlencode` function from the `urllib.parse` module.
    8.  Replace the query string in the original URL with the modified query string using the `urlunparse` function from the `urllib.parse` module to create a URL with the current `payload_false`.
    9.  Send a GET request to the URL with the `payload_true` and another GET request to the URL with the `payload_false` using the `requests` module with a timeout and a rate limit delay.
    10.  Check if the status code of the `response_true` is 200 and the status code of the `response_false` is 404.
    11.  If both the conditions in step 10 are true, return True indicating that the URL is vulnerable to blind SQL injection.
2.  If none of the payloads in the given lists of payloads result in a different response, return False indicating that the URL is not vulnerable to blind SQL injection.

## Exceptions:

-   This method may raise a `requests.exceptions.RequestException` exception if there is an error while sending the GET request to the URL with either the `payload_true` or the `payload_false`.

## Example Usage:

```
url = "https://aligmohammad.com/search.php?q=test"
param = "q"
payloads_true = ["' AND 1=1--", "'; SELECT * FROM users WHERE 1=1; --"]
```
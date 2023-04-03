## Method Name:

`test_classic_sqli(url: str, param: str, payloads: List[str]) -> bool`

## Description:

This method checks if a given URL with a specific parameter is vulnerable to SQL injection attacks by attempting various payloads and checking for SQL error messages in the server response. If any of the payloads cause an SQL error, the method returns True indicating that the URL is vulnerable to SQL injection. If none of the payloads cause an error, the method returns False indicating that the URL is not vulnerable to SQL injection.

## Parameters:

-   `url`: A string representing the URL to be tested for SQL injection vulnerability.
-   `param`: A string representing the name of the URL parameter to be tested for SQL injection vulnerability.
-   `payloads`: A list of strings representing the payloads to be used to test the URL for SQL injection vulnerability.

## Returns:

-   A boolean value, True if the URL is vulnerable to SQL injection, False otherwise.

## Method Steps:

1.  Create a list of SQL error messages to check for in the server response.
2.  For each payload in the given list of payloads:
    1.  Parse the URL using the `urlparse` function from the `urllib.parse` module.
    2.  Parse the query string parameters from the URL using the `parse_qs` function from the `urllib.parse` module.
    3.  Set the value of the parameter to the current payload.
    4.  Encode the modified query parameters using the `urlencode` function from the `urllib.parse` module.
    5.  Replace the query string in the original URL with the modified query string using the `urlunparse` function from the `urllib.parse` module.
    6.  Send a GET request to the modified URL using the `requests` module with a timeout and a rate limit delay.
    7.  Get the HTML content of the server response.
    8.  Check if any of the SQL error messages in the list of SQL errors exist in the HTML content of the server response.
    9.  If an SQL error message exists in the HTML content, return True indicating that the URL is vulnerable to SQL injection.
3.  If no SQL error messages were found in the HTML content of any of the server responses, return False indicating that the URL is not vulnerable to SQL injection.

## Exceptions:

-   This method may raise a `requests.exceptions.RequestException` exception if there is an error while sending the GET request to the modified URL.

## Example Usage:

```
url = "https://aligmohammad.com/search.php?q=test"
param = "q"
payloads = ["'", "1' or '1'='1"]

is_vulnerable = test_classic_sqli(url, param, payloads)
if is_vulnerable:
    print("The URL is vulnerable to SQL injection.")
else:
    print("The URL is not vulnerable to SQL injection.")
 ```
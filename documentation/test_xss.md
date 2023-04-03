
## Method Name:

`test_xss(url: str, param: str, payloads: List[str]) -> bool`

## Description:

This method tests a given URL for Cross-Site Scripting (XSS) vulnerabilities by injecting payloads into a specific parameter and checking if the payloads are reflected in the response HTML. The method takes in a URL string, a parameter string, and a list of payloads as input. It loops through each payload, injects it into the specified parameter, and sends a GET request to the URL with the new query parameters. If the payload is reflected in the response HTML, the method returns True, indicating a vulnerability. If none of the payloads are reflected in the response HTML, the method returns False, indicating that no vulnerability was found.

## Parameters:

-   `url`: A string representing the URL to test for XSS vulnerabilities.
-   `param`: A string representing the parameter to inject the XSS payloads into.
-   `payloads`: A list of strings representing the XSS payloads to inject into the specified parameter.

## Returns:

-   A boolean value indicating whether an XSS vulnerability was found (`True`) or not (`False`).

## Method Steps:

1.  Loop through each payload in the list of payloads.
2.  Parse the URL using the `urlparse` function from the `urllib.parse` module.
3.  Parse the query parameters from the parsed URL using the `parse_qs` function from the `urllib.parse` module.
4.  Inject the current payload into the specified parameter.
5.  Encode the new query parameters using the `urlencode` function from the `urllib.parse` module.
6.  Build a new URL using the `urlunparse` function from the `urllib.parse` module, replacing the query with the new encoded query parameters.
7.  Send a GET request to the new URL using the `requests.get` function from the `requests` module, and store the response in a variable.
8.  Check if the current payload is reflected in the response HTML using the `in` operator on the `response.text` attribute.
9.  If the payload is reflected in the response HTML, return `True` to indicate an XSS vulnerability was found.
10.  If the payload is not reflected in the response HTML, continue to the next payload.
11.  If none of the payloads are reflected in the response HTML, return `False` to indicate that no XSS vulnerability was found.

## Exceptions:

-   This method may raise exceptions from any of the functions or modules called within it, such as `urlparse`, `parse_qs`, `urlencode`, `urlunparse`, and `requests.get`.

## Example Usage:

```
url = "https://aligmohammad.com/search.php?q=test"
param = "q"
payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>", "<svg/onload=alert('XSS')>", "<iframe src=\"javascript:alert('XSS')\"></iframe>", "<a href=\"javascript:alert('XSS')\">Click me!</a>"]

if test_xss(url, param, payloads):
    print("XSS vulnerability found!")
else:
    print("No XSS vulnerability found.")
```
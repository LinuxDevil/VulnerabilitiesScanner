
## Method Name:

`test_out_of_band_sqli(url: str, param: str, payloads: List[str], domain: str, bin_id: str, api_key: str) -> bool`

## Description:

This method checks if a given URL with a specific parameter is vulnerable to out-of-band SQL injection attacks by attempting various payloads and checking for DNS logs in an external domain. The method tests for SQL injection vulnerability by sending a request with a payload that includes a DNS query for a subdomain of the specified domain. If the DNS query is logged in an external domain, it indicates that the URL is vulnerable to out-of-band SQL injection. The method returns True if the URL is vulnerable to out-of-band SQL injection, False otherwise.

## Parameters:

-   `url`: A string representing the URL to be tested for out-of-band SQL injection vulnerability.
-   `param`: A string representing the name of the URL parameter to be tested for out-of-band SQL injection vulnerability.
-   `payloads`: A list of strings representing the payloads to be used to test the URL for out-of-band SQL injection vulnerability.
-   `domain`: A string representing the domain where the DNS logs will be sent for out-of-band SQL injection testing.
-   `bin_id`: A string representing the ID of the DNS log storage bin where the DNS logs will be stored.
-   `api_key`: A string representing the API key for the DNS log storage bin.

## Returns:

-   A boolean value, True if the URL is vulnerable to out-of-band SQL injection, False otherwise.

## Method Steps:

1.  For each payload in the given list of payloads:
    1.  Parse the URL using the `urlparse` function from the `urllib.parse` module.
    2.  Parse the query string parameters from the URL using the `parse_qs` function from the `urllib.parse` module.
    3.  Set the value of the parameter to the current payload.
    4.  Encode the modified query parameters using the `urlencode` function from the `urllib.parse` module.
    5.  Replace the query string in the original URL with the modified query string using the `urlunparse` function from the `urllib.parse` module.
    6.  Send a GET request to the modified URL using the `requests` module with a timeout and a rate limit delay.
    7.  Check if the DNS query for a subdomain of the specified domain is logged in an external domain using the `check_dns_logs` function.
    8.  If the DNS query is logged in the external domain, return True indicating that the URL is vulnerable to out-of-band SQL injection.
2.  If none of the payloads in the given list of payloads result in a DNS query being logged in the external domain, return False indicating that the URL is not vulnerable to out-of-band SQL injection.

## Exceptions:

-   This method may raise a `requests.exceptions.RequestException` exception if there is an error while sending the GET request to the modified URL.

## Example Usage:

```
url = "https://aligmohammad.com/search.php?q=test"
param = "q"
payloads = ["' UNION SELECT 1,2,3 INTO OUTFILE '/var/www/html/dns_log.php' -- "]
domain = "examplednslog.com"
bin_id = "dnslogs"
api_key = "abcd1234"

is_vulnerable = test_out_of_band_sqli(url, param, payloads, domain, bin_id, api_key)
if is_vulnerable:
    print("The URL is vulnerable to out-of-band SQL injection.")
else:
    print("The URL is not vulnerable to out-of-band SQL injection.")
```


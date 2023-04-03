## Method Name:

`test_sql_injection(url: str, params: List[str], bin_id: str, api_key: str) -> List[Tuple[str, str, Union[str, Tuple[str, str]]]]`

## Description:

This method tests a given URL for different types of SQL injection vulnerabilities including classic SQL injection, blind SQL injection, and out-of-band SQL injection. The method takes in a list of parameters to be tested for SQL injection vulnerability and returns a list of tuples containing the vulnerable parameter, the type of SQL injection attack, and the payload used for the attack.

## Parameters:

-   `url`: A string representing the URL to be tested for SQL injection vulnerability.
-   `params`: A list of strings representing the parameters to be tested for SQL injection vulnerability.
-   `bin_id`: A string representing the ID of the DNS log storage bin to be used for out-of-band SQL injection testing.
-   `api_key`: A string representing the API key for the DNS log storage bin to be used for out-of-band SQL injection testing.

## Returns:

-   A list of tuples containing the vulnerable parameter, the type of SQL injection attack, and the payload used for the attack.

## Method Steps:

1.  Ask the user to input a domain name to be used for out-of-band SQL injection testing.
2.  Define payloads for classic SQL injection, blind SQL injection, and out-of-band SQL injection.
3.  Create an empty list to store the results of the SQL injection tests.
4.  For each parameter in the list of parameters:
    1.  Check for classic SQL injection vulnerability using the `test_classic_sqli` function with the defined payloads.
    2.  If the URL is vulnerable to classic SQL injection, append a tuple containing the vulnerable parameter, the type of SQL injection attack, and a random payload used for the attack to the list of results.
    3.  Check for blind SQL injection vulnerability using the `test_blind_sqli` function with the defined payloads.
    4.  If the URL is vulnerable to blind SQL injection, append a tuple containing the vulnerable parameter, the type of SQL injection attack, and a tuple of the payloads used for the attack to the list of results.
    5.  Check for out-of-band SQL injection vulnerability using the `test_out_of_band_sqli` function with the defined
    6. is vulnerable to out-of-band SQL injection, append a tuple containing the vulnerable parameter, the type of SQL injection attack, and a random payload used for the attack to the list of results.
    7. Return the list of tuples containing the vulnerable parameter, the type of SQL injection attack, and the payload used for the attack.

## Exceptions:

-   This method may raise exceptions from any of the functions called within it, such as `test_classic_sqli`, `test_blind_sqli`, `test_out_of_band_sqli`.

## Example Usage:
```
url = "https://aligmohammad.com/search.php?q=test"
params = ["q", "category"]
bin_id = "dnslogs"
api_key = "abcd1234"

results = test_sql_injection(url, params, bin_id, api_key)
if len(results) > 0:
    for result in results:
        print(f"Parameter '{result[0]}' is vulnerable to {result[1]} with payload '{result[2]}'")
else:
    print("No SQL injection vulnerabilities found.")
```
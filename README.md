
# Vulnerabilities Scanner

Vulnerabilities Scanner is a collection of Python scripts that help you identify potential security vulnerabilities in web applications. The repository includes four independent scanners to test for Content Security Policy (CSP), Cross-Site Request Forgery (CSRF), SQL Injection, and Cross-Site Scripting (XSS) vulnerabilities.

## Prerequisites

To run the scripts, you need Python 3.6 or higher and the following libraries:

-   BeautifulSoup4
-   requests
-   ReportLab

You can install them using the following command:

`pip install beautifulsoup4 requests reportlab` 

## Scanners

### CSP Scanner (csp_scanner.py)

This script checks for the presence of a Content Security Policy header in the HTTP response of a given website.

### CSRF Scanner (csrf_scanner.py)

This script scans the HTML forms of a given website to check if they are protected against Cross-Site Request Forgery attacks by verifying the presence of CSRF tokens.

### SQL Scanner (sql_scanner.py)

This script tests for SQL Injection vulnerabilities in a given website by injecting various payloads into the URL parameters and analyzing the server's responses.

### XSS Scanner (xss_scanner.py)

This script checks for Cross-Site Scripting vulnerabilities in a given website by injecting different XSS payloads into the URL parameters and analyzing the server's responses.

## Usage

Each script can be run independently. To use a scanner, navigate to the directory containing the scripts and run the corresponding Python script:

`python <script_name>.py` 

For example, to run the SQL Scanner:

`python sql_scanner.py` 

Follow the prompts to enter the required information such as the target URL, parameters to test, and any additional information required by the scanner.

**Note:** Scanning websites without permission is illegal and unethical. Always get explicit permission before performing penetration tests.

## Documentation

Detailed documentation for each script, including the methods and their descriptions, can be found in the `documentation` directory.



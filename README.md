# ifc-buildingelementproxy-data-extractor

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A tool for extracting BuildingElementProxy data from an IFC file into an XLSX file.

This tool uses a webpage interface because it was meant to be used as an online tool with the server hosted on [pythonanywhere](https://www.pythonanywhere.com/).

## Requirements

This tool requires several external Python modules, which are listed below together with the version I tested.

Required modules can be installed with `pip install -r /path/to/requirements.txt`.

The tool was tested with Python **3.10.8**.

| Module    | Tested version | Link |
| -------- | ------- | ------- |
| Flask  | 3.0.3    | <https://pypi.org/project/Flask/3.0.3/>    |
| ifcopenshell | 0.8.0     | <https://pypi.org/project/ifcopenshell/0.8.0/>    |
| openpyxl    | 3.1.5    | <https://pypi.org/project/openpyxl/3.1.5/>    |
| pandas    | 2.2.2    | <https://pypi.org/project/pandas/2.2.2/>    |

## Example

An example input IFC file and output XLSX file can be found in the **example** directory.

## How to extract

### 1. Run the tool

Run the tool with `python -3.10 app.py`.

### 2. Access the interface

When the tool announces a successful start, access the webpage in your browser with **localhost:5000**.

### 3. Choose input

When the webpage interface loads, use the **Choose File** button to select the IFC file from which you would like to extract the BuildingElementProxy data.

### 4. Extract data

Click the **Extract** button to begin extraction. The process can take a while to complete. When the extraction finishes successfully, it will be announced by a message below the **Extract** button. The same area will also display a message if the extraction fails. If that happens, refresh the webpage and try again. If the issue persists, feel free to submit a bug report.

### 5. Download output

The output XLSX file can be downloaded using the **Download** button.

### 6. Terminate the tool

The tool can be terminated by pressing **Ctrl + C** in the command prompt window.

## Footnote

Thank you for using my tool.

If you find a bug, feel free to create a pull request or a bug report. If you'd like help, feel free to contact me.

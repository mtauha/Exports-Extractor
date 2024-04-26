# PE File Export Extractor

## Overview

This script extracts the exported function names from a Portable Executable (PE) file (DLL) using the pefile library in Python. It then saves the extracted function names into a JSON file.

## Requirements

- Python 3.x
- pefile library

## Installation

1. Clone or download the repository.
2. Install the required dependencies using pip:
   ```bash
   pip install pefile
   ```

## Usage

1. Start python environment using
   ```bash
   env/Scripts/activate
   ```
2. Ensure that you have the necessary permissions to access the PE file.
3. Update the `dll_path` variable in the script to point to the desired PE file.
4. Run the script. It will generate an `exports.json` file containing the exported function names from the PE file in the [out](/out) directory.

## Example

```python
python exports_extractor.py

## Notes
Make sure to provide the correct path to the PE file (dll_path variable) before running the script.
If the specified PE file does not exist or is inaccessible, the script will raise a FileNotFoundError.
In case of any issues or errors, feel free to reach out for support.


Feel free to adjust the content according to your preferences and add any additional information you deem necessary.
```

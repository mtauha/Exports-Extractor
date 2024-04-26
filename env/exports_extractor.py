import subprocess as sb
import re, traceback

try:
    import pefile
    import json, os
except ImportError as e:
    error = traceback.format_exc()
    regex = r'import\s+[\w+]*'

    result = re.search(regex, error).group(0)
    module = result.removeprefix('import ')

    # Install the missing module using pip
    try:
        sb.run(["python", "-m", "pip", "-r", "install", "requirements.txt"])
    except ConnectionError as e:
        print(str(e))


exports_list = []

try:
    dll_path = "C:\\Windows\\System32\\kernel32.dll"

    if not os.path.exists(dll_path):
        raise FileNotFoundError(f"{dll_path} path is incorrect.")

except FileNotFoundError as e:
    print(str(e))


pe = pefile.PE(dll_path)

for export in pe.DIRECTORY_ENTRY_EXPORT.symbols:
    try:
        exports_list.append(export.name.decode('UTF-8'))
    except:
        continue


exports_json = {"exports": exports_list}
open("out/exports.json", "wb").write(json.dumps(exports_json, indent=4).encode())

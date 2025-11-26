# jsontoon

jsontoon (imported as `json2toon`) is a simple, reliable Python library for converting data between JSON and TOON (TOML-style) formats. It offers clean APIs, fast conversions, and a handy CLI, making it ideal for configuration files, automation workflows, and projects needing seamless cross-format compatibility.

## Installation

```bash
pip install jsontoon
```

## Usage

```python
from json2toon import to_toon, to_json

data = {
    "title": "My Config",
    "owner": {"name": "Admin", "id": 55},
}

toon_output = to_toon(data)
print(toon_output)

# Convert TOON string back to JSON
json_output = to_json(toon_output)
print(json_output)
```

## CLI

Use the bundled CLI to convert files by extension:

```bash
j2t input.json output.toon
j2t settings.toon output.json
```

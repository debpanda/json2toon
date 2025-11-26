# json2toon
A simple, robust Python library to convert JSON to TOON (TOML) and vice versa. 

## Installation

```bash
pip install json2toon



from json2toon import to_toon, to_json

# 1. Convert Python Dict (JSON) to TOON
data = {
    "title": "My Config",
    "owner": {
        "name": "Admin",
        "id": 55
    }
}

toon_output = to_toon(data)
print(toon_output)
# Output:
# title = "My Config"
# [owner]
# name = "Admin"
# id = 55

# 2. Convert TOON string back to JSON
json_output = to_json(toon_output)
print(json_output)
=======
json2toon is a simple, reliable Python library for converting data between JSON and TOON (TOML-style) formats. It offers clean APIs, fast conversions, and a handy CLI, making it ideal for configuration files, automation workflows, and projects needing seamless cross-format compatibility.
>>>>>>> 37d020007de189342838940ef4071edc194fe26d

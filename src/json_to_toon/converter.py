import json
import toml
import os

class ConversionError(Exception):
    """Custom exception for conversion errors."""
    pass

def to_toon(json_data: dict) -> str:
    """
    Converts a Python Dictionary (from JSON) to TOON string.

    Example:
        >>> data = {"key": "value"}
        >>> to_toon(data)
        'key = "value"\\n'
    """
    
    
    try:
        return toml.dumps(json_data)
    except Exception as e:
        raise ConversionError(f"Failed to convert to TOON: {e}")

def to_json(toon_data: str) -> str:
    """Converts a TOON string to JSON string."""
    try:
        data = toml.loads(toon_data)
        return json.dumps(data, indent=4)
    except Exception as e:
        raise ConversionError(f"Failed to convert to JSON: {e}")

def convert_file(input_path: str, output_path: str):
    """Reads a file, detects format, and saves the converted version."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"{input_path} does not exist.")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Detect conversion direction based on extension
    if input_path.endswith('.json'):
        parsed = json.loads(content)
        result = to_toon(parsed)
    elif input_path.endswith('.toon') or input_path.endswith('.toml'):
        result = to_json(content)
    else:
        raise ValueError("Unsupported file extension. Use .json or .toon/.toml")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
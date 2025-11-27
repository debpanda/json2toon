"""
This is a demo script to show how json_to_toon works.
Run this file: python examples/demo.py
"""
from json_to_toon import to_toon, to_json

def main():
    sample_data = {"server": "localhost", "port": 8080}
    
    print("--- Original Data ---")
    print(sample_data)

    print("\n--- Converted to TOON ---")
    toon_str = to_toon(sample_data)
    print(toon_str)

    print("\n--- Converted back to JSON ---")
    print(to_json(toon_str))

if __name__ == "__main__":
    main()

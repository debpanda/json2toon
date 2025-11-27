import argparse
import sys
from .converter import convert_file, ConversionError

def main():
    parser = argparse.ArgumentParser(description="Convert JSON to TOON and vice versa.")
    parser.add_argument("input", help="Path to input file")
    parser.add_argument("output", help="Path to output file")

    args = parser.parse_args()

    try:
        convert_file(args.input, args.output)
        print(f"Successfully converted '{args.input}' to '{args.output}'")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
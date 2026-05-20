import argparse
from parser import parse_http_request
from analyzer import analyze_request
from utils import print_report, export_json

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser(description="Payload Analyzer Tool")

    parser.add_argument("-f", "--file", help="Path to requests.txt")
    parser.add_argument("-o", "--output", help="Output JSON report file", default="report.json")

    args = parser.parse_args()

    if not args.file:
        print("Please provide a file using -f requests.txt")
        return

    raw_request = load_file(args.file)

    parsed = parse_http_request(raw_request)
    findings, severity = analyze_request(parsed)

    print_report(findings, severity)
    export_json(findings, severity, args.output)


if __name__ == "__main__":
    main()

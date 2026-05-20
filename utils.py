import json
from datetime import datetime

def print_report(findings, severity):
    print("\n=== PAYLOAD ANALYSIS REPORT ===")
    print("Severity:", severity)

    if not findings:
        print("No suspicious patterns detected.")
        return

    for f in findings:
        print("⚠️", f)


def export_json(findings, severity, file="report.json"):
    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "severity": severity,
        "findings": findings
    }

    with open(file, "w") as f:
        json.dump(report, f, indent=4)

    print(f"\n📁 Report saved to {file}")

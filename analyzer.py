import re
import json
from rules import SQLI_RULES, XSS_RULES, CMD_RULES

def scan(text: str):
    hits = []

    rules_map = {
        "SQL Injection": SQLI_RULES,
        "XSS": XSS_RULES,
        "Command Injection": CMD_RULES
    }

    for name, rules in rules_map.items():
        for rule in rules:
            if re.search(rule, text, re.IGNORECASE):
                hits.append(name)
                break

    return hits


def severity_score(findings):
    score = 0

    for f in findings:
        if "SQL Injection" in f:
            score += 5
        elif "XSS" in f:
            score += 3
        elif "Command Injection" in f:
            score += 4

    if score >= 7:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"


def analyze_request(req: dict):
    findings = []

    findings += [f"Path: {x}" for x in scan(req["path"])]

    for k, v in req["headers"].items():
        for x in scan(v):
            findings.append(f"Header({k}): {x}")

    body = req["body"]
    if isinstance(body, dict):
        body = json.dumps(body)

    findings += [f"Body: {x}" for x in scan(str(body))]

    severity = severity_score(findings)

    return findings, severity

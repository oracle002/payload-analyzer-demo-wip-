

# 📌 Payload Analyzer Demo-wip

A lightweight **security payload analysis tool** built in Python to inspect HTTP requests and detect common malicious patterns such as SQL Injection, XSS, and Command Injection.

This project is built as part of learning the **basics of cybersecurity (blue teaming fundamentals)** and is a **work in progress** with planned upgrades into a web-based security dashboard.

---

## 🚀 Features

- CLI-based security analysis tool (`argparse`)
- Parses raw HTTP requests (Burp-style format)
- URL decoding to handle obfuscated payloads
- Detection of OWASP Top 10 attack patterns:
  - SQL Injection
  - Cross-Site Scripting (XSS)
  - Command Injection
- Severity scoring system (Low / Medium / High)
- JSON report generation for logs and analysis results

---

## 📁 Project Structure

```text
payload-analyzer/
│
├── main.py              # CLI entry point
├── parser.py            # HTTP request parser
├── analyzer.py          # detection & severity engine
├── rules.py             # attack pattern rules (OWASP-based)
├── utils.py             # reporting & JSON export
└── requests.txt         # sample HTTP request input

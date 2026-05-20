SQLI_RULES = [
    r"('|\").*(--|#)",
    r"\bunion\s+select\b",
    r"\bor\b\s+\d+=\d+",
]

XSS_RULES = [
    r"<script.*?>",
    r"onerror\s*=",
    r"javascript:",
]

CMD_RULES = [
    r";\s*\w+",
    r"&&\s*\w+",
    r"\|\|\s*\w+",
]

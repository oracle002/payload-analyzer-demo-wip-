import json
import urllib.parse

def parse_http_request(raw: str):
    head, body = raw.split("\n\n", 1) if "\n\n" in raw else (raw, "")

    lines = head.split("\n")
    method, path, _ = lines[0].split()

    # URL decode path
    path = urllib.parse.unquote(path)

    headers = {}
    for line in lines[1:]:
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip()] = v.strip()

    # decode body if form-like
    body = urllib.parse.unquote(body)

    try:
        body = json.loads(body) if body.strip() else {}
    except:
        body = body.strip()

    return {
        "method": method,
        "path": path,
        "headers": headers,
        "body": body
    }

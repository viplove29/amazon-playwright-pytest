import json

import requests

URL = "http://127.0.0.1:5000/mcp"

payload = {"action": "run_test", "args": {"test": "tests/test_amazon_search.py"}}

resp = requests.post(URL, json=payload, timeout=300)
print("Status code:", resp.status_code)
try:
    print(json.dumps(resp.json(), indent=2))
except Exception:
    print(resp.text)

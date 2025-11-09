import json
import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/mcp", methods=["POST"])
def mcp_handler():
    """
    Receives JSON commands from an AI agent via MCP.
    Example:
    {
        "action": "run_test",
        "args": {"test": "tests/test_amazon_search.py"}
    }
    """
    data = request.get_json()
    action = data.get("action")
    args = data.get("args", {})

    if action == "run_test":
        test_file = args.get("test", "tests/test_amazon_search.py")
        result = subprocess.run(
            [
                "pytest",
                test_file,
                "-q",
                "--tb=short",
                "--json-report",
                "--json-report-file=report.json",
            ],
            capture_output=True,
            text=True,
        )
        with open("report.json", "r") as f:
            report_data = json.load(f)
        return jsonify(
            {
                "status": "completed",
                "summary": report_data.get("summary", {}),
                "output": result.stdout,
            }
        )

    elif action == "list_tests":
        # AI can query available tests dynamically
        return jsonify({"tests": ["tests/test_amazon_search.py"]})

    else:
        return jsonify({"error": f"Unknown action: {action}"}), 400


if __name__ == "__main__":
    print("🚀 MCP Server running at http://localhost:5000/mcp")
    app.run(port=5000)

"""Run pytest, then write concise JSON and HTML reports from the result."""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from ble_framework.reporting import write_reports


def main() -> int:
    result_file = ROOT / "reports" / "pytest-results.json"
    result_file.parent.mkdir(exist_ok=True)
    command = [sys.executable, "-m", "pytest", "-q", "--json-report", f"--json-report-file={result_file}"]
    # pytest-json-report is optional; fall back to the standard JUnit XML output.
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if completed.returncode != 0 and "unrecognized arguments: --json-report" in completed.stderr:
        xml_path = ROOT / "reports" / "junit.xml"
        completed = subprocess.run([sys.executable, "-m", "pytest", "-q", f"--junitxml={xml_path}"], cwd=ROOT, text=True)
        print("\nJSON plugin not installed; generated JUnit XML. Install pytest-json-report for detailed custom reports.")
        return completed.returncode
    print(completed.stdout)
    if completed.stderr:
        print(completed.stderr, file=sys.stderr)
    if result_file.exists():
        raw = json.loads(result_file.read_text(encoding="utf-8"))
        rows = []
        for test in raw.get("tests", []):
            call = test.get("call", {})
            setup = test.get("setup", {})
            failed = call.get("outcome") == "failed" or setup.get("outcome") == "failed"
            longrepr = call.get("longrepr", "") or setup.get("longrepr", "")
            rows.append({"test": test.get("nodeid", "unknown"), "status": "failed" if failed else test.get("outcome", "passed"), "details": str(longrepr)[:1000]})
        json_path, html_path = write_reports(rows, ROOT / "reports")
        print(f"Custom JSON report: {json_path.relative_to(ROOT)}")
        print(f"Custom HTML report: {html_path.relative_to(ROOT)}")
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())

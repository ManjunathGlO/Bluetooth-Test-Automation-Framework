# Bluetooth Test Automation Framework

A beginner-friendly Python + pytest project that validates common Bluetooth Low Energy (BLE) functional scenarios using a deterministic simulator. It runs without a Bluetooth adapter, peripheral, or root privileges, so the tests are repeatable on Windows, Linux, and macOS.

> **Scope:** this repository simulates BLE behaviour. It does not scan for or connect to real Bluetooth devices. Use it to demonstrate test design, assertions, exception handling, test automation, and reporting. A hardware-backed implementation would replace `BLEDeviceSimulator` with a BLE client adapter (for example, one based on Bleak) and add device-specific GATT UUIDs.

## Features

- Simulated device discovery and connection lifecycle
- Simulated characteristic reads/writes
- Negative tests for invalid timeouts, unknown devices/characteristics, disconnected access, and injected failures
- pytest fixtures and assertions
- JSON and standalone HTML summary reports (with optional `pytest-json-report` plugin)
- Linux-friendly command-line workflow

## Project structure

```text
bluetooth-test-automation/
├── src/ble_framework/
│   ├── __init__.py
│   ├── simulator.py
│   └── reporting.py
├── tests/
│   ├── conftest.py
│   └── test_ble_functional.py
├── reports/
├── pytest.ini
├── requirements.txt
├── run_tests.py
└── README.md
```

## Run on Linux / Ubuntu / WSL

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pytest-json-report
python run_tests.py
```

On Windows PowerShell, activate the environment with `.venv\\Scripts\\Activate.ps1` after creating it with `py -m venv .venv`.

The command prints the test summary and writes `reports/test-report.json` and `reports/test-report.html` when `pytest-json-report` is installed. Open the HTML report in a browser. Without that optional plugin, the runner falls back to `reports/junit.xml`.

You can also run pytest directly:

```bash
pytest -v
```

## Test scenarios

| Scenario | Expected result |
|---|---|
| Device discovery | Returns the expected simulated device |
| Invalid scan timeout | Raises `ValueError` |
| Connect / disconnect | State changes correctly |
| Unknown device | Raises `BLEError` |
| Characteristic read | Returns simulated battery value |
| Characteristic write | New value can be read back |
| Operation while disconnected | Raises `BLEError` |
| Unknown characteristic | Raises `BLEError` |
| Injected connection failure | Failure is surfaced clearly |
| Injected write failure | Failure is surfaced clearly |

## Next step: real BLE hardware

For real hardware, use a compatible Bluetooth adapter and a known BLE peripheral. Install `bleak`, implement a separate adapter around `BleakScanner` and `BleakClient`, and update the tests to use a controlled device and its documented service/characteristic UUIDs. Keep simulator tests as fast unit tests and mark hardware tests separately so CI can run without a peripheral.

## Resume description

**Bluetooth Test Automation Framework | Python, pytest, Linux, Git, BLE Simulation, JSON/HTML Reporting**

- Built a Python/pytest framework to validate simulated BLE discovery, connection handling, characteristic data exchange, disconnection, and error paths.
- Created positive and negative test cases with assertions, fixtures, and exception handling to improve repeatability and failure diagnosis.
- Added structured test reporting with JSON and standalone HTML summaries for quick review of pass/fail outcomes.
- Designed the simulator abstraction so the test suite can later be connected to a real BLE client and hardware test setup.

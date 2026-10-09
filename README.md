# Bluetooth Test Automation Framework

### Python | Pytest | Bluetooth Low Energy (BLE) | Linux | Test Automation

A Python-based test automation framework designed to simulate Bluetooth Low Energy (BLE) functional validation scenarios, verify device interaction workflows, and generate structured test reports for debugging and test result analysis.

This project demonstrates a systematic approach to embedded software validation through reusable test cases, automated assertions, negative testing, exception handling, and machine-readable test reporting.

> **Project type:** Embedded Systems Test Automation  
> **Testing approach:** BLE simulation and automated functional testing  
> **Current scope:** Software-based simulation; physical Bluetooth hardware integration is a future enhancement.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Engineering Objectives](#engineering-objectives)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Test Coverage](#test-coverage)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Running the Tests](#running-the-tests)
- [Test Reporting](#test-reporting)
- [Engineering Approach](#engineering-approach)
- [Limitations and Future Enhancements](#limitations-and-future-enhancements)
- [Skills Demonstrated](#skills-demonstrated)
- [Author](#author)

---

## Project Overview

Bluetooth Low Energy is widely used in embedded products, connected devices, sensors, and wireless communication systems. Validating device discovery, connection handling, data exchange, and failure scenarios is an important part of developing reliable wireless software.

This project implements a Python-based automation framework that simulates BLE device interactions and executes repeatable functional test scenarios using Pytest.

The framework is designed to:

- Automate functional test execution.
- Validate expected behavior using assertions.
- Exercise positive and negative test scenarios.
- Capture test failures for troubleshooting.
- Generate structured reports for reviewing test outcomes.

The objective is to demonstrate foundational embedded validation and test automation practices relevant to entry-level embedded software testing and validation roles.

## Engineering Objectives

1. **Functional validation:** Verify expected behavior across simulated BLE interaction workflows.
2. **Test automation:** Replace repetitive manual checks with reusable automated test cases.
3. **Negative testing:** Evaluate how the framework handles invalid inputs and simulated failures.
4. **Debugging support:** Capture test outcomes and diagnostic information.
5. **Reporting:** Produce machine-readable JSON results and human-readable HTML reports.

## Key Features

| Feature | Description |
|---|---|
| BLE device discovery | Simulates device scanning and discovery scenarios. |
| Connection handling | Tests connection establishment and disconnection workflows. |
| Data exchange | Validates simulated characteristic read and write operations. |
| Negative testing | Covers invalid inputs and simulated connection failures. |
| Automated assertions | Checks expected outcomes and reports unexpected behavior. |
| Exception handling | Handles supported error scenarios during test execution. |
| Test reporting | Generates JSON and HTML summaries for analysis. |
| Repeatable execution | Uses Pytest to organize and execute automated tests. |

## System Architecture

The framework follows a modular testing workflow:

```text
          Test Execution
                |
                v
         Pytest Test Suite
                |
                v
       BLE Simulation Layer
                |
                v
      Simulated BLE Operations
                |
        +-------+-------+
        |               |
        v               v
   Assertions       Error Scenarios
        |               |
        +-------+-------+
                |
                v
        Test Result Collection
                |
          +-----+-----+
          |           |
          v           v
      JSON Report  HTML Report
```

**Workflow:** Pytest executes test cases against the simulated BLE layer, evaluates expected outcomes, and collects results for reporting.

The current architecture does not directly communicate with a physical BLE device.

## Test Coverage

The framework is intended to cover the following functional areas:

| Test area | Validation objective |
|---|---|
| Device discovery | Verify simulated discovery results. |
| Connection | Validate successful connection scenarios. |
| Disconnection | Verify device disconnection behavior. |
| Data exchange | Validate simulated characteristic reads and writes. |
| Invalid device | Check behavior for unsupported or unknown devices. |
| Connection failure | Verify expected handling of simulated failures. |
| Invalid operations | Check error handling for invalid requests. |
| Result validation | Ensure actual outcomes match expected outcomes. |

Test coverage depends on the scenarios implemented in the test suite. See the test files for the exact executable cases.

## Technology Stack

- **Python:** Test logic, reusable functions, and error handling.
- **Pytest:** Test discovery, execution, fixtures, and assertions.
- **Linux / Ubuntu:** Development and test execution environment.
- **Git and GitHub:** Version control and project management.
- **JSON:** Structured test result output.
- **HTML:** Human-readable test reporting.
- **BLE simulation:** Software-based modeling of Bluetooth interaction scenarios.

## Project Structure

```text
bluetooth-test-automation/
├── tests/
│   └── test_ble_functionality.py
├── reports/
│   ├── test-report.json
│   └── test-report.html
├── requirements.txt
├── pytest.ini
├── run_tests.py
└── README.md
```

*Note: The structure above is illustrative. Adjust filenames to match the actual repository contents before publishing.*

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version.
- Linux / Ubuntu, WSL, or another supported Python environment.
- Git.
- Basic familiarity with Python and automated testing.

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd bluetooth-test-automation
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install pytest-json-report
```

If the JSON reporting plugin is already included in the dependency file, the additional installation is unnecessary.

## Running the Tests

Execute the project test runner:

```bash
python run_tests.py
```

Alternatively, run Pytest directly:

```bash
python -m pytest -v
```

To generate a JSON report using the Pytest JSON reporting plugin:

```bash
python -m pytest -v --json-report --json-report-file=reports/test-report.json
```

Use the reporting command supported by the current project configuration. HTML report generation must be configured in the test runner or through a compatible reporting plugin.

## Test Reporting

The framework supports reviewing test execution results through structured reporting.

**JSON report**

Useful for automated result processing, CI pipelines, and extracting test status information.

**HTML report**

Useful for quickly reviewing test outcomes, identifying failures, and presenting results to engineers.

Recommended metrics to track as the project evolves:

- Total test cases executed.
- Passed and failed test cases.
- Test execution duration.
- Failure messages and diagnostic logs.
- Regression results between test runs.

Only report test counts and execution results that can be reproduced from the current test suite.

## Engineering Approach

The framework applies several core software testing principles:

- **Modularity:** Separate test scenarios from simulated device behavior.
- **Repeatability:** Execute the same test scenarios consistently.
- **Assertions:** Compare actual outcomes with expected behavior.
- **Negative testing:** Exercise invalid operations and failure conditions.
- **Diagnostics:** Capture useful information to help investigate failures.
- **Maintainability:** Organize tests so new scenarios can be added systematically.

## Limitations and Future Enhancements

The current project focuses on software-based BLE simulation. Simulation can validate the test framework's logic, but it cannot establish the real-world reliability or interoperability of Bluetooth hardware.

Planned enhancements:

- Integrate real BLE scanning and communication using Python's Bleak library.
- Validate GATT services, characteristics, and descriptors on physical devices.
- Add configurable connection timeouts and retry scenarios.
- Introduce parameterized tests for multiple device configurations.
- Add test logging and failure diagnostics.
- Integrate automated testing into GitHub Actions.
- Explore Bluetooth protocol analysis and hardware-in-the-loop validation.

## Skills Demonstrated

**Programming and automation**
- Python
- Pytest
- Test fixtures and assertions
- Exception handling

**Embedded validation fundamentals**
- BLE functional testing concepts
- Device discovery and connection workflows
- Data exchange validation
- Negative and failure scenario testing

**Development tools**
- Linux / Ubuntu
- Git and GitHub
- JSON and HTML reporting
- Test result analysis

These skills reflect the project's implementation scope and are not a claim of professional Bluetooth qualification or physical hardware testing.

## Author

**Manjunath G. L.**

Mechatronics Engineering | Aspiring Embedded Software & Validation Engineer

Interested in embedded systems, Python-based test automation, firmware validation, wireless connectivity, and reliable software for connected devices.

- **GitHub:** [Add your GitHub profile URL](https://github.com/)
- **LinkedIn:** [Add your LinkedIn profile URL](https://www.linkedin.com/)

---

*This project is intended as a learning and portfolio demonstration of embedded software test automation fundamentals.*

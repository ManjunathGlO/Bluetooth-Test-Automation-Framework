# Bluetooth Test Automation Framework

### Python · Pytest · Bluetooth Low Energy (BLE) · Linux · Test Automation

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest"/>
  <img src="https://img.shields.io/badge/Bluetooth-LE-0082FC?style=for-the-badge&logo=bluetooth&logoColor=white" alt="Bluetooth Low Energy"/>
  <img src="https://img.shields.io/badge/Linux-Ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux"/>
  <img src="https://img.shields.io/badge/Reports-JSON%20%7C%20HTML-2E8B57?style=for-the-badge" alt="JSON and HTML reports"/>
</p>

<p align="center">
  <b>A Python-based framework for automating simulated Bluetooth Low Energy functional validation scenarios.</b>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/manjunathgl/">LinkedIn</a> •
  <a href="https://github.com/ManjunathGlO">GitHub Profile</a>
</p>

---

## 📌 Project Overview

Bluetooth Low Energy (BLE) is widely used in embedded devices, wireless sensors, connected products, and IoT applications. Reliable wireless functionality requires systematic testing of device discovery, connection handling, data exchange, and failure scenarios.

The **Bluetooth Test Automation Framework** is a Python-based project that uses Pytest to execute repeatable functional tests against a simulated BLE environment.

The framework demonstrates core software validation practices, including automated assertions, positive and negative testing, exception handling, and structured test reporting.

**Project objective:** Develop a maintainable foundation for embedded connectivity testing and demonstrate practical test automation concepts relevant to entry-level embedded software validation roles.

> **Testing scope:** This version uses BLE simulation. It does not establish a connection to physical Bluetooth hardware.

## 🎯 Engineering Objectives

- Automate repeatable BLE functional test scenarios.
- Validate expected behavior using assertions.
- Test device discovery, connection, disconnection, and simulated data exchange.
- Exercise invalid inputs and simulated failure conditions.
- Improve debugging through test logs and failure messages.
- Generate structured JSON and human-readable HTML reports.
- Build a foundation for future hardware-based connectivity testing.

## ✨ Key Features

| Feature | Description |
|---|---|
| Device discovery | Simulates BLE scanning and device discovery scenarios. |
| Connection handling | Tests simulated connection and disconnection workflows. |
| Data exchange | Validates simulated characteristic read and write operations. |
| Negative testing | Exercises invalid inputs and simulated connection failures. |
| Automated assertions | Compares actual results with expected outcomes. |
| Exception handling | Tests supported error scenarios and unexpected outcomes. |
| Test reporting | Supports structured JSON and HTML result summaries. |
| Repeatable execution | Uses Pytest to organize and execute test cases. |
| Linux compatibility | Supports development in Linux / Ubuntu environments. |

## 🏗️ System Architecture

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
          +---------+---------+
          |                   |
          v                   v
    Functional Tests     Negative Tests
          |                   |
          +---------+---------+
                    |
                    v
          Assertions & Validation
                    |
                    v
            Result Collection
                    |
              +-----+-----+
              |           |
              v           v
          JSON Report  HTML Report
```

### Workflow

1. Pytest discovers and executes the automated test cases.
2. The test cases interact with the BLE simulation layer.
3. Assertions validate the expected behavior.
4. Negative scenarios exercise error-handling paths.
5. Test outcomes are collected and presented through configured reports.

The simulated environment validates the test framework's behavior, not the performance or interoperability of physical Bluetooth devices.

## 🧪 Test Scenarios

The project focuses on the following functional testing areas.

| Test scenario | Validation objective |
|---|---|
| Device discovery | Verify simulated discovery results. |
| Successful connection | Validate expected connection behavior. |
| Disconnection | Check simulated disconnection handling. |
| Characteristic read | Verify expected simulated read results. |
| Characteristic write | Validate simulated data-write behavior. |
| Unknown device | Exercise invalid or unsupported device handling. |
| Connection failure | Check the expected response to simulated failures. |
| Invalid operation | Validate supported error-handling scenarios. |
| Result assertions | Detect mismatches between expected and actual outcomes. |

The actual test coverage and number of executable cases depend on the implementation in the repository's test files.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Test logic, reusable functions, and error handling |
| Pytest | Test execution, assertions, and test organization |
| Linux / Ubuntu | Development and test execution environment |
| Git / GitHub | Version control and source management |
| JSON | Structured test result reporting |
| HTML | Human-readable test summaries |
| BLE simulation | Software-based modeling of BLE interaction scenarios |

## 📂 Project Structure

```text
bluetooth-test-automation/
│
├── tests/
│   └── test_ble_functionality.py
│
├── reports/
│   ├── test-report.json
│   └── test-report.html
│
├── requirements.txt
├── pytest.ini
├── run_tests.py
└── README.md
```

> **Note:** Update the example tree to match the actual files and directory names in your repository before publishing.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or another version supported by the project.
- Git.
- Linux / Ubuntu, WSL, or another compatible environment.
- Basic knowledge of Python and automated testing.

### Step 1: Clone the repository

```bash
git clone https://github.com/ManjunathGlO/bluetooth-test-automation.git
cd bluetooth-test-automation
```

Replace the repository URL and directory name if your GitHub repository uses a different name.

### Step 2: Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If JSON reporting uses the `pytest-json-report` plugin and it is not already included in `requirements.txt`, install it with:

```bash
pip install pytest-json-report
```

## ▶️ Running the Tests

Run the project's test runner:

```bash
python run_tests.py
```

Alternatively, execute Pytest directly:

```bash
python -m pytest -v
```

To generate a JSON report using the `pytest-json-report` plugin:

```bash
mkdir -p reports
python -m pytest -v \
  --json-report \
  --json-report-file=reports/test-report.json
```

Use the commands supported by the actual project configuration. HTML reporting must be implemented in the test runner or configured with a compatible reporting plugin.

## 📊 Test Reporting

The framework is designed to make test outcomes easier to inspect and analyze.

### JSON report

JSON reporting is useful for:

- Structured test result storage.
- Automated result processing.
- Identifying failed test cases.
- Integrating results with future CI pipelines.

### HTML report

HTML reporting is useful for:

- Reviewing test execution results.
- Presenting test outcomes clearly.
- Investigating failures.
- Sharing test summaries with engineering teams.

### Recommended validation metrics

As the framework evolves, consider tracking:

- Total tests executed.
- Passed and failed tests.
- Test execution duration.
- Failure messages and diagnostic logs.
- Regression results across multiple test runs.

Only publish test counts and report screenshots that can be reproduced from your current implementation.

## 🔍 Engineering Practices Demonstrated

**Modular test design**
- Organizing tests into understandable, reusable functions.
- Separating test scenarios from simulated BLE behavior.

**Functional validation**
- Defining expected outcomes.
- Using assertions to identify unexpected behavior.

**Negative testing**
- Exercising invalid inputs and simulated failures.
- Checking error-handling behavior.

**Debugging and reporting**
- Capturing test outcomes.
- Producing structured reports for troubleshooting.

**Maintainability**
- Keeping the test suite organized.
- Creating a foundation for additional test scenarios.

## 🚀 Future Enhancements

The following enhancements could extend the framework toward practical embedded connectivity validation.

- [ ] Integrate real BLE scanning and communication using Python's Bleak library.
- [ ] Validate GATT services, characteristics, and descriptors on physical devices.
- [ ] Add configurable connection timeouts and retry scenarios.
- [ ] Introduce parameterized tests for multiple device configurations.
- [ ] Improve diagnostic logging and failure analysis.
- [ ] Add regression testing and test coverage measurement.
- [ ] Integrate automated execution with GitHub Actions.
- [ ] Explore Bluetooth protocol analysis and hardware-in-the-loop testing.

These items represent potential future work, not features claimed as currently implemented.

## 💼 Skills Demonstrated

**Programming and test automation**
- Python
- Pytest
- Automated assertions
- Exception handling
- Test case design

**Embedded systems and connectivity**
- Bluetooth Low Energy fundamentals
- Device discovery and connection workflows
- Simulated data exchange
- Functional and negative testing

**Development tools**
- Linux / Ubuntu
- Git and GitHub
- JSON and HTML reporting
- Test result analysis

## 👨‍💻 About the Developer

**Manjunath G. L.**  
*Mechatronics Engineering | Aspiring Embedded Software & Validation Engineer*

I am interested in embedded systems, wireless connectivity, firmware validation, and Python-based test automation. My goal is to apply engineering fundamentals to practical testing challenges and develop reliable, maintainable validation solutions.

I am particularly interested in entry-level opportunities involving embedded software testing, connectivity validation, automation frameworks, and smart-device technologies.

### 🤝 Let's Connect

<p align="center">
  <a href="https://www.linkedin.com/in/manjunathgl/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect%20with%20me-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect with me on LinkedIn"/>
  </a>
  <a href="https://github.com/ManjunathGlO">
    <img src="https://img.shields.io/badge/GitHub-Explore%20my%20projects-181717?style=for-the-badge&logo=github&logoColor=white" alt="Explore my GitHub projects"/>
  </a>
</p>

<p align="center">
  <i>Building. Testing. Debugging. Improving.</i><br/>
  <b>Turning engineering fundamentals into practical solutions.</b>
</p>

---

<p align="center">
  If you find this project useful, consider giving the repository a ⭐
</p>

<p align="center">
  <sub>Developed as an embedded systems test automation learning project.</sub>
</p>

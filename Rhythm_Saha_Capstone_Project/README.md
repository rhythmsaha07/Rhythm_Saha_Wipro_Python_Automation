# 🚀 Wipro Selenium Python Automation Framework

> **A maintainable, data-driven UI automation framework built with Selenium WebDriver, PyTest, Page Object Model, reusable utilities, structured logging, failure evidence, and HTML reporting.**

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-Test%20Framework-0A9EDC?logo=pytest&logoColor=white)
![POM](https://img.shields.io/badge/Design-Page%20Object%20Model-6C5CE7)
![HTML Report](https://img.shields.io/badge/Reporting-HTML-orange)
![Status](https://img.shields.io/badge/Status-6%2F6%20Passed-2EA44F)

---

## 📌 Project Overview

This project is a **production-style Selenium Python automation framework** developed for the **Wipro Selenium Python Automation Capstone**.

Instead of treating automation as a collection of individual Selenium scripts, the framework is designed around software-engineering principles such as:

- 🧩 **Page Object Model (POM)**
- 🔄 **Data-driven testing**
- 🧪 **PyTest-based execution**
- 🔗 **Python `unittest` compatibility**
- ⏱️ **Explicit synchronization**
- 📸 **Failure screenshot capture**
- 📝 **Structured logging**
- 📊 **HTML execution reporting**
- ⚙️ **Centralized configuration**
- ♻️ **Reusable framework utilities**
- 📦 **Reproducible project setup**

The goal is to demonstrate not only **how to automate a browser**, but also **how to design an automation framework that remains maintainable as test coverage grows**.

---

## 🌐 Application Under Test

### Automation Exercise

**Application:** Automation Exercise  
**URL:** https://automationexercise.com/

The framework currently automates:

| Area | Coverage |
|---|---|
| 🔐 Invalid Login | Data-driven validation |
| 🔎 Product Search | Data-driven product search |
| 🧪 PyTest | Primary test execution |
| 🧰 unittest | Framework compatibility |
| 📸 Failure Diagnostics | Automatic screenshots |
| 📝 Logging | Execution and diagnostic logs |
| 📊 Reporting | Self-contained HTML report |
| 🧱 POM | Page-level UI abstraction |

---

# 🏗️ Framework Architecture

The framework follows a layered architecture where each layer has a clearly defined responsibility.

```text
                         ┌──────────────────────────┐
                         │       TEST LAYER         │
                         │   PyTest / unittest      │
                         │                          │
                         │ test_login.py            │
                         │ test_search.py           │
                         │ test_unittest_search.py  │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │     PAGE OBJECT LAYER    │
                         │                          │
                         │ LoginPage / HomePage     │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │      BASE PAGE LAYER     │
                         │                          │
                         │ waits / interactions     │
                         │ reusable browser logic   │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │    SELENIUM WEBDRIVER    │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │    AUTOMATION EXERCISE   │
                         │      APPLICATION          │
                         └──────────────────────────┘


     ┌─────────────────┐       ┌─────────────────┐
     │   TEST DATA     │──────►│  TEST SCENARIOS │
     │      CSV        │       └─────────────────┘
     └─────────────────┘

     ┌─────────────────┐       ┌─────────────────┐
     │ CONFIGURATION   │──────►│    FRAMEWORK    │
     └─────────────────┘       └─────────────────┘

     ┌─────────────────┐       ┌─────────────────┐
     │     LOGGER      │──────►│   DIAGNOSTICS   │
     └─────────────────┘       └─────────────────┘

     ┌─────────────────┐       ┌─────────────────┐
     │   SCREENSHOTS   │──────►│ FAILURE EVIDENCE│
     └─────────────────┘       └─────────────────┘

     ┌─────────────────┐       ┌─────────────────┐
     │   HTML REPORT   │──────►│ TEST RESULTS    │
     └─────────────────┘       └─────────────────┘
```

### 🎯 Design Philosophy

> **Tests describe what should happen. Page Objects describe how the UI is operated. Utilities provide reusable framework services. Test data remains independent from test logic.**

This separation reduces duplication and makes the framework easier to debug and extend.

---

# 📁 Project Structure

```text
Rhythm_Saha_Capstone_Project/
│
├── 📂 pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   └── login_page.py
│
├── 📂 tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_search.py
│   └── test_unittest_search.py
│
├── 📂 utils/
│   ├── __init__.py
│   ├── config_reader.py
│   ├── csv_reader.py
│   └── logger.py
│
├── 📂 config/
│   └── config.ini
│
├── 📂 test_data/
│   ├── login_data.csv
│   └── product_search.csv
│
├── 📂 screenshots/
│   ├── 📂 evidence/
│   │   ├── test_invalid_login_data0.png
│   │   ├── test_invalid_login_data1.png
│   │   ├── test_product_search_product_data0.png
│   │   ├── test_product_search_product_data1.png
│   │   ├── test_product_search_product_data2.png
│   │   └── test_product_search_using_unittest.png
│   │
│   └── 📂 failures/
│       ├── test_invalid_login[data0].png
│       └── test_product_search.png
│
├── 📂 reports/
│   ├── automation.log
│   └── test_report.html
│
├── 📄 conftest.py
├── 📄 pytest.ini
├── 📄 requirements.txt
├── 📄 README.md
└── 📂 .venv/
```

### 🔍 Responsibility of Each Layer

| Component | Responsibility |
|---|---|
| `pages/` | Encapsulates page locators and UI interactions |
| `tests/` | Contains business-oriented test scenarios |
| `utils/` | Provides reusable framework services |
| `config/` | Stores configurable framework/application values |
| `test_data/` | Stores external test inputs |
| `screenshots/` | Stores failure evidence |
| `reports/` | Stores logs and HTML execution reports |
| `conftest.py` | Manages fixtures, browser lifecycle, and failure handling |
| `pytest.ini` | Controls PyTest configuration |
| `requirements.txt` | Defines project dependencies |
| `README.md` | Documents setup, architecture, execution, and maintenance |

> ⚠️ Runtime directories such as `.venv/`, `__pycache__/`, and `.pytest_cache/` should not be committed to source control.

---

# 🧪 Automated Test Coverage

## 🔐 1. Invalid Login Validation

### Objective

Verify that invalid login combinations are correctly rejected by the application.

### Approach

- PyTest parametrization
- CSV-based test data
- Page Object Model
- Explicit waits
- Assertion-based validation

### Flow

```text
Login Test
    │
    ▼
Load login credentials from CSV
    │
    ▼
Open Login Page
    │
    ▼
Enter invalid email/password
    │
    ▼
Submit Login
    │
    ▼
Validate error message
    │
    ▼
PASS / FAIL
```

---

## 🔎 2. Data-Driven Product Search

### Objective

Validate product search functionality using multiple independent datasets.

### Approach

- PyTest parametrization
- CSV-based test data
- Page Object Model
- Explicit synchronization
- Product-result validation

### Current datasets

The framework validates **three product-search inputs** from:

```text
test_data/product_search.csv
```

### Flow

```text
CSV Test Data
     │
     ▼
PyTest Parameterization
     │
     ▼
Open Products
     │
     ▼
Enter Product Name
     │
     ▼
Execute Search
     │
     ▼
Validate "SEARCHED PRODUCTS"
     │
     ▼
Validate Product Results
     │
     ▼
PASS / FAIL
```

---

# 🧰 3. unittest Compatibility

The framework also demonstrates that the Page Object layer is reusable outside a PyTest-only implementation.

```text
tests/test_unittest_search.py
```

The test uses Python's standard `unittest` framework while reusing the same page-object components.

This demonstrates separation between:

```text
Test Framework
       │
       ├── PyTest
       │
       └── unittest
              │
              ▼
        Shared Page Objects
              │
              ▼
          Selenium
```

---

# 📊 Latest Validation

The latest successful execution validated **6 automated tests**:

```text
✓ test_invalid_login[data0]
✓ test_invalid_login[data1]

✓ test_product_search[product_data0]
✓ test_product_search[product_data1]
✓ test_product_search[product_data2]

✓ TestProductSearch::test_product_search_using_unittest
```

### 🟢 Execution Result

```text
Total Tests : 6
Passed      : 6
Failed      : 0
Skipped     : 0
Errors      : 0
```

This result is also represented in the generated HTML execution report.

> **Note:** The numbers above describe the documented latest validation run. Re-run the suite before presenting them as a new execution result.

---

# ⏱️ Synchronization Strategy

Reliable UI automation should not depend on arbitrary delays such as:

```python
time.sleep(5)
```

The framework primarily uses **Selenium explicit waits** to synchronize with the application's state.

### Why?

Explicit synchronization helps handle:

- 🌐 Dynamic page loading
- 🖥️ Delayed rendering
- 🔄 Navigation transitions
- ⚡ Asynchronously loaded elements
- 🧩 Interactive UI states

### Preferred approach

```text
Test Action
    │
    ▼
Wait for required UI state
    │
    ▼
Perform interaction
    │
    ▼
Validate expected state
```

This improves stability compared with fixed-duration sleeps.

---

# 📸 Screenshot & Evidence Strategy

The framework intentionally separates **successful execution evidence** from **failure diagnostics**.

This provides a clearer and more auditable view of test execution.

## ✅ Evidence Screenshots

Successful tests are captured under:

```text
screenshots/evidence/
```

The current PyTest execution produces:

```text
evidence/
├── test_invalid_login_data0.png
├── test_invalid_login_data1.png
├── test_product_search_product_data0.png
├── test_product_search_product_data1.png
├── test_product_search_product_data2.png
└── test_product_search_using_unittest.png
```

These screenshots provide visual evidence of the browser state associated with successful test execution.

## 🚨 Failure Screenshots

Failed tests are captured separately under:

```text
screenshots/failures/
```

Existing failure artifacts are retained independently from successful execution evidence.

```text
failures/
├── test_invalid_login[data0].png
└── test_product_search.png
```

The PyTest fixture handles failure screenshots for PyTest tests, while the standalone `unittest` implementation manages its own failure screenshot because it creates its own WebDriver instance.

### Evidence vs Failure Flow

```text
                    TEST EXECUTION
                          │
                 ┌────────┴────────┐
                 │                 │
               PASS              FAIL
                 │                 │
                 ▼                 ▼
          screenshots/       screenshots/
            evidence/          failures/
                 │                 │
                 ▼                 ▼
        Execution Evidence   Failure Diagnostics
```

This separation ensures that successful execution evidence does not overwrite or replace failure artifacts.

---

# 🛡️ Failure Diagnostics

A failed UI test should provide **evidence**, not merely a red test result.

The framework therefore captures diagnostic artifacts independently from successful execution evidence.

## 📸 Failure Screenshots

When a PyTest test fails, the screenshot is stored under:

```text
screenshots/failures/
```

The unittest implementation also captures its own failure screenshot because it manages its Selenium driver independently from the PyTest fixture.

Failure screenshots help identify problems such as:

- Unexpected overlays
- Incorrect navigation
- Missing elements
- Application errors
- UI changes
- Synchronization problems

## 📝 Execution Logs

Framework logs are stored in:

```text
reports/automation.log
```

Logs help distinguish between:

```text
Framework Setup
       │
       ├── Browser initialization
       ├── Application launch
       ├── Test execution
       ├── Navigation
       ├── Evidence capture
       ├── Failure diagnostics
       └── Teardown
```

## 💥 PyTest Failure Information

Terminal output provides:

- Failing test name
- Source location
- Exception type
- Stack trace
- Execution timing

Together, these artifacts make failures easier to investigate and reproduce.

---

# 📈 HTML Reporting

The framework uses **pytest-html** to generate a self-contained HTML execution report.

```text
reports/test_report.html
```

The report provides:

- 📊 Execution summary
- ✅ Pass/fail status
- ⏱️ Test duration
- 🖥️ Platform information
- 🐍 Python information
- 🔌 Plugin information
- 🧪 Individual test results

### Generate the report

```bash
pytest --html=reports/test_report.html --self-contained-html
```

---

# ⚙️ Configuration Management

Framework configuration is separated from test and page logic.

```text
config/config.ini
```

A reusable configuration reader provides controlled access to framework settings.

### Benefits

- 🔧 Centralized configuration
- ♻️ Reduced duplication
- 🌍 Easier environment switching
- 🧩 Cleaner test code
- 🚀 Future support for DEV / QA / STAGING environments

Example conceptual structure:

```text
                config.ini
                    │
                    ▼
             Config Reader
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
    Base URL     Timeout      Browser
        │           │           │
        └───────────┼───────────┘
                    ▼
                Framework
```

---

# 🗃️ Data-Driven Testing

Test data is intentionally separated from automation logic.

```text
                 Test Logic
                     │
                     ▼
                CSV Reader
                     │
             ┌───────┴────────┐
             ▼                ▼
       login_data.csv   product_search.csv
             │                │
             └───────┬────────┘
                     ▼
              PyTest Parameters
                     │
                     ▼
                Test Execution
```

### Advantages

✅ Add new scenarios without duplicating test code  
✅ Keep test logic clean  
✅ Improve maintainability  
✅ Make test inputs easy to review  
✅ Support scalable regression testing  

---

# 📝 Logging Strategy

The reusable logging utility is located at:

```text
utils/logger.py
```

Logs are persisted to:

```text
reports/automation.log
```

Logging can help identify:

| Event | Diagnostic Value |
|---|---|
| Browser startup | Environment verification |
| Application launch | Navigation verification |
| Test execution | Execution trace |
| Page interaction | Flow diagnosis |
| Screenshot capture | Failure evidence |
| Teardown | Resource lifecycle |

---

# 🧱 Page Object Model

The framework uses **Page Object Model (POM)** to separate UI implementation details from test intent.

### Without POM

```text
Test Case
   │
   ├── XPath
   ├── CSS Selector
   ├── click()
   ├── send_keys()
   ├── waits
   └── assertions
```

This can make tests difficult to maintain when the UI changes.

### With POM

```text
Test Case
    │
    ▼
Page Object
    │
    ├── Locators
    ├── UI Actions
    └── Synchronization
            │
            ▼
        Selenium
```

### Example responsibility

```text
test_search.py
      │
      ▼
HomePage.search_product()
      │
      ▼
Search Input / Search Button
      │
      ▼
Selenium WebDriver
```

The test therefore remains focused on **business behavior**, while the Page Object owns the UI implementation.

---

# 🔄 Test Execution Lifecycle

```text
                    ┌──────────────┐
                    │    START     │
                    └──────┬───────┘
                           ▼
                ┌────────────────────┐
                │ Load Configuration │
                └─────────┬──────────┘
                          ▼
                ┌────────────────────┐
                │ Initialize Browser │
                └─────────┬──────────┘
                          ▼
                ┌────────────────────┐
                │ Launch Application │
                └─────────┬──────────┘
                          ▼
                ┌────────────────────┐
                │ Execute Test Case │
                └─────────┬──────────┘
                          ▼
                   ┌─────────────┐
                   │   Result?   │
                   └──────┬──────┘
                    ┌─────┴─────┐
                   PASS         FAIL
                    │             │
                    │       ┌─────▼────────┐
                    │       │  Screenshot  │
                    │       └─────┬────────┘
                    │             ▼
                    │       ┌──────────────┐
                    │       │ Diagnostic   │
                    │       │ Logging      │
                    │       └─────┬────────┘
                    │             │
                    └──────┬──────┘
                           ▼
                   ┌──────────────┐
                   │   Teardown   │
                   └──────┬───────┘
                          ▼
                   ┌──────────────┐
                   │ HTML Report  │
                   └──────┬───────┘
                          ▼
                   ┌──────────────┐
                   │     END      │
                   └──────────────┘
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Automation programming language |
| 🌐 **Selenium WebDriver** | Browser automation |
| 🧪 **PyTest** | Test execution and parametrization |
| 🧱 **Page Object Model** | Maintainable UI abstraction |
| 📄 **CSV** | External test data |
| ⚙️ **ConfigParser** | Configuration management |
| 📝 **Logging** | Execution diagnostics |
| 📸 **Screenshots** | Failure evidence |
| 📊 **pytest-html** | HTML reporting |
| 🪟 **Chrome** | Browser under test |

---

# 🚀 Installation & Setup

## 1️⃣ Clone or copy the project

```bash
git clone <repository-url>
cd Selenium_Python_Automation_Framework
```

If the project is already available locally, simply open the project directory.

---

## 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

---

## 3️⃣ Activate the environment

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

---

## 4️⃣ Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 5️⃣ Verify Python

```bash
python --version
```

---

## 6️⃣ Run the complete test suite

```bash
pytest
```

---

# ▶️ Execution Commands

### 🧪 Run all tests

```bash
pytest
```

### 🔐 Run login tests

```bash
pytest tests/test_login.py
```

### 🔎 Run product-search tests

```bash
pytest tests/test_search.py
```

### 🧰 Run unittest-based test

```bash
pytest tests/test_unittest_search.py
```

### 📊 Generate HTML report

```bash
pytest --html=reports/test_report.html --self-contained-html
```

### 🔍 Run with verbose output

```bash
pytest -v
```

---

# 🧭 Troubleshooting Guide

| Symptom | Recommended Checks |
|---|---|
| `ModuleNotFoundError` | Verify virtual environment and dependencies |
| Browser does not start | Check Chrome installation and Selenium environment |
| `TimeoutException` | Check locator, synchronization, navigation state, and overlays |
| Element not found | Verify locator and current page |
| Works manually but fails in automation | Check timing, overlays, page state, and synchronization |
| Driver/session issue | Verify browser/Selenium compatibility |
| Test data not loaded | Check CSV path, headers, encoding, and reader |
| HTML report missing | Verify `pytest-html` and output directory |
| Screenshot not generated | Check failure hook/path and write permissions |

---

# 📦 Reproducibility

The framework uses an isolated Python environment and a dependency file so that another user can recreate the execution environment.

### Dependency installation

```bash
python -m pip install -r requirements.txt
```

### Dependency verification

```bash
pip list
```

### Recommended source-control exclusions

```text
.venv/
__pycache__/
.pytest_cache/
*.pyc
```

---

# 🎯 Engineering Principles Demonstrated

### 🧩 Separation of Concerns

Tests, page interactions, data, configuration, utilities, and reporting are separated.

### ♻️ Reusability

Common browser operations and framework services are centralized.

### 🛠️ Maintainability

UI changes can primarily be handled within the corresponding Page Object rather than across multiple test files.

### 📊 Data-Driven Testing

Test inputs are externalized into CSV files.

### 🔍 Observability

Failures produce diagnostic information, screenshots, and logs.

### 🔁 Reproducibility

Dependencies and execution commands are documented.

### 📈 Extensibility

The architecture can accommodate additional pages, test scenarios, datasets, and reporting integrations.

---

# 🏆 What This Project Demonstrates

This framework goes beyond basic Selenium scripting.

It demonstrates an end-to-end automation mindset:

```text
                 AUTOMATION FRAMEWORK
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
 Maintainability     Reusability      Data Separation
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                 Reliable Execution
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        Diagnostics            Reporting
              │                     │
              └──────────┬──────────┘
                         ▼
                  Reproducibility
```

The project therefore demonstrates not only **test execution**, but also the engineering practices required to build a framework that can evolve with an application's regression suite.

---

# 🔮 Future Enhancements

The current framework provides a foundation for further automation capabilities.

Potential future improvements include:

- 🌐 Cross-browser execution
- ⚙️ Environment-specific configuration
- ⚡ Parallel test execution
- 🔁 Controlled retry mechanisms for infrastructure failures
- 📊 Allure or advanced reporting
- 🔄 CI/CD integration
- 🏷️ Smoke and regression test tagging
- 🧪 Expanded regression coverage
- 🔌 API + UI hybrid validation
- ☁️ Remote browser execution
- 📸 Richer report integration with screenshots
- 🐳 Containerized test execution

> These are planned extension points and are **not represented as currently implemented features**.

---

# 📂 Evidence & Quality Artifacts

The project is designed to provide more than source code.

```text
              ┌─────────────────┐
              │   Source Code   │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │    Test Data    │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │  Configuration  │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Execution Logs  │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │   Screenshots   │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │   HTML Report   │
              └────────┬────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Reproducible Testing │
            │       Evidence       │
            └──────────────────────┘
```

---

# 👨‍💻 Author

### **Rhythm Saha**

**Wipro Selenium Python Automation Capstone**

**Technology Focus:**  
Python • Selenium WebDriver • PyTest • Page Object Model • Test Automation • Data-Driven Testing • Test Reporting

---

## 📜 License

This project is intended for **educational, assessment, and portfolio demonstration purposes**.

---

<p align="center">
  <strong>🚀 Built with Python + Selenium + PyTest</strong><br>
  <sub>Designed with maintainability, reusability, diagnostics, evidence, and reproducibility in mind.</sub>
</p>

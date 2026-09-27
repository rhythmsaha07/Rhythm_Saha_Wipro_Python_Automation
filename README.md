# Wipro Python Automation Course Portfolio

<p align="center">
  <strong>Python Automation • Selenium • PyTest • POM • REST API • BDD • Robot Framework</strong>
</p>

<p align="center">
  A structured academic and technical portfolio documenting Python Automation Course, laboratory work, assignments, and the final automation capstone project.
</p>

---

## 👨‍💻 Student Information

| Field | Details |
|---|---|
| **Name** | Rhythm Saha |
| **Enrollment No.** | 12023052017065 |
| **Stream** | CSE (IOT-CSBT) |
| **Course** | Python Automation |
| **Repository** | `Rhythm_Saha_Wipro_Python_Automation` |

### 🎥 Live Capstone Demonstration

> **▶️ Watch the live demonstration of the complete Capstone Project:**  
> **[🔗 WATCH LIVE DEMONSTRATION](https://1drv.ms/v/c/6ffb79a3e58ea87c/IQC-oCLewFmgTagVCULR9H4yAQcnh61XkK4mNKBK2nWCOpo?e=K82e3U)**

**Demo Coverage:** Framework Structure • Page Object Model • Data-Driven Testing • PyTest Execution • unittest Execution • Test Reports • Screenshots / Execution Evidence • Failure Diagnostics

---

## 📌 Repository Overview

This repository presents my work completed as part of the **Wipro Python Automation Course Program**.

The repository is organized to provide a clear progression from foundational laboratory exercises and module-wise learning to a complete automation testing capstone project.

The work covers:

- 🐍 Python-based automation concepts
- 🌐 Selenium WebDriver and UI automation
- 🧪 Unit testing with `unittest` and `pytest`
- 🏗️ Page Object Model (POM)
- 📊 Data-driven testing
- 🔌 RESTful API automation concepts
- 🥒 BDD and Gherkin concepts
- 🤖 Robot Framework
- 📑 Test reporting and execution evidence
- 🛠️ Automation framework design and maintainability

---

# 📂 Repository Structure

```text
Rhythm_Saha_Wipro_Python_Automation/
│
├── 📜 README.md
│
├── 📁 Certificates/
│   ├── Certificate_1
│   ├── Certificate_2
│   └── Certificate_3
│
├── 📁 Initial_Lab_Work/
│   └── Python_Automation_Modules_1-4_Lab_Report_RhythmSaha.pdf
│
└── 📁 Rhythm_Saha_Capstone_Project/
    ├── 📜 README.md
    ├── 📁 pages/
    ├── 📁 tests/
    ├── 📁 test_data/
    ├── 📁 utils/
    ├── 📁 config/
    ├── 📁 reports/
    ├── 📁 screenshots/
    ├── 📁 logs/
    ├── 📜 conftest.py
    ├── 📜 pytest.ini
    ├── 📜 requirements.txt
    └── ...
```

> **Note:** The exact files inside the capstone project may evolve as the framework is improved. The structure above represents the intended organization of the repository.

---

# 📚 1. Initial Lab Work

The `Initial_Lab_Work/` directory contains the consolidated lab report documenting the learning and assignment work associated with **Modules 1–4 of the Wipro CoE Python Automation training**.

The report covers the following major areas:

### Module 1 — Automation with Selenium 🌐

The Selenium module introduces browser automation and the fundamentals required to create reliable UI automation scripts.

Key areas covered include:

- Selenium WebDriver architecture
- Environment and WebDriver setup
- Web element identification and locators
- Standard web controls
- Advanced web controls
- Explicit and implicit waits
- Exception handling
- Screenshots
- External test data
- Common Selenium implementation challenges

---

### Module 2 — Unit Test Frameworks 🧪

This module focuses on Python testing frameworks and framework-level organization.

Key areas include:

- Python `unittest`
- PyTest
- Test discovery and execution
- Fixtures
- `conftest.py`
- PyTest parameterization
- HTML and Allure reporting concepts
- Page Object Model
- Data-driven test integration
- Migration from `unittest` to PyTest

---

### Module 3 — Python BDD & RESTful API Automation 🔌

This module introduces API automation and Behavior-Driven Development concepts.

Key areas include:

- REST and SOAP concepts
- HTTP requests and responses
- Python `requests`
- API response validation
- HTTP methods such as GET, POST, PUT and PATCH
- Authentication and session handling
- Secure handling of credentials
- BDD concepts
- Gherkin syntax
- Behave
- Hooks
- Tags
- Scenario outlines

---

### Module 4 — Robot Framework 🤖

The Robot Framework module introduces keyword-driven automation and reusable test components.

Key areas include:

- Robot Framework fundamentals
- Keyword-driven syntax
- SeleniumLibrary
- Test case organization
- Data-driven testing
- Templates
- Resource files
- Tags
- Parallel execution concepts
- Test reports
- CI-oriented automation concepts

---

## 📄 Lab Report

The complete module-wise documentation is available here:

```text
Initial_Lab_Work/
└── Python_Automation_Modules_1-4_Lab_Report_RhythmSaha.pdf
```

The report documents the curriculum coverage, technical concepts, investigation questions, implementation challenges, and overall learning progression across Modules 1–4.

---

# 🚀 2. Capstone Project

The `Rhythm_Saha_Capstone_Project/` directory contains the complete Python Selenium automation framework developed as the major practical project.

The capstone focuses on building a structured, maintainable and reusable automation framework rather than writing isolated Selenium scripts.

## 🎯 Application Under Test

**Automation Exercise**

The project automates selected user-facing workflows on the Automation Exercise website, including:

- Invalid login validation
- Product search validation
- Product search through both PyTest and `unittest`

The framework also handles practical browser automation challenges encountered during execution, including unexpected advertisement overlays.

---

# 🏗️ Capstone Framework Architecture

The project follows a layered automation framework structure.

```text
Rhythm_Saha_Capstone_Project/
│
├── 📁 pages/
│   ├── home_page.py
│   └── login_page.py
│
├── 📁 tests/
│   ├── test_login.py
│   ├── test_search.py
│   └── test_unittest_search.py
│
├── 📁 test_data/
│   ├── login_data.csv
│   └── product_search.csv
│
├── 📁 utils/
│   ├── config_reader.py
│   ├── csv_reader.py
│   └── logger.py
│
├── 📁 config/
│   └── config.ini
│
├── 📁 reports/
│   └── ...
│
├── 📁 screenshots/
│   ├── evidence/
│   └── failures/
│
├── 📁 logs/
│   └── ...
│
├── 📜 conftest.py
├── 📜 pytest.ini
├── 📜 requirements.txt
└── 📜 README.md
```

---

# 🧩 Core Automation Concepts Implemented

## 1. Page Object Model

The framework uses the **Page Object Model (POM)** to separate page-specific locators and interactions from test logic.

Instead of placing selectors throughout the test files, page classes provide reusable methods for interacting with the application.

Example responsibilities include:

- Opening application sections
- Navigating to the Products page
- Searching for products
- Performing login actions
- Validating page state
- Counting displayed products
- Handling page-specific browser behavior

### Benefits

- Better maintainability
- Reduced selector duplication
- Cleaner test cases
- Improved code reusability
- Easier maintenance when UI elements change

---

# 📊 2. Data-Driven Testing

Test inputs are separated from test logic using CSV files.

```text
test_data/
├── login_data.csv
└── product_search.csv
```

PyTest parameterization is used to execute the same test logic against multiple data sets.

This allows the framework to scale test coverage without duplicating test functions.

For example:

```text
Invalid Login Test
        │
        ├── Dataset 1
        └── Dataset 2

Product Search Test
        │
        ├── Dataset 1
        ├── Dataset 2
        └── Dataset 3
```

---

# 🧪 3. PyTest and unittest

The capstone demonstrates both major Python testing approaches used in the training.

### PyTest

The PyTest implementation provides:

- Fixtures
- Parameterization
- Markers
- Centralized browser setup
- Automated test execution
- Failure diagnostics
- HTML reporting

### unittest

A separate product-search implementation demonstrates the Python `unittest` framework.

The comparison provides practical understanding of how the same automation objective can be implemented using different testing frameworks.

---

# ⚙️ 4. Centralized Test Setup

The framework uses `conftest.py` to centralize browser and test-environment setup for PyTest.

Responsibilities include:

- Browser initialization
- Browser configuration
- Headless execution support
- Implicit wait configuration
- Application launch
- Test cleanup
- Failure screenshot capture
- Execution logging

This avoids repeating common setup and teardown logic in individual test files.

---

# 🔍 5. Failure Diagnostics

The framework includes automated screenshot capture for failed PyTest executions.

```text
screenshots/
└── failures/
    ├── test_invalid_login[data0].png
    └── test_product_search.png
```

When a test fails, the framework captures a screenshot and records the relevant failure information in the logs.

This provides visual evidence that can help diagnose UI automation failures.

---

# 📸 6. Successful Execution Evidence

Successful test executions are also documented separately from failure diagnostics.

```text
screenshots/
├── evidence/
│   ├── test_invalid_login_data0.png
│   ├── test_invalid_login_data1.png
│   ├── test_product_search_product_data0.png
│   ├── test_product_search_product_data1.png
│   ├── test_product_search_product_data2.png
│   └── test_product_search_using_unittest.png
│
└── failures/
    ├── test_invalid_login[data0].png
    └── test_product_search.png
```

The distinction between `evidence/` and `failures/` makes the test artifacts easier to understand and review.

---

# 🛠️ 7. Real-World Automation Challenge

During product-search automation, the application displayed a Google Vignette advertisement overlay that interfered with Selenium interactions.

The framework was enhanced to handle this situation through a dedicated page-level method.

The solution considers:

- Advertisement iframe detection
- Nested iframe handling
- Dismiss controls
- Browser navigation fallback
- Page-level encapsulation

This demonstrates an important practical aspect of UI automation: automation frameworks must be capable of dealing with dynamic and unexpected browser/application behavior rather than relying only on ideal execution conditions.

---

# 🧾 8. Test Scenarios

The current capstone suite contains six automated test executions:

| Test Area | Framework | Coverage |
|---|---|---|
| Invalid Login | PyTest | 2 parameterized datasets |
| Product Search | PyTest | 3 parameterized datasets |
| Product Search | unittest | 1 test |
| **Total** | **PyTest + unittest** | **6 test executions** |

The PyTest suite uses parameterization to improve coverage while keeping the underlying test logic reusable.

---

# 📈 Expected Test Execution

The primary PyTest execution can be performed from the capstone project directory using:

```bash
pytest -v
```

The framework is designed to execute the automated tests, collect results, generate reporting artifacts, capture failure evidence where required, and close the browser cleanly after execution.

---

# 📑 Reporting

The framework includes support for HTML-based test reporting.

Reporting provides a convenient way to review:

- Test names
- Test outcomes
- Execution details
- Failed tests
- Test metadata
- Execution summaries

Reports are maintained separately from source code so that generated artifacts do not interfere with the framework implementation.

---

# 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python 3.13.7** | Programming language |
| 🌐 **Selenium WebDriver** | Browser automation |
| 🧪 **PyTest 9.1.1** | Test framework |
| 🔬 **unittest** | Python unit testing framework |
| 📊 **pytest-html 4.2.0** | HTML test reporting |
| 📝 **pytest-metadata 3.1.1** | Test metadata |
| 📄 **CSV** | External test data |
| 🏗️ **POM** | Page abstraction and maintainability |
| ⚙️ **Config-driven setup** | Environment configuration |
| 📋 **Logging** | Execution and diagnostic information |

---

# 🔄 Automation Flow

```text
                ┌─────────────────────┐
                │   Test Data / CSV   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     Test Layer      │
                │  PyTest / unittest  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Page Objects     │
                │   Login / HomePage  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Selenium WebDriver│
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Automation Exercise │
                │   Application Under │
                │        Test         │
                └──────────┬──────────┘
                           │
                           ▼
          ┌─────────────────────────────────┐
          │ Reports • Logs • Screenshots    │
          │ Evidence • Failure Diagnostics  │
          └─────────────────────────────────┘
```

---

# 🎓 Learning Outcomes

Through the training and capstone implementation, the project demonstrates practical understanding of:

- Python automation fundamentals
- Selenium WebDriver
- Web element identification
- Browser automation
- Explicit automation architecture
- PyTest
- unittest
- Fixtures and test lifecycle management
- Parameterized testing
- Page Object Model
- Data-driven automation
- Configuration management
- Logging
- Failure diagnostics
- Screenshot-based evidence
- HTML reporting
- REST API automation concepts
- BDD concepts
- Robot Framework concepts
- Maintainable automation framework design

---

# 📜 3. Certificates

The `Certificates/` directory contains the certificates associated with the completed training.

```text
Certificates/
├── Certificate_1
├── Certificate_2
└── Certificate_3
```

These certificates provide supporting evidence of the course and learning completed alongside the practical work documented in this repository.

---

# 🗺️ Training Journey

```text
Python Automation Fundamentals
              │
              ▼
       Selenium WebDriver
              │
              ▼
       Unit Test Frameworks
       ┌──────┴───────┐
       ▼              ▼
    unittest         PyTest
                       │
                       ▼
              Page Object Model
                       │
                       ▼
              Data-Driven Testing
                       │
                       ▼
         REST API + BDD Concepts
                       │
                       ▼
              Robot Framework
                       │
                       ▼
             Practical Capstone
                       │
                       ▼
        Reports • Logs • Evidence
```

---

# 🧠 Engineering Focus

The overall work emphasizes the transition from basic automation scripts to a structured automation framework.

| Area | Engineering Focus |
|---|---|
| **Maintainability** | Page Object Model and reusable utilities |
| **Scalability** | Parameterized and data-driven tests |
| **Reliability** | Waits, exception handling and centralized setup |
| **Diagnostics** | Logs and failure screenshots |
| **Reporting** | HTML test execution reports |
| **Reusability** | Shared fixtures, page methods and utilities |
| **Organization** | Clear separation of tests, pages, data and utilities |
| **Practicality** | Handling real browser/application interruptions |

---

# 📌 Repository Navigation

### 📁 `Certificates/`

Training certificates and supporting credentials.

### 📁 `Initial_Lab_Work/`

Module-wise lab report covering the four major areas of the Python Automation training.

### 📁 `Rhythm_Saha_Capstone_Project/`

Complete automation framework containing the implementation, test cases, test data, utilities, configuration, reports, screenshots and detailed project documentation.

---

# 🔮 Future Scope

The framework can be extended further with additional automation capabilities such as:

- More functional test scenarios
- Cross-browser execution
- Expanded API automation
- Additional data-driven test suites
- Advanced reporting
- Parallel execution
- CI/CD integration
- Remote browser execution
- More comprehensive failure diagnostics
- Additional reusable page components
- Broader regression coverage

---

# 🏁 Conclusion

This repository represents a structured progression through **Python Automation Course**, beginning with module-level laboratory work and extending to the implementation of a practical Selenium automation framework.

The work combines automation fundamentals with framework-oriented practices such as **Page Object Model, PyTest fixtures, data-driven testing, configuration management, logging, reporting and execution evidence**.

The repository is organized to make the learning journey, implementation approach and resulting automation artifacts easy to review and understand.

---

## 👤 Author

**Rhythm Saha**

**B.Tech CSE (IOT-CSBT)**

Enrollment No. **12023052017065**

---

<p align="center">
  <strong>Python Automation • Selenium • PyTest • POM • API Automation • BDD • Robot Framework</strong>
</p>

<p align="center">
  <em>Learning → Implementing → Automating → Improving</em>
</p>

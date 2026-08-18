# Enterprise Human Resource Management System (HRMS)

[![Enterprise HRMS CI](https://github.com/manognakm123/Enterprise-HRMS/actions/workflows/tests.yml/badge.svg)](https://github.com/manognakm123/Enterprise-HRMS/actions/workflows/tests.yml)

A full-stack Human Resource Management System built with **Python and Flask**, supported by a structured **test automation framework** using **Playwright, PyTest, REST API automation, SQLite database validation, and HTML test reporting**.

The project demonstrates end-to-end software testing across the **UI, API, database, and integration layers**, with automated execution through **GitHub Actions CI/CD**.

---

## Project Overview

The Enterprise HRMS application provides employee management functionality through a Flask-based web application.

The project includes a maintainable automation framework following the **Page Object Model (POM)** design pattern. The framework validates application functionality at multiple levels:

* UI automation
* REST API automation
* Database validation
* UI + API + Database integration testing
* Automated HTML test reporting
* Continuous Integration using GitHub Actions

---

## Project Status

### CI Validation — Successful

The latest GitHub Actions CI execution successfully completed:

| Result        |       Count |
| ------------- | ----------: |
| Total Tests   |          19 |
| Passed        |          19 |
| Failed        |           0 |
| Skipped       |           0 |
| Errors        |           0 |
| Test Duration | ~26 seconds |

The CI pipeline automatically:

1. Checks out the source code
2. Sets up Python
3. Installs project dependencies
4. Installs Playwright browsers
5. Creates the SQLite database
6. Verifies database tables and data
7. Starts the Flask application
8. Performs an API health check
9. Executes the complete PyTest suite
10. Generates an HTML test report
11. Uploads the HTML report as a GitHub Actions artifact

---

## Key Features

### HRMS Application

* User authentication/login
* Employee management
* Add employee
* Search employee
* Edit employee
* Delete employee
* Employee data persistence using SQLite
* REST API endpoints for employee operations

### Automation Framework

* Playwright-based UI automation
* PyTest test execution
* Page Object Model (POM)
* REST API automation using Requests
* SQLite database validation
* UI + API + Database integration testing
* CSV-based test data management
* Centralized configuration
* Logging
* PyTest markers
* HTML test reporting
* GitHub Actions CI/CD

---

## Technology Stack

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python 3.13           | Programming language      |
| Flask 3.1.3           | Web application framework |
| Playwright            | UI automation             |
| PyTest 9.1.1          | Test automation framework |
| Requests              | REST API automation       |
| SQLite                | Database                  |
| pytest-html 4.2.0     | HTML test reporting       |
| pytest-metadata 3.1.1 | Test environment metadata |
| Git                   | Version control           |
| GitHub                | Source code repository    |
| GitHub Actions        | Continuous Integration    |

---

## Automation Framework Architecture

The framework follows a layered architecture to separate application interaction, test logic, API communication, and database validation.

```text
                         Enterprise HRMS
                               |
              +----------------+----------------+
              |                |                |
              v                v                v
          UI Layer         API Layer       Database Layer
              |                |                |
         Playwright         Requests          SQLite
              |                |                |
              v                v                v
        Page Objects       API Client      DB Helpers
              |                |                |
              +----------------+----------------+
                               |
                               v
                            PyTest
                               |
                               v
                         Test Reporting
                               |
                               v
                        GitHub Actions CI
```

---

## Page Object Model

The UI automation framework follows the **Page Object Model (POM)** design pattern.

Page-specific actions and locators are separated from test cases.

Example:

```text
LoginPage
    |
    +-- Enter username
    +-- Enter password
    +-- Click login
    +-- Verify login

DashboardPage
    |
    +-- Open Employee Management

EmployeePage
    |
    +-- Search employee
    +-- Verify employee

AddEmployeePage
    |
    +-- Add employee

EditEmployeePage
    |
    +-- Edit employee

DeleteEmployeePage
    |
    +-- Delete employee
```

This improves:

* Maintainability
* Reusability
* Readability
* Separation of concerns
* Locator management

---

## Project Structure

```text
Enterprise-HRMS/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── automation_framework/
│   │
│   ├── api/
│   │   ├── api_client.py
│   │   └── endpoints.py
│   │
│   ├── config/
│   │   └── config.py
│   │
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── dashboard_page.py
│   │   ├── employee_page.py
│   │   ├── add_employee_page.py
│   │   ├── edit_employee_page.py
│   │   └── delete_employee_page.py
│   │
│   ├── tests/
│   │   ├── test_add_employee.py
│   │   ├── test_api_create_employee.py
│   │   ├── test_api_delete_employee.py
│   │   ├── test_api_get_employee.py
│   │   ├── test_api_get_employees.py
│   │   ├── test_api_update_employee.py
│   │   ├── test_database_connection.py
│   │   ├── test_delete_employee.py
│   │   ├── test_edit_employee.py
│   │   ├── test_employee_exists.py
│   │   ├── test_get_employee.py
│   │   ├── test_launch_hrms.py
│   │   ├── test_login.py
│   │   ├── test_search_employee.py
│   │   └── test_ui_api_integration.py
│   │
│   ├── test_data/
│   │   ├── delete_employee.csv
│   │   ├── edit_employee.csv
│   │   └── login_data.csv
│   │
│   ├── utilities/
│   │   ├── csv_reader.py
│   │   └── database_helper.py
│   │
│   └── logs/
│
├── database/
│   └── create_database.py
│
├── docs/
│
├── hrms_app/
│   ├── app.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── employees.html
│   │   ├── add_employee.html
│   │   └── edit_employee.html
│   │
│   └── static/
│       └── style.css
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

> Generated reports, logs, databases, Python cache files, and the virtual environment are excluded from version control through `.gitignore`.

---

## Test Coverage

The automation suite currently contains **19 automated tests** covering UI, API, database, and integration functionality.

### UI Tests

* Application launch
* Login validation
* Employee search
* Add employee
* Edit employee
* Delete employee

### API Tests

* Get all employees
* Get employee by ID
* Get invalid employee
* Create employee
* Update employee
* Delete employee

### Database Tests

* Database connection
* Employee existence validation
* Employee data retrieval
* Database validation after UI operations

### Integration Tests

* UI + API + Database integration

---

## Test Execution

The project uses PyTest as the primary test execution framework.

### Run all tests

```bash
pytest
```

### Run the complete automation suite directly

```bash
pytest automation_framework/tests -v -s
```

### Run UI tests

```bash
pytest -m ui
```

### Run API tests

```bash
pytest -m api
```

### Run database tests

```bash
pytest -m database
```

### Run integration tests

```bash
pytest -m integration
```

### Run smoke tests

```bash
pytest -m smoke
```

### Run regression tests

```bash
pytest -m regression
```

---

## HTML Test Reporting

HTML reporting is configured using `pytest-html`.

Running:

```bash
pytest
```

generates the local report:

```text
automation_framework/reports/report.html
```

The CI pipeline generates a separate report:

```text
reports/test_report.html
```

The CI report is uploaded automatically as a GitHub Actions artifact.

### Latest CI Report

```text
19 Tests
19 Passed
0 Failed
0 Skipped
0 Errors
```

---

## CI/CD Pipeline

GitHub Actions is configured to automatically execute the automation suite whenever code is pushed to the `main` branch or a pull request is created against `main`.

### CI Workflow

```text
Developer Push
      |
      v
GitHub Repository
      |
      v
GitHub Actions
      |
      v
Checkout Repository
      |
      v
Setup Python 3.13
      |
      v
Install Dependencies
      |
      v
Install Playwright
      |
      v
Create SQLite Database
      |
      v
Verify Database
      |
      v
Start Flask Application
      |
      v
Flask Health Check
      |
      v
API Health Check
      |
      v
Run 19 PyTest Tests
      |
      v
Generate HTML Report
      |
      v
Upload Report Artifact
      |
      v
CI Result
```

---

## GitHub Actions Workflow

The CI workflow is located at:

```text
.github/workflows/tests.yml
```

The workflow uses:

* `actions/checkout`
* `actions/setup-python`
* `actions/upload-artifact`
* Python 3.13
* Playwright
* PyTest
* pytest-html

The workflow also handles the Flask application's lifecycle during CI execution by:

1. Starting the Flask application as a background process
2. Waiting for the application to become available
3. Checking the application endpoint
4. Checking the employee API endpoint
5. Running the automation suite
6. Displaying Flask logs
7. Stopping the Flask process after execution

---

## Database Validation

The project uses SQLite for persistence.

The CI pipeline automatically creates the database using:

```bash
python database/create_database.py
```

The pipeline then verifies:

* Required database tables exist
* Users table contains data
* Employees table contains data
* Database connection works correctly

This prevents the automation suite from running against an incorrectly initialized database.

---

## Test Data Management

CSV files are used for data-driven testing.

Current test data includes:

```text
automation_framework/test_data/
├── login_data.csv
├── edit_employee.csv
└── delete_employee.csv
```

This allows test data to be maintained separately from test logic.

---

## Configuration Management

Centralized configuration is maintained through:

```text
automation_framework/config/config.py
```

Configuration includes values such as:

* Application base URL
* Browser
* Execution mode
* Timeout settings
* Test credentials

Sensitive credentials should be stored outside source control using environment variables or CI secrets.

---

## Logging

The framework includes logging to help troubleshoot test execution and application behavior.

Generated logs are intentionally excluded from Git version control.

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Enterprise-HRMS
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Git Bash:

```bash
source venv/Scripts/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright browsers

```bash
playwright install
```

---

## Running the HRMS Application

Create the database:

```bash
python database/create_database.py
```

Start the Flask application:

```bash
python hrms_app/app.py
```

The application runs locally at:

```text
http://127.0.0.1:5000
```

---

## Running the Automation Framework

With the Flask application running:

```bash
pytest
```

Or:

```bash
pytest automation_framework/tests -v -s
```

The HTML report will be generated automatically according to the configuration in `pytest.ini`.

---

## Git Workflow

The project follows a basic Git workflow:

```text
Create / Modify Code
       |
       v
Run Tests Locally
       |
       v
git status
       |
       v
git add
       |
       v
git commit
       |
       v
git push
       |
       v
GitHub Actions
       |
       v
Automated Tests
       |
       v
CI Report
```

---

## Quality and Maintainability

The framework was designed with maintainability and scalability in mind through:

* Page Object Model
* Centralized configuration
* Reusable API client
* Database helper utilities
* Data-driven testing
* PyTest markers
* Separation of UI, API, and database tests
* Automated CI execution
* HTML reporting
* Git version control

---

## Future Enhancements

Potential future improvements include:

* Cross-browser execution with Chromium, Firefox, and WebKit
* Parallel test execution
* Test retry mechanism
* Screenshot capture on UI test failure
* Trace/video capture for failed Playwright tests
* API schema validation
* Docker-based test execution
* Multi-version Python CI matrix
* Test result notifications
* Advanced CI/CD deployment pipeline
* Allure reporting
* Cloud-based browser execution

---

## Project Highlights

This project demonstrates an end-to-end automation testing workflow covering:

```text
Python
  |
  +-- Flask Web Application
  |
  +-- Playwright UI Automation
  |
  +-- PyTest
  |
  +-- REST API Automation
  |
  +-- SQLite Database Validation
  |
  +-- Page Object Model
  |
  +-- Data-Driven Testing
  |
  +-- Integration Testing
  |
  +-- Git & GitHub
  |
  +-- GitHub Actions CI/CD
  |
  +-- HTML Test Reporting
```

### Latest Verified Result

**19/19 automated tests passed successfully in GitHub Actions CI.**

---

## Author

**Enterprise HRMS Automation Framework**

Built as an end-to-end software testing and CI/CD project demonstrating UI, API, database, integration, and continuous integration automation.

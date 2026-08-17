# Enterprise HR Management System

A full-stack Human Resource Management System built with Python and Flask, with an enterprise-style test automation framework using Playwright, PyTest, REST API automation, SQLite database validation, and HTML test reporting.

## Project Overview

The Enterprise HR Management System (HRMS) provides employee management functionality through a web application.

The project also includes an automation framework designed to validate the application at multiple levels:

- UI automation
- REST API automation
- Database validation
- UI + API + Database integration
- Automated HTML test reporting

The framework follows the Page Object Model (POM) approach for maintainable UI automation.

---

## Key Features

### HRMS Application

- User login
- Employee management
- Add employee
- Search employee
- Edit employee
- Delete employee
- Employee data persistence using SQLite
- REST API endpoints for employee operations

### Test Automation Framework

- Playwright-based UI automation
- PyTest test execution
- Page Object Model (POM)
- REST API automation using `requests`
- SQLite database validation
- UI + API + Database integration testing
- Test data management
- Centralized configuration
- Logging
- HTML test reports
- PyTest markers for test categorization

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Programming language |
| Flask 3.1.3 | Web application |
| Playwright 1.61.0 | UI automation |
| PyTest 9.1.1 | Test framework |
| Requests 2.34.2 | REST API automation |
| SQLite | Database |
| pytest-html 4.2.0 | HTML test reporting |
| pytest-metadata 3.1.1 | Test metadata |
| Git | Version control |
| GitHub | Source code repository |

---

## Project Structure

```text
Enterprise-HRMS/
│
├── automation_framework/
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
│   │   ├── UI tests
│   │   ├── API tests
│   │   ├── Database tests
│   │   └── Integration tests
│   │
│   ├── utilities/
│   │   ├── csv_reader.py
│   │   └── database_helper.py
│   │
│   ├── test_data/
│   └── reports/
│
├── database/
│   └── Database-related files
│
├── docs/
│
├── hrms_app/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── test_logger.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
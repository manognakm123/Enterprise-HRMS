# Enterprise Human Resource Management System (HRMS)

A full-stack Human Resource Management System built using Python and Flask, with an enterprise-style test automation framework using Playwright, PyTest, REST API automation, SQLite database validation, and HTML test reporting.

---

## Project Overview

The Enterprise HRMS project provides employee management functionality through a Flask-based web application.

The project also includes a structured automation framework designed to validate the application at multiple levels:

- UI automation
- REST API automation
- Database validation
- UI + API + Database integration testing
- Automated HTML test reporting

The automation framework follows the **Page Object Model (POM)** approach to improve test maintainability, readability, and reusability.

---

## Project Status

**Completed and validated successfully**

- 19 automated test cases implemented
- 19/19 test cases passing
- UI automation implemented
- REST API automation implemented
- Database validation implemented
- UI + API + Database integration implemented
- HTML test reporting configured
- PyTest markers configured
- Centralized configuration implemented
- Logging implemented
- Test data management implemented

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
- REST API automation using Requests
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
| Flask 3.1.3 | Web application framework |
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
│   └── reports/
│       └── report.html
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
├── test_logger.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
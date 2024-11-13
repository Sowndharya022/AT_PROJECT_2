
# AT Project 2: OrangeHRM Employee Photo Management System

## Overview

The **OrangeHRM Employee Photo Management System** is a web-based application designed to manage employee photos. Employees can add or change their own photos, and Human Resources (HR) can add or change everyone's photos. The system produces lists of photos based on different selection criteria. These photos are integrated into various systems within the company. The photos are stored in a configurable file structure, and the location is referenced by a file system. This release only includes employee photos, as well as name, address, and social security information—not the other HR features planned for future releases.

## Features

- **Employee Login**: Employees can log into the system using their credentials.
- **HR Photo Management**: HR staff can manage photos for all employees in the system.
- **Employee Photo Lists**: Photos can be listed based on various selection criteria.
- **File System Integration**: Photos are stored in a configurable file structure that can be accessed by other systems in the company.

## Technologies Used

- **Python**: Backend scripting and automation testing.
- **Selenium**: WebDriver for automating interactions with the OrangeHRM web interface.
- **pytest**: Testing framework to run automated test cases.
- **Pandas**: For handling CSV data, including login credentials.
- **CSV**: For storing login test data.
- **Git**: Version control for source code management.
- **ChromeDriver**: For automated browser interactions during testing.

### Framework

- **Test Framework**: The project uses a **Data-Driven Testing** approach.
  - **Data-Driven Framework**: Test data is stored in CSV files (`data/login_data.csv`) and is fed into the tests to execute with different sets of inputs (login credentials).
  - **pytest** is used to handle the test execution, with each test running for multiple sets of data as provided by the CSV file.

## File Structure

```
AT-Project-2/
│
├── data/
│   └── login_data.csv           # Login credentials data file for tests
│
├── pages/
│   ├── base_page.py             # Base page object class with common methods
│   ├── login_page.py            # Page object for login functionality
│   ├── admin_page.py            # Page object for Admin page
│   └── menu_page.py             # Page object for Menu navigation
│
├── tests/
│   ├── conftest.py              # Pytest setup and screenshot capture logic
│   ├── test_login.py            # Test cases for login functionality
│   ├── test_admin.py            # Test cases for Admin page functionality
│   └── test_menu.py             # Test cases for Menu page navigation
│
└── utils/
    └── result_writer.py         # Utility to update test results in CSV files
```

## Usage

### Running the Tests

To run the tests for the OrangeHRM Employee Photo Management System, use the following commands:

- **Login Test Cases**: These test cases verify valid and invalid login scenarios. The login credentials are fetched from the CSV file `data/login_data.csv`.

  To run the login tests:
  ```bash
  pytest tests/test_login.py
  ```

- **Admin Page Test Cases**: These test cases validate the header and functionality of the Admin page. This includes checking that all expected header options are displayed after logging in.

  To run the Admin page tests:
  ```bash
  pytest tests/test_admin.py
  ```

- **Menu Page Test Cases**: These test cases ensure that the correct menu options are displayed after logging in.

  To run the Menu page tests:
  ```bash
  pytest tests/test_menu.py
  ```

### Writing Test Results

Test results are saved in `data/test_result.csv` using the `update_test_result()` function from `utils/result_writer.py`.

---

## Test Cases

### Login Test Cases

- **TC_PIM_01**: **Forgot Password Link Validation on Login Page**  
  **Test Objective**: Verify that clicking on the "Forgot Password" link leads to a successful password reset message.  
  **Preconditions**:
  - Valid username exists.
  - OrangeHRM site is launched on a compatible browser.
  - Steps:
    1. Navigate to the login page.
    2. Click the "Forgot Password" link.
    3. Enter the username and click "Reset Password."
  - **Expected Result**: A success message appears: "Reset Password link sent successfully."

- **TC_PIM_02**: **Admin Page Header Validation**  
  **Test Objective**: Verify that all expected header options are displayed on the Admin page after logging in as "Admin".  
  **Preconditions**:
  - Valid "Admin" account available.
  - OrangeHRM site is launched in a compatible browser.
  - Steps:
    1. Login as "Admin."
    2. Navigate to the Admin page.
    3. Validate that the following options are displayed:
      - User Management
      - Job
      - Organization
      - Qualifications
      - Nationalities
      - Corporate Branding
      - Configuration
  - **Expected Result**: All the listed options are displayed as headers.

- **TC_PIM_03**: **Menu Page Item Validation**  
  **Test Objective**: Verify that the correct menu items are visible after logging into the system.  
  **Preconditions**:
  - Valid "Admin" account available.
  - OrangeHRM site is launched in a compatible browser.
  - Steps:
    1. Login as "Admin."
    2. Navigate to the Menu page.
    3. Validate that the following menu items are displayed:
      - Admin
      - PIM
      - Leave
      - Time
      - Recruitment
      - My Info
      - Performance
      - Directory
      - Maintenance
      - Buzz
  - **Expected Result**: All the listed menu options are displayed correctly.

---

## Conclusion

This repository provides a comprehensive implementation of the **OrangeHRM Employee Photo Management System**. It includes test cases for login functionality, Admin page header validation, and menu page item validation. The automation scripts, utilizing **Selenium** for web interaction and **pytest** for running the tests, ensure that the system works as expected.


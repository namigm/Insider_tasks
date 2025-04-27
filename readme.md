# Task for Insider Company

This project contains automated UI and API tests for Insider's platform, along with additional assignments in a separate folder. The project utilizes Python, Selenium, Page Object Model (POM), and the Requests library for API testing.

## Table of Contents
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Configuration](#configuration)
- [Test Structure](#test-structure)
- [Known Issues](#known-issues)


## Installation

1. **Create a Virtual Environment**:
    - Create a virtual environment:
      ```bash
      python3 -m venv venv
      ```

2. **Activate the Virtual Environment**:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

3. **Install Dependencies**:
    - Install all required libraries using:
      ```bash
      pip install -r requirements.txt
      ```

4. **Set up Environment Variables**:
    - Ensure your `.env` file is configured with the necessary variables, such as base URLs, authentication tokens, etc.

## Running Tests

1. **Run UI and API Tests**:
    - You can run the tests with `pytest` command:
      ```bash
      pytest
      ```

2. **Run Tests for Specific Browser**:
    - Since browser is parametrically changeable, use the `-k` flag to specify the browser:
      - For Chrome:
        ```bash
        pytest -k "chrome"
        ```
      - For Firefox:
        ```bash
        pytest -k "firefox"
        ```

    This flag will make sure that the browser is selected based on the parameter passed during the test run.

3. **Running Tests for a Specific Module/Folder**:
    - To run tests from a specific file or folder:
      ```bash
      pytest path_to_your_test_file_or_folder
      ```

## Configuration

The project supports browser configuration using `pytest` flags. The following configuration allows you to switch between different browsers (Chrome or Firefox):

- **Chrome**: To run tests with Chrome, you need to use the `-k "chrome"` flag.
- **Firefox**: Similarly, to use Firefox, use the `-k "firefox"` flag.



## Test Structure

- **UI Tests**: These tests are located in the `ui_tests` folder. They interact with the platform’s user interface via Selenium and follow the Page Object Model (POM) design pattern.
  
- **API Tests**: These tests are located in the `api_tests` folder. The tests use the `requests` library to send HTTP requests to the API and validate the responses.

- **Additional Tasks**: There are two additional tasks that involve answering questions and are located in a different folder. The answers are provided in text files and a file containing the responses.

## Known Issues

1. **Environment Limitation**:
    - `pytest-order` is used due to environment limitations. 
  
2. **GitHub and `.env`**:
    - The `.env` file is included in the GitHub repository for convenience. However, **do not** commit your sensitive information to the repository.

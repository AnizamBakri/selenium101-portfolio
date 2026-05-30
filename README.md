# Selenium Portfolio — Python Test Suite

Automated UI test suite built with Selenium WebDriver and pytest,
following the Page Object Model design pattern.

## Tech Stack
- Python 3.13
- Selenium 4
- pytest

## Project Structure
pages/       - Page Object classes
tests/       - pytest test files
conftest.py  - shared driver fixture

## How to Run
pip install -r requirements.txt
pytest -v

## Test Coverage
- Dynamic loading — explicit waits, visibility conditions
- Login — form interaction, positive and negative test cases
- Checkboxes — state assertion, pre/post conditions, negative testing
# Overview
This project tests the User Registration, User Login, View Account balance, Transfer funds, and Logout endpoints using the python unittest.
The test cases cover both positive and negative scenarios, ensuring proper validation of authentication, authorization, and error handling.

# Assumptions
The API requires a valid JWT token for authorization, and it follows the Bearer token format.
The status codes returned are consistent with standard HTTP responses (200, 401, 403, and 404).

# File Structure
test_account_balance.py: Contains the test cases for the balance retrieval API, along with mocked responses.
test_transfer_funds.py: Contains the test cases for the balance retrieval API, along with mocked responses.
test_user_login.py: Contains the test cases for the balance retrieval API, along with mocked responses.
test_user_logout.py: Contains the test cases for the balance retrieval API, along with mocked responses.
test_user_registration.py: Contains the test cases for the balance retrieval API, along with mocked responses.

# How to run test files

- Download the project folder
- Run `pip install -r requirements.txt`
- Run each test file with `python filename.py`

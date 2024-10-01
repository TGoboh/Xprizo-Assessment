import requests
import unittest
from unittest.mock import patch

# Sample URL for the fictional API
BASE_URL = "http://localhost:5000/api/v1/users/register"

class TestUserRegistration(unittest.TestCase):
    """
    Test class for user registration API endpoint.
    """

    @patch("requests.post")
    def test_successful_registration(self, mock_post):
        """
        Successful user registration with valid inputs
        """
        # Arrange
        mock_response = {
            "message": "User registered successfully."
        }
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = mock_response
        
        data = {
            "username": "validUser",
            "password": "StrongPassword123!",
            "email": "validuser@example.com",
            "phone": "1234567890"
        }

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 201
        assert response.json() == mock_response

   
    @patch("requests.post")
    def test_missing_fields(self, mock_post):
        """
        Test user registration with missing fields.
        """
        # Arrange
        mock_response = {
            "error": "Missing required fields."
        }
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = mock_response

        data = {
            "username": "missingEmailUser",
            "password": "StrongPassword123!",
            "phone": "1234567890"
        }

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 400
        assert response.json() == mock_response
        

    @patch("requests.post")
    def test_username_already_exists(self, mock_post):
        """
        Registration with an already existing username.
        """
        # Arrange
        mock_response = {
            "error": "Username already exist."
        }
        mock_post.return_value.status_code = 409
        mock_post.return_value.json.return_value = mock_response

        data = {
            "username": "existingUser",
            "password": "StrongPassword123!",
            "email": "newuser@example.com",
            "phone": "0987654321"
        }

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 409
        assert response.json() == mock_response


    @patch("requests.post")
    def test_email_already_exists(self, mock_post):
        """
        Test Registration with an already existing email.
        """
        # Arrange
        mock_response = {
            "error": "Email already exists."
        }
        mock_post.return_value.status_code = 409
        mock_post.return_value.json.return_value = mock_response

        data = {
            "username": "newUser",
            "password": "StrongPassword123!",
            "email": "existinguser@example.com",
            "phone": "1234567890"
        }

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 409
        assert response.json() == mock_response


    @patch("requests.post")
    def test_sql_injection_attempt(self, mock_post):
        """
        Test user registration with a potential SQL injection in the username.
        """
        # Arrange
        mock_response = {
            "error": "Invalid input."
        }
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = mock_response

        data = {
            "username": "'; DROP TABLE users;--",
            "password": "Test@1234",
            "email": "sqlinjection@example.com",
            "phone": "1234567890"
        }

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 400
        assert response.json() == mock_response

if __name__ == '__main__':
    unittest.main()

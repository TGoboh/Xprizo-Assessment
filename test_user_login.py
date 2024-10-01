import requests
import unittest
from unittest.mock import patch

# Sample URL for the fictional API
BASE_URL = "http://localhost:5000/api/v1/users/login"

class TestUserLogin(unittest.TestCase):
    """
    Test class for user login API endpoint.
    """

    @patch("requests.post")
    def test_successful_login(self, mock_post):
        """
        User with valid credentials can successfully log in and receive a JWT token.
        """
        # Arrange
        mock_response = {
            "message": "Bearer eyJowiwnbwcibyuYtt78786667987rfghhjHtutdRdr6EDFFFffagahahaq"
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response
        
        data = {
             "username": "testUser",
             "password": "testPassword"
        }

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 200
        assert response.json() == mock_response

   
    @patch("requests.post")
    def test_username_incorrect(self, mock_post):
        """
        Test Login failure when username is incorrect.
        """
        # Arrange
        mock_response = {
            "error": "Invalid credentials"
        }
        mock_post.return_value.status_code = 401
        mock_post.return_value.json.return_value = mock_response

        data = {
            "username": "invalidUser",
            "password": "testPassword"
        }


        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 401
        assert response.json() == mock_response
        

    @patch("requests.post")
    def test_password_incorrect(self, mock_post):
        """
        Test Login failure when password is incorrect
        """
        # Arrange
        mock_response = {
            "error": "Invalid credentials"
        }
        mock_post.return_value.status_code = 401
        mock_post.return_value.json.return_value = mock_response

        data = {
            "username": "testUser",
            "password": "wrongPassword"
        }

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 401
        assert response.json() == mock_response


    @patch("requests.post")
    def test_password_missing(self, mock_post):
        """
        Test Login failure when the password is missing in the request body.
        """
        # Arrange
        mock_response = {
            "error": "Password field missing"
        }
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = mock_response

        data = {
             "username": "testUser"
        }

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 400
        assert response.json() == mock_response

if __name__ == '__main__':
    unittest.main()

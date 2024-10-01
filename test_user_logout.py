import requests
import unittest
from unittest.mock import patch

# Sample URL for the fictional API
BASE_URL = "http://localhost:5000/api/v1/users/logout"

class TestUserLogout(unittest.TestCase):
    """
    Test class for logout API endpoint.
    """

    @patch("requests.post")
    def test_successful_logout(self, mock_post):
        """
        Test Successful logout for a valid user session
        """
        # Arrange
        mock_response = {
            "message": "Logout successful"
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response
        
        

        # Act
        response = requests.post(BASE_URL, headers={"Authorization": "Bearer valid_token"})

        # Assert
        assert response.status_code == 200
        assert response.json() == mock_response

   
    @patch("requests.post")
    def test_unsuccessful_logout(self, mock_post):
        """
        Test Logout attempt without token.
        """
        # Arrange
        mock_response = {
            "message": "Authorization required"
        }
        mock_post.return_value.status_code = 401
        mock_post.return_value.json.return_value = mock_response
        
        

        # Act
        response = requests.post(BASE_URL)

        # Assert
        assert response.status_code == 401
        assert response.json() == mock_response


    @patch("requests.post")
    def test_unsuccessful_logout_with_invalid_token(self, mock_post):
        """
        Test Logout attempt with invalid token.
        """
        # Arrange
        mock_response = {
            "message": "Invalid token"
        }
        mock_post.return_value.status_code = 401
        mock_post.return_value.json.return_value = mock_response
        
        

        # Act
        response = requests.post(BASE_URL, headers={"Authorization": "Bearer invalid_token"})
       
        # Assert
        assert response.status_code == 401
        assert response.json() == mock_response

if __name__ == '__main__':
    unittest.main()
   
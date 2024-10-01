import requests
import unittest
from unittest.mock import patch

# Sample URL for the fictional API
BASE_URL = "http://localhost:5000/api/v1/accounts/transfer"

class TestTransferFunds(unittest.TestCase):
    """
    Test class for fund transfer API endpoint.
    """

    @patch("requests.post")
    def test_successful_fund_transfer(self, mock_post):
        """
        Test Successful transfer of funds between two valid accounts with sufficient balance..
        """
        # Arrange
        mock_response = {
            "message": "Transfer successful"
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response
        
        data = {
             "from_account_id": 12345,
             "to_account_id": 67890,
             "amount": 100.50

        }, 
        headers={"Authorization": "Bearer valid_token"}

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 200
        assert response.json() == mock_response

   
    @patch("requests.post")
    def test_insufficient_funds(self, mock_post):
        """
        Test Transfer failure due to insufficient funds in from_account_id
        """
        # Arrange
        mock_response = {
            "message": "Insufficient funds"
        }
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = mock_response
        
        data = {
             "from_account_id": 12345,
             "to_account_id": 67890,
             "amount": 1000.00
        }, 
        headers={"Authorization": "Bearer valid_token"}


        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 400
        assert response.json() == mock_response


    @patch("requests.post")
    def test_unauthorized_access(self, mock_post):
        """
        Test Unauthorized access attempt due to missing token.
        """
        # Arrange
        mock_response = {
            "message": "Authorization required"
        }
        mock_post.return_value.status_code = 401
        mock_post.return_value.json.return_value = mock_response
        
        data = {
             "from_account_id": 12345,
             "to_account_id": 67890,
             "amount": 100.50
        }, 

        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 401
        assert response.json() == mock_response


    @patch("requests.post")
    def test_non_existing_account(self, mock_post):
        """
        Test Transfer attempt with a non-existent from account
        """
        # Arrange
        mock_response = {
            "message": "Account not found"
        }
        mock_post.return_value.status_code = 404
        mock_post.return_value.json.return_value = mock_response
        
        data = {
             "from_account_id": 99999,
             "to_account_id": 67890,
             "amount": 50.00
        }, 
        headers={"Authorization": "Bearer valid_token"}


        # Act
        response = requests.post(BASE_URL, json=data)

        # Assert
        assert response.status_code == 404
        assert response.json() == mock_response

if __name__ == '__main__':
    unittest.main()

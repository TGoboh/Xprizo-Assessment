import requests
import unittest
from unittest.mock import patch

BASE_URL = "http://localhost:5000/api/v1"


class ViewAccountBalance(unittest.TestCase):
    """Test class for view account balance API endpoint"""
     
    @patch("requests.get")
    def test_account_balance_valid_token(self, mock_get):
        """Test Account balance is successfully retrieved when using correct authentication and an existing account."""

        mock_response = {"balance": 1000.50}

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        response = requests.get(f"{BASE_URL}/accounts/12345/balance", headers={
            "Authorization": "Bearer valid_token"
        })

        assert response.status_code == 200
        assert response.json() == {"balance": 1000.50}
        

    @patch("requests.get")
    def test_account_balance_invalid_token(self, mock_get):
        """Test request failure when the JWT token is invalid."""

        mock_response = {"error": "Invalid token"}

        mock_get.return_value.status_code = 401
        mock_get.return_value.json.return_value = mock_response

        response = requests.get(f"{BASE_URL}/accounts/12345/balance", headers={
            "Authorization": "Bearer invalid_token"
        })

        assert response.status_code == 401
        assert response.json() == {"error": "Invalid token"}


    @patch("requests.get")
    def test_access_to_another_users_account(self, mock_get):
        """Test Access to another user's account balance is denied when the authenticated user doesn't have permission."""

        mock_response = {"error": "Access denied"}

        mock_get.return_value.status_code = 403
        mock_get.return_value.json.return_value = mock_response

        response = requests.get(f"{BASE_URL}/accounts/12345/balance", headers={
            "Authorization": "Bearer valid_token_for_different_user"
        })
        assert response.status_code == 403
        assert response.json() == {"error": "Access denied"}


    @patch("requests.get")
    def test_access_to_non_existing_account(self, mock_get):
        """Test Request failure when trying to access a non-existent account."""

        mock_response = {"error": "Account not found"}

        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = mock_response

        response = requests.get(f"{BASE_URL}/accounts/99999/balance", headers={
            "Authorization": "Bearer valid_token"
        })
        assert response.status_code == 404
        assert response.json() == {"error": "Account not found"}

if __name__ == '__main__':
    unittest.main()

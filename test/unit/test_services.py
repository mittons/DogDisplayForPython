from requests.exceptions import ConnectionError, Timeout, HTTPError
import unittest
from unittest.mock import patch

from dog_app.services import DogBreedService


class DogBreedServiceGeneralTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize the external service with a dummy base URL
        self.external_service = DogBreedService("http://dummyurl")

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_data = [{'name': 'Shiba Inu', 'temperament': 'Friendly'}]

        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data

        # Call the method
        result = self.external_service.get_data()

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result, mock_data)

    @patch('requests.get')
    def test_get_data_failure_404_response(self, mock_get):
        # Mock a failed response
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        # Call the method
        result = self.external_service.get_data()

        # Assertions
        self.assertIsNone(result)

    @patch('requests.get')
    def test_get_data_connection_error(self, mock_get):
        # Simulate a ConnectionError
        mock_get.side_effect = ConnectionError

        # Call the method
        result = self.external_service.get_data()

        # Assertions
        self.assertIsNone(result)

    @patch('requests.get')
    def test_get_data_timeout(self, mock_get):
        # Simulate a Timeout
        mock_get.side_effect = Timeout

        # Call the method
        result = self.external_service.get_data()

        # Assertions
        self.assertIsNone(result)   

    @patch('requests.get')
    def test_get_data_http_error(self, mock_get):
        # Simulate an HTTPError
        mock_get.side_effect = HTTPError

        # Call the method
        result = self.external_service.get_data()

        # Assertions
        self.assertIsNone(result)

class DogBreedServiceSanitationTestCase(unittest.TestCase):
    def setUp(self):
        self.external_service = DogBreedService("http://dummyurl")
        self.unsafe_chars = ['|', '&', ';', '<', '>', '$', '`', '\\', '"']

    @patch('requests.get')
    def test_unsafe_character_rejection(self, mock_get):
        for char in self.unsafe_chars:
            with self.subTest(char=char):
                # Mocking a response containing the unsafe character
                mock_data = [{'name': 'Test' + char, 'temperament': 'Aggressive' + char}]
                mock_response = mock_get.return_value
                mock_response.status_code = 200
                mock_response.json.return_value = mock_data

                # Call the method
                result = self.external_service.get_data()

                # Assertions
                self.assertNotIn(char, str(result), "Unsafe character {} was not sanitized".format(char))


if __name__ == "__main__":
    unittest.main()
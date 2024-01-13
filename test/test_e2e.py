from requests.exceptions import ConnectionError, Timeout, HTTPError
import unittest
from flask import template_rendered
from contextlib import contextmanager

from dog_app import create_app
from unittest.mock import patch
from bs4 import BeautifulSoup


@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

class EndToEndTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

        self.client = self.app.test_client()
        self.client.testing = True

    def test_index_route(self):
        with captured_templates(self.app) as templates:
            # -----------------------------------------
            # Run code - Generate response for route
            # -----------------------------------------
            response = self.client.get('/')

            # -----------------------------------------
            # Observe result - make assertions
            # -----------------------------------------

            ## Verify routes source template
            self.assertEqual(templates[-1][0].name, 'dog_screen_init.html')

            # Test response
            ## Test response status code
            self.assertEqual(response.status_code, 200)

            ## Test response data - Structure and data placement
            test_initial_template_structure_and_data(self, response.data)
    
    @patch('requests.get')
    def test_dog_list_template_structure_and_data(self, mock_get):
        # -----------------------------------------
        # | Prepare dependencies for test
        # -----------------------------------------
        # | Mock data 
        mock_data = [{'name': 'Shiba Inu', 'temperament': 'Friendly'}, {'name': 'Pug', 'temperament': 'Happy'}, {'name': 'Retriever', 'temperament': 'Excited'}]
        # | Mock http response
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data

        with captured_templates(self.app) as templates:
            # -----------------------------------------
            # Run code - Generate response for route
            # -----------------------------------------
            response = self.client.get('/renderBreeds')

            # -----------------------------------------
            # Observe result - make assertions
            # -----------------------------------------

            ## Verify routes source template
            self.assertEqual(templates[-1][0].name, 'dog_breeds_partial.html')

            # Test response
            ## Test response status code
            self.assertEqual(response.status_code, 200)

            ## Test response data - Structure and data placement
            test_dog_list_template_structure_and_data(self, response.data, mock_data)

    @patch('requests.get')
    def test_get_data_failure_404_response(self, mock_get):
        # -----------------------------------------
        # | Prepare dependencies for test
        # -----------------------------------------
        # Mock a failed response
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        # -----------------------------------------
        # Run code - Generate response for route
        # -----------------------------------------        
        response = self.client.get('/renderBreeds')

        # -----------------------------------------
        # Observe result - make assertions
        # -----------------------------------------        
        self.assertEqual(response.status_code, 500)


    @patch('requests.get')
    def test_get_data_connection_error(self, mock_get):
        # -----------------------------------------
        # | Prepare dependencies for test
        # -----------------------------------------
        # Simulate a ConnectionError
        mock_get.side_effect = ConnectionError

        # -----------------------------------------
        # Run code - Generate response for route
        # -----------------------------------------       
        response = self.client.get('/renderBreeds')

        # -----------------------------------------
        # Observe result - make assertions
        # -----------------------------------------        
        self.assertEqual(response.status_code, 500)


    @patch('requests.get')
    def test_get_data_timeout(self, mock_get):
        # -----------------------------------------
        # | Prepare dependencies for test
        # -----------------------------------------
        # Simulate a Timeout
        mock_get.side_effect = Timeout

        # -----------------------------------------
        # Run code - Generate response for route
        # -----------------------------------------
        response = self.client.get('/renderBreeds')

        # -----------------------------------------
        # Observe result - make assertions
        # -----------------------------------------        
        self.assertEqual(response.status_code, 500)


    @patch('requests.get')
    def test_get_data_http_error(self, mock_get):
        # -----------------------------------------
        # | Prepare dependencies for test
        # -----------------------------------------
        # Simulate an HTTPError
        mock_get.side_effect = HTTPError

        # -----------------------------------------
        # Run code - Generate response for route
        # -----------------------------------------        
        response = self.client.get('/renderBreeds')

        # -----------------------------------------
        # Observe result - make assertions
        # -----------------------------------------        
        self.assertEqual(response.status_code, 500)


def test_initial_template_structure_and_data(unitTester, rendered_template):
    """
    Test the structure and data placement of the initial rendered landing page HTML template.

    This function verifies that the rendered template adheres to specific structural
    requirements towards the initially displayed elements. It uses BeautifulSoup
    to parse the rendered HTML and unittest assertions to validate the content.

    Args:
        unitTester (unittest.TestCase): The unit test case instance used for making assertions.
        rendered_template (str): The HTML content of the rendered template.

    The function performs the following checks:
    - Asserts the presence of specific HTML elements in initial state (e.g., '.header-bar', 'button').

    Example:
        test_initial_template_structure_and_data(self, response.data)
    """
    # ----------------------------
    # | Prepare test data
    # ----------------------------

    # Parse the rendered template
    soup = BeautifulSoup(rendered_template, 'html.parser')

    # ----------------------------
    # | Structure contract tests
    # ----------------------------

    # Test for structure
    ## - Header
    unitTester.assertTrue("Dog Diversity Galore! 🐶" in soup.select_one('.header-bar').text)

    ## - Request button
    unitTester.assertIsNotNone(soup.find('button', string=lambda text: "Get list of so many types of good dogs!" in text))
    

def test_dog_list_template_structure_and_data(unitTester, rendered_template, mock_data):
    """
    Test the structure and data placement of the partially rendered HTML data template.

    This function verifies that the rendered partial template adheres to specific structural
    requirements and correctly places data within this structure. It uses BeautifulSoup
    to parse the rendered HTML and unittest assertions to validate the content.

    Args:
        unitTester (unittest.TestCase): The unit test case instance used for making assertions.
        rendered_template (str): The HTML content of the rendered template.
        mock_data (list of dict): A list of dictionaries containing mock data used in the test.

    The function performs the following checks:
    - Verifies that each item in the mock data is correctly reflected in the HTML elements.
      This includes checks for the presence and correct placement of names and temperaments
      within the designated HTML elements.`

    Example:
        test_initial_template_structure_and_data(self, response.data, mock_data)
    """
    # ----------------------------
    # | Prepare test data
    # ----------------------------

    # Parse the rendered template
    soup = BeautifulSoup(rendered_template, 'html.parser')

    # ----------------------------
    # | Structure contract tests
    # ----------------------------

    # Test for structure

    ## - List of dog breeds
    unitTester.assertIsNotNone(soup.find('md-list'))

    unitTester.assertIsNotNone(soup.find('md-elevated-card'))
    div_slot_headline_elems = soup.find_all('div', {"slot": "headline"})

    div_slot_support_text_elems = soup.find_all('div', {"slot": "supporting-text"})


    # ----------------------------
    # | Data placement tests
    # ----------------------------

    # Loop through each item in mock_data and check for its presence in the rendered HTML
    for item in mock_data:
        # Find the corresponding divs for each item
        name_div = next(
            filter(
                lambda elem: item['name'] in elem.text, 
                div_slot_headline_elems), 
            None)

        temperament_div = next(
            filter(
                lambda elem: item['temperament'] in elem.text, 
                div_slot_support_text_elems), 
            None)
        
        # Test for data placement
        unitTester.assertIsNotNone(name_div)
        unitTester.assertIsNotNone(temperament_div)

if __name__ == "__main__":
    unittest.main()
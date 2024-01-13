import unittest
import sys

# Import test modules
from test import test_e2e
from test.unit import test_routes, test_services

def run_tests(test_module):
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_module))

    # Run the test suite and collect results
    result = unittest.TextTestRunner().run(suite)
    return result.wasSuccessful()

if __name__ == '__main__':
    # Running each test module as a separate suite
    results = []
    results.append(run_tests(test_e2e))
    results.append(run_tests(test_routes))
    results.append(run_tests(test_services))

    # Check if any of the test suites failed
    if not all(results):
        sys.exit(1)  # Exit with a non-zero status if any tests failed

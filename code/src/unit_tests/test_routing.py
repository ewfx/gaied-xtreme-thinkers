import unittest
from app import route_request

class TestRouting(unittest.TestCase):
    def test_route_request(self):
        classification_result = '{"Request Type": "Loan Adjustment"}'
        assigned_team = route_request(classification_result)
        self.assertIsInstance(assigned_team, str, "Routing failed")

if __name__ == '__main__':
    unittest.main()

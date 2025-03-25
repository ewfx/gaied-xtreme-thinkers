import unittest
from app import fetch_latest_email

class TestEmailFetch(unittest.TestCase):
    def test_fetch_latest_email(self):
        email_msg = fetch_latest_email()
        self.assertIsNotNone(email_msg, "Failed to fetch email")

if __name__ == '__main__':
    unittest.main()

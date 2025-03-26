import unittest
from app import classify_email

class TestEmailClassification(unittest.TestCase):
    def test_classify_email(self):
        sample_text = "This is a loan adjustment request."
        classification_result = classify_email(sample_text)
        self.assertIn("Request Type", classification_result, "Classification failed")

if __name__ == '__main__':
    unittest.main()

import unittest
from app import extract_data

class TestDataExtraction(unittest.TestCase):
    def test_extract_data(self):
        sample_text = "Deal Name: XYZ Loan Amount: 1,000,000 USD Expiry Date: 01-Jan-2026"
        extraction_result = extract_data(sample_text)
        self.assertIn("Deal Name", extraction_result, "Data extraction failed")

if __name__ == '__main__':
    unittest.main()

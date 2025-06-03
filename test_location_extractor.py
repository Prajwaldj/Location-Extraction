import unittest
from location_extractor import LocationExtractor

class TestLocationExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = LocationExtractor()

    def test_location_extraction(self):
        text = "List properties in Baner and Wakad."
        expected = ["Baner", "Wakad"]
        self.assertEqual(self.extractor.extract_locations(text), expected)

    def test_location_extraction(self):
        text = "Location not entered."
        expected = ["No location found"]
        self.assertEqual(self.extractor.extract_locations(text), expected)

if __name__ == "__main__":
      unittest.main()
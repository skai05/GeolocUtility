import unittest
from utility.geoloc_utility import GeoLocUtility

class TestGeoLocUtility(unittest.TestCase):
    def test_valid_city_state(self):
        result = GeoLocUtility.fetch_location_by_name("Madison, WI")
        self.assertGreater(len(result), 0)
        self.assertIn("lat", result)
        self.assertEqual(result.get("country"), "US")

    def test_valid_zip(self):
        result = GeoLocUtility.fetch_location_by_zip("12345")
        self.assertIn("lat", result)
        self.assertEqual(result.get("country"), "US")

    def test_invalid_city_state(self):
        with self.assertRaises(Exception) as context:
            GeoLocUtility.fetch_location_by_name("UnknownCity")
        self.assertTrue("No results found in the US" in str(context.exception))

    def test_invalid_zip(self):
        with self.assertRaises(Exception) as context:
            GeoLocUtility.fetch_location_by_zip("99999")
        self.assertTrue("ZIP code not found in the US" in str(context.exception))

    def test_mixed_inputs(self):
        inputs = ["Madison, WI", "12345", "Springfield", "99999"]
        results = GeoLocUtility.fetch_locations(inputs)
        self.assertEqual(len(results), len(inputs))
        self.assertIn("lat", results[0])
        self.assertIn("lat", results[1])
        self.assertIn("error", results[3])

if __name__ == "__main__":
    unittest.main()

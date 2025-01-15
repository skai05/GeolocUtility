
import unittest
from utility.geoloc_utility import GeoLocUtility

class TestGeoLocUtility(unittest.TestCase):
    def test_fetch_location_by_name(self):
        result = GeoLocUtility.fetch_location_by_name("Chicago, IL")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("lat", result[0])
        self.assertIn("lon", result[0])

    def test_fetch_location_by_zip(self):
        result = GeoLocUtility.fetch_location_by_zip("90210")
        self.assertIsInstance(result, dict)
        self.assertIn("lat", result)
        self.assertIn("lon", result)

    def test_fetch_locations_mixed(self):
        locations = ["Chicago, IL", "90210"]
        result = GeoLocUtility.fetch_locations(locations)
        self.assertEqual(len(result), len(locations))
        self.assertIsInstance(result[0], list)  # City/state query returns a list
        self.assertIsInstance(result[1], dict)  # ZIP query returns a dict

if __name__ == "__main__":
    unittest.main()

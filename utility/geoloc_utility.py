
import requests

class GeoLocUtility:
    BASE_URL_NAME = "http://api.openweathermap.org/geo/1.0/direct"
    BASE_URL_ZIP = "http://api.openweathermap.org/geo/1.0/zip"
    API_KEY = "f897a99d971b5eef57be6fafa0d83239"

    @staticmethod
    def fetch_location_by_name(city_state):
        params = {"q": city_state, "appid": GeoLocUtility.API_KEY}
        response = requests.get(GeoLocUtility.BASE_URL_NAME, params=params)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def fetch_location_by_zip(zip_code):
        params = {"zip": zip_code, "appid": GeoLocUtility.API_KEY}
        response = requests.get(GeoLocUtility.BASE_URL_ZIP, params=params)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def fetch_locations(locations):
        results = []
        for location in locations:
            if location.isdigit():
                results.append(GeoLocUtility.fetch_location_by_zip(location))
            else:
                results.append(GeoLocUtility.fetch_location_by_name(location))
        return results

import requests

class GeoLocUtility:
    BASE_URL_NAME = "http://api.openweathermap.org/geo/1.0/direct"
    BASE_URL_ZIP = "http://api.openweathermap.org/geo/1.0/zip"
    API_KEY = "f897a99d971b5eef57be6fafa0d83239"

    @staticmethod
    def fetch_location_by_name(city_state):
        params = {"q": city_state, "appid": GeoLocUtility.API_KEY}
        response = requests.get(GeoLocUtility.BASE_URL_NAME, params=params)
        if response.ok:
            results = [res for res in response.json() if res.get("country") == "US"]
            if results:
                return results[0]  # Use the first valid result
            else:
                raise Exception("No results found in the US")
        else:
            raise Exception("API Error: Invalid city/state")

    @staticmethod
    def fetch_location_by_zip(zip_code):
        params = {"zip": zip_code, "appid": GeoLocUtility.API_KEY}
        response = requests.get(GeoLocUtility.BASE_URL_ZIP, params=params)
        if response.ok:
            if response.json().get("country") == "US":
                return response.json()  # Only return US-based results
            else:
                raise Exception("ZIP code not found in the US")
        else:
            raise Exception("API Error: Invalid ZIP code")

    @staticmethod
    def fetch_locations(locations):
        results = []
        for location in locations:
            try:
                if location.isdigit():
                    results.append(GeoLocUtility.fetch_location_by_zip(location))
                else:
                    results.append(GeoLocUtility.fetch_location_by_name(location))
            except Exception as e:
                results.append({"error": str(e), "input": location})
        return results

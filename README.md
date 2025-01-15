
# Geolocation Utility

## Overview
This utility fetches geolocation data (latitude, longitude, and place information) from the OpenWeather Geocoding API for a given list of city/state or ZIP code inputs.

## Features
- Supports both city/state and ZIP code inputs.
- Handles multiple locations in one call.
- Uses OpenWeather's Geocoding API.

## Setup

### Prerequisites
- Python 3.8 or higher
- `requests` library

### Installation
1. Clone the repository.
2. Navigate to the repository directory.
3. Install dependencies: `pip install -r requirements.txt`.

## Usage
Run the utility using the following formats:
```
python utility/geoloc_utility.py --locations "Madison, WI" "12345"
```

## Tests
To run the integration tests:
```
python -m unittest discover tests
```

## API Key
The utility uses a pre-configured API key: `f897a99d971b5eef57be6fafa0d83239`.

## Example Input
- `Madison, WI`
- `12345`

## Example Output
```
[
    {"lat": 43.0731, "lon": -89.4012, "name": "Madison", "state": "WI"},
    {"lat": 42.8142, "lon": -73.9396, "name": "12345", "country": "US"}
]
```


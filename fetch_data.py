# fetch_data.py
import requests
from config import API_BASE_URL

def fetch_route_data():
    """Fetch route and schedule information from transport.rest.
    Falls back to simulated data if API is unavailable.
    """
    try:
        resp = requests.get(API_BASE_URL, timeout=10)
        resp.raise_for_status()
        return resp.json()  # API response
    except Exception as e:
        print(f"[WARN] API unavailable ({e}). Using simulated data instead.")
        # Simulated route data for testing
        return [
            {"id": "bus1", "start_lat": 51.5074, "start_lon": -0.1278},  # London center
            {"id": "bus2", "start_lat": 51.5155, "start_lon": -0.1421},  # Oxford Circus
            {"id": "bus3", "start_lat": 51.5033, "start_lon": -0.1195},  # London Eye
        ]

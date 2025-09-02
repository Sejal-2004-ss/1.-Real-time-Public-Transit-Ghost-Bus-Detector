# utils.py
from datetime import datetime
import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth.

    Returns distance in degrees to match MIN_MOVE_THRESHOLD units in config.py.
    """
    # Convert decimal degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Earth radius in degrees (circumference / 360)
    earth_radius_km = 6371  # kilometers
    distance_km = earth_radius_km * c

    # Convert km to degrees (approx: 1° ~ 111.32 km)
    return distance_km / 111.32


def time_diff_seconds(t1, t2):
    """
    Return the absolute time difference between two datetime objects in seconds.
    Accepts both datetime objects and ISO 8601 strings.
    """
    if isinstance(t1, str):
        try:
            t1 = datetime.fromisoformat(t1)
        except ValueError:
            t1 = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
    if isinstance(t2, str):
        try:
            t2 = datetime.fromisoformat(t2)
        except ValueError:
            t2 = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
    return abs((t2 - t1).total_seconds())

# detect_ghosts.py
from datetime import datetime
import random
from utils import haversine, time_diff_seconds
from config import STALE_THRESHOLD, MIN_MOVE_THRESHOLD

previous_positions = {}

def simulate_bus_positions(routes):
    """Simulate bus locations along available routes as mock real-time data."""
    simulated = []
    now = datetime.utcnow()
    for route in routes[:10]:  # simulate first 10 routes
        lat = float(route.get("start_lat", random.uniform(0, 1)))
        lon = float(route.get("start_lon", random.uniform(0, 1)))
        simulated.append({
            "vehicle_id": route.get("id"),
            "lat": lat,
            "lon": lon,
            "timestamp": now
        })
    return simulated

def detect_ghosts(bus_list):
    now = datetime.utcnow()
    results = []

    for bus in bus_list:
        bus_id = bus["vehicle_id"]
        lat, lon = bus["lat"], bus["lon"]
        ts = bus["timestamp"]

        status = "healthy"
        reasons = []

        if time_diff_seconds(ts, now) > STALE_THRESHOLD:
            status = "ghost"
            reasons.append("stale data")

        if bus_id in previous_positions:
            prev_lat, prev_lon = previous_positions[bus_id]
            movement = haversine(lat, lon, prev_lat, prev_lon)
            if movement < MIN_MOVE_THRESHOLD:
                status = "ghost"
                reasons.append("not moving")

        previous_positions[bus_id] = (lat, lon)

        results.append({
            "vehicle_id": bus_id,
            "lat": lat,
            "lon": lon,
            "status": status,
            "reasons": ", ".join(reasons) or "-"
        })

    return results

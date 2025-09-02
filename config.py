# config.py

# Using transport.rest API for cities
CITY = "london"
API_BASE_URL = f"https://transport.rest/api/cities/{CITY}/routes"

# Detection thresholds
REFRESH_INTERVAL = 10  # seconds
STALE_THRESHOLD = 60   # seconds
MIN_MOVE_THRESHOLD = 0.0005  # degrees (~50m)

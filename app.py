# app.py
import streamlit as st
import pandas as pd
import time
from fetch_data import fetch_route_data
from detect_ghosts import simulate_bus_positions, detect_ghosts
from config import REFRESH_INTERVAL

st.set_page_config(page_title="Ghost Bus Detector (Simulated)", layout="wide")
st.title("🚌 Ghost Bus Detector — Using transport.rest Data (Simulated)")

while True:
    routes = fetch_route_data()
    bus_list = simulate_bus_positions(routes)
    data = detect_ghosts(bus_list)

    df = pd.DataFrame(data)
    total = len(df)
    ghosts = len(df[df["status"] == "ghost"])
    healthy = total - ghosts

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Buses", total)
    c2.metric("Healthy Buses", healthy)
    c3.metric("Ghost Buses", ghosts)

    st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))
    st.dataframe(df, use_container_width=True)

    time.sleep(REFRESH_INTERVAL)

import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# --- Klucz API OpenWeatherMap ---
API_KEY = "887c734580374264e3f182be7564ce52"

# --- Lista miast ---
CITIES = ["Amsterdam", "Porto", "Wroclaw", "Paris"]

# --- Funkcja pobierania danych ---
def fetch_air_quality(city):
    try:
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_resp = requests.get(geo_url).json()
        if not geo_resp:
            return None
        lat, lon = geo_resp[0]["lat"], geo_resp[0]["lon"]

        air_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        air_resp = requests.get(air_url).json()
        pm25 = air_resp["list"][0]["components"]["pm2_5"]

        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_resp = requests.get(weather_url).json()
        temp = weather_resp["main"]["temp"]
        humidity = weather_resp["main"]["humidity"]
        wind = weather_resp["wind"]["speed"]

        return {"PM2.5": pm25, "Temperatura (°C)": temp, "Wilgotność (%)": humidity, "Wiatr (m/s)": wind}
    except:
        return None

# --- Funkcja prognozy ---
def predict_pm25(base_pm25, temp_diff, hum_diff, wind_diff):
    pm25 = base_pm25
    pm25 -= temp_diff * 0.1   # ujemny wpływ temperatury
    pm25 -= hum_diff * 0.05   # ujemny wpływ wilgotności
    pm25 -= wind_diff * 0.3   # większy wiatr = mniej PM2.5
    return max(pm25, 0)

# --- Streamlit UI ---
st.title("„Prognoza jakości powietrza (PM2.5) z uwzględnieniem temperatury, wilgotności i wiatru – RAG + Publisher”")
selected_city = st.selectbox("Wybierz miasto", CITIES)

# --- Automatyczne odświeżanie co 60 sekund ---
count = st_autorefresh(interval=60 * 1000, limit=None, key="refresh")

# --- Pobranie danych bieżących ---
data = fetch_air_quality(selected_city)

if data:
    df_current = pd.DataFrame([data])
    st.subheader(f"Bieżące dane dla {selected_city}")
    st.dataframe(df_current)

    st.subheader("Prognoza PM2.5 dla nowych parametrów")
    temp_input = st.number_input("Temperatura (°C)", value=float(data["Temperatura (°C)"]))
    humidity_input = st.number_input("Wilgotność (%)", value=float(data["Wilgotność (%)"]))
    wind_input = st.number_input("Wiatr (m/s)", value=float(data["Wiatr (m/s)"]))

    pm25_pred = predict_pm25(
        base_pm25=data["PM2.5"],
        temp_diff=temp_input - data["Temperatura (°C)"],
        hum_diff=humidity_input - data["Wilgotność (%)"],
        wind_diff=wind_input - data["Wiatr (m/s)"]
    )
    st.write(f"Prognozowany PM2.5: {pm25_pred:.2f}")
else:
    st.error("Nie udało się pobrać danych dla wybranego miasta.")

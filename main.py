import time
from src.utils.weather_api import fetch_weather_data, convert_kelvin_to_celsius
from src.config.settings import API_KEY, CITIES, INTERVAL, THRESHOLD_TEMP

def monitor_weather():
    while True:
        for city in CITIES:
            weather_data = fetch_weather_data(city, API_KEY)
            temp = convert_kelvin_to_celsius(weather_data['main']['temp'])
            
            # Calculate rollups, log data, trigger alerts, etc.
            if temp > THRESHOLD_TEMP:
                print(f"ALERT: {city} temperature exceeded {THRESHOLD_TEMP}C!")
        
        time.sleep(INTERVAL)

if __name__ == '__main__':
    monitor_weather()

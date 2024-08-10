import requests
import matplotlib.pyplot as plt
from datetime import datetime


def fetch_weather(city_name, key):
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={key}"
    response = requests.get(base_url)

    if response.ok:
        return response.json()
    else:
        print("API çağrısı başarısız oldu.")
        return None


def extract_weather_info(weather_json):
    times = []
    temperatures = []

    for entry in weather_json.get('list', []):
        timestamp = datetime.fromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M')
        temp = entry['main']['temp']

        times.append(timestamp)
        temperatures.append(temp)

    return times, temperatures


def visualize_weather(times, temperatures, city_name):
    plt.figure(figsize=(12, 6))
    plt.plot(times, temperatures, marker='o', linestyle='-', color='b')
    plt.title(f"{city_name} İçin 7 Günlük Hava Durumu Tahmini")
    plt.xlabel('Tarih ve Saat')
    plt.ylabel('Sıcaklık (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def run_program():
    city_name = input("Hangi şehrin hava durumunu görmek istersiniz? ")
    api_key = ''
    weather_info = fetch_weather(city_name, api_key)

    if weather_info:
        times, temperatures = extract_weather_info(weather_info)
        visualize_weather(times, temperatures, city_name)


if __name__ == "__main__":
    run_program()

import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weather (
    date_time TEXT,
    temperature REAL
)
''')


def get_temperature():
    url = 'https://www.gismeteo.ua/ua/weather-kyiv-4944/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temp_div = soup.find('div', class_='js_value')
        if temp_div:
            temperature = temp_div.text.strip()
            return float(temperature.replace('°', ''))
    return None


temperature = get_temperature()

if temperature is not None:
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
    INSERT INTO weather (date_time, temperature) VALUES (?, ?)
    ''', (current_time, temperature))

    conn.commit()

    print(f"Температура на {current_time} склала {temperature}°C.")
else:
    print("Не вдалося отримати температуру.")

conn.close()
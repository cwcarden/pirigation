import requests
import json
import time
from config import Config

def test():
    print(Config.weather)
#initiate timestamp, api_key from darksky, and gps coordinates of location that will be used for weather data
timestamp = int(time.time())
longitude = "35.2091"
lattitude = "-101.8890"

"""
Darksky api calls for water weather delay
current function calls current weather, writes to database for history logging, then returns a boolean value
for rain delay
"""
def current():
    url = f'https://api.darksky.net/forecast/{Config.weather["api_key"]}/{longitude},{lattitude}?exclude=minutely,daily,flags'
    res = requests.get(url)
    data = res.json()
    current_data = {
            "time": data['currently']['time'], "condition": data['currently']['summary'],
            "precipProbability": data['currently']['precipProbability'],
            "humidity": data['currently']['humidity'], "temperature": data['currently']['temperature'],
            "wind": data['currently']['windSpeed'], "icon": data['currently']['icon']
    }
"""
#write current weather to database every 4 hours for rain event logging
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS weather_data (id ")
    with open('data.json', 'a') as f:
        json.dump(current_data, f)

    current_weather = current_data['icon']
    if current_weather == 'rain':
        return True
    else:
        return False
"""
def forecast():
    url = f'https://api.darksky.net/forecast/{Config.weather["api_key"]}/{longitude},{lattitude}?exclude=minutely,current,daily,flags'
    res = requests.get(url)
    weather_data = res.json()
    six_hr_forcast = weather_data['hourly']['data'][7]['precipProbability']
    if six_hr_forcast > Config.weather["rain_prob"]:
        return True # True for engage water
    else:
        return False
"""
def history():
    -Parses weather_logger data in either json or db
    -checks if rain event was in past ? hours of current timestamp
"""


def all_weather():
    if forecast() or current() == True or history() == True:
        return True
    else:
        return False

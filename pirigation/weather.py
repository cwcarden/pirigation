import requests
import json
import time

timestamp = int(time.time())
api_key = ""
longitude = "35.2091"
lattitude = "-101.8890"

#Darksky api calls for water weather delay
def current():
    url = f'https://api.darksky.net/forecast/{api_key}/{longitude},{lattitude}?exclude=minutely,daily,flags'
    res = requests.get(url)
    data = res.json()
    current_data = {
            "time": data['currently']['time'], "condition": data['currently']['summary'],
            "precipProbability": data['currently']['precipProbability'],
            "humidity": data['currently']['humidity'], "temperature": data['currently']['temperature'],
            "wind": data['currently']['windSpeed'], "icon": data['currently']['icon']
    }
    with open('data.json', 'w') as f:
        json.dump(current_data, f)
    current_weather = current_data['icon']
    if current_weather == 'rain':
        return True
    else:
        return False

def forecast():
    url = f'https://api.darksky.net/forecast/{api_key}/{longitude},{lattitude}?exclude=minutely,current,daily,flags'
    res = requests.get(url)
    weather_data = res.json()
    six_hr_forcast = weather_data['hourly']['data'][7]['precipProbability']
    if six_hr_forcast > 0.8:
        return True # True for engage water
    else:
        return False
''' history function has five api calls that check for rain from past hour,
past 3 hr, past 6 hr, past 12 hr, and past 24 hours to determine if any rain has occurred.'''
def history():
    past_day = timestamp - 86400
    twelve_hour = timestamp - 42300
    six_hour = timestamp - 21150
    three_hour = timestamp - 10575
    one_hour = timestamp - 3525
    url_past_day = f'https://api.darksky.net/forecast/{api_key}/{longitude},{lattitude},{past_day}'
    url_past_twelve = f'https://api.darksky.net/forecast/{api_key}/{longitude},{lattitude},{twelve_hour}'
    url_past_six = f'https://api.darksky.net/forecast/{api_key}/{longitude},{lattitude},{six_hour}'
    url_past_three = f'https://api.darksky.net/forecast/{api_key}/{longitude},{lattitude},{three_hour}'
    url_past_hr = f'https://api.darksky.net/forecast/{api_key}/{longitude},{lattitude},{one_hour}'
    res_day = requests.get(url_past_day)
    res_twelve = requests.get(url_past_twelve)
    res_six = requests.get(url_past_six)
    res_three = requests.get(url_past_three)
    res_hr = requests.get(url_past_hr)
    weather_data_24 = res_day.json()
    weather_data_12 = res_twelve.json()
    weather_data_6 = res_six.json()
    weather_data_3 = res_three.json()
    weather_data_hr = res_hr.json()
    pastcast_24 = weather_data_24['hourly']['data'][0]['icon']
    pastcast_12 = weather_data_12['hourly']['data'][0]['icon']
    pastcast_6 = weather_data_6['hourly']['data'][0]['icon']
    pastcast_3 = weather_data_3['hourly']['data'][0]['icon']
    pastcast_hr = weather_data_hr['hourly']['data'][0]['icon']
    if pastcast_24 == 'rain' or pastcast_12 == 'rain' or pastcast_6 == 'rain' or pastcast_3 == 'rain' or pastcast_hr == 'rain':
        return True
    else:
        return False

def all_weather():
    if forecast() or current() == True or history() == True:
        return True
    else:
        return False

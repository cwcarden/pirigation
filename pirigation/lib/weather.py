import requests
import json
import time

darksky_api_key = ""
latitude = "35.2429"
longitude = "-101.9333"
rain_prob = 0.9 # <- need to fix to coencide with 0 - 1 precipProbability from API
current_forecast_data = {}

def get_current():
    """Gets current weather conditions"""
    url = f'https://api.darksky.net/forecast/{darksky_api_key}/{latitude},{longitude}?exclude=minutely,current,daily,flags'
    forecast_data = requests.get(url).json()
    current_data = forecast_data['currently']
    current_forecast_data.update({'temperature': current_data['temperature'], 'precip_prob': current_data['precipProbability'], 
    'rain_intensity': current_data['precipIntensity'], 'wind': current_data['windSpeed'], 'current_time': current_data['time']})
    print(current_data)

def get_forecast():
    """Gets rain probability for 6 and 8 hour forecast then returns True or False. True if rain is greater than rain_prob configuration"""
    url = f'https://api.darksky.net/forecast/{darksky_api_key}/{latitude},{longitude}?exclude=minutely,current,daily,flags'
    forecast_data = requests.get(url).json()
    six_hr_forecast = forecast_data['hourly']['data'][7]['precipProbability']
    eight_hr_forecast = forecast_data['hourly']['data'][8]['precipProbability']
    if six_hr_forecast or eight_hr_forecast > rain_prob:
        return True
    else:
        return False

def get_history():
    """Get rain history"""
    current_time = time.time()
    hist_time = int(current_time - (24*60*60)) #subtracts one day from current time


    url = f'https://api.darksky.net/forecast/{darksky_api_key}/{latitude},{longitude},{hist_time}?exclude=currently,flags'
    history_data = requests.get(url).json()
    hist = history_data
    print(hist_time)
    print(hist)
     
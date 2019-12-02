import requests
import json
import time
import config


def get_local():
    """Gets local weather station temperature, last rain date, and current rain event, returns data respectively in tuple
    example: ('2019-10-05T02:56:00.000Z', 51.6, 0)
    """
    url = f"https://api.ambientweather.net/v1/devices?applicationKey={config.app_key}&apiKey={config.api_key}"
    data = requests.get(url).json() 
    local_data = {
        "timestamp": data[-1]['lastData']['dateutc'], "humidity": data[-1]['lastData']['humidity'],
        "tempf": data[-1]['lastData']['tempf'], 'windspeed': data[-1]['lastData']['windspeedmph'],
        "weekrain": data[-1]['lastData']['weeklyrainin'], "rainevent": data[-1]['lastData']['eventrainin'], 
        "lastrain": data[-1]['lastData']['lastRain']
    }
    last_rain = local_data["lastrain"]
    current_temp = local_data["tempf"]
    is_raining =  local_data["rainevent"]
    return last_rain, current_temp, is_raining
    
def get_forecast():
    """Gets rain probability for 6 and 8 hour forecast then returns True or False. True if rain is greater than rain_prob configuration"""
    url = f'https://api.darksky.net/forecast/{config.darksky_api_key}/{config.latitude},{config.longitude}?exclude=minutely,current,daily,flags'
    forecast_data = requests.get(url).json()
    six_hr_forecast = forecast_data['hourly']['data'][7]['precipProbability']
    eight_hr_forecast = forecast_data['hourly']['data'][8]['precipProbability']
    if six_hr_forecast or eight_hr_forecast > config.rain_prob:
        return True
    else:
        return False
#import weather
import datetime
import dateutil.parser
import pytz #time zone support module
#import config

def is_raining():
    """ checks if it is currently raining """
    if weather.get_local()[2] > 0:
        return True
    else:
        return False
    
def last_rain():
    """ Gets difference of current time and last rain time """
    last_rain = dateutil.parser.parse(weather.get_local()[0])
    current_time = pytz.utc.localize(datetime.datetime.utcnow())
    dif = current_time - last_rain
    return dif.days
  
def check_temp():
    """ Gets current temperature for freeze and heat watering functions """
    return weather.get_local()[1]




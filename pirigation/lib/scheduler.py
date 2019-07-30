import datetime
import time
import sqlite3

#checks and returns current cst time
def current_time():
    current_time = time.strftime('%H:%M')#temporarily formatted for colon for prettiness in index template
    return(current_time)

#checks and returns current day of the week
def current_day():
    day_of_week = datetime.datetime.today().strftime('%A')
    return(day_of_week)

#checks if current datetime params == db schedule params
def schedule_checker():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM schedule ORDER BY id; ''')
    schedule_time = c.fetchall()
    conn.close()
    start_time = (schedule_time[0][3])
    start_days = (schedule_time[0])
    days_dict = {"Sunday": start_days[3], "Monday": start_days[4], "Tuesday": start_days[5],
                "Wednesday": start_days[6],"Thursday": start_days[7],"Friday": start_days[8],
                "Saturday": start_days[9],}
    days_to_water = [day for day in days_dict if days_dict[day]]
    if current_day() in days_to_water and start_time == current_time():
        return True
    else:
        return False

#Checks zone 1 enabled and runtime
def z1_enab():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM zone ORDER BY id; ''')
    zone_list = c.fetchall()
    conn.close()
    zone_1 = zone_list[0]
    if zone_1[1] == 1:
        return True
    else:
        return False

def z1_runtime():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM zone ORDER BY id; ''')
    zone_list = c.fetchall()
    conn.close()
    zone_1 = zone_list[0]
    z1_runtime = zone_1[3]
    return(z1_runtime)
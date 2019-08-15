from weather import all_weather as aw
import relays
import scheduler as sched
import time

#Get current schedule boolean from scheduler module
def scheduler():
    if sched.schedule_checker() == True:
        return True
    else:
        return False
        print("...")
        time.sleep(30)
        scheduler()

#Get rain delay information from weather module
def rain_delay():
    if aw() == True:
        print("Rain Delay")
        return True #Rain Delay = True activates rain delay
    else:
        print("water")
        return False #Rain Delay = False allows relays to activate normally
'''
def run_relays():
    relays.zone_1()
    relays.zone_2()
    relays.zone_3()
    relays.zone_4()
    relays.zone_5()
    print("watering complete. awaiting next schedule...")
'''
#FOR TESTING ONLY##################################################FOR TESTING#
def run_relays():                                                 
    print("watering zone 1")
    time.sleep(25)
    print("watering zone 2")
    time.sleep(25)
    print("watering zone 3")
    time.sleep(25)
    print("watering complete. awaiting next schedule...")
#FOR TESTING ONLY#################################################FOR TESTING#
def main():
    while True:
        if scheduler() == True and rain_delay() == False:
            run_relays()

#if __name__=="__main__":
#    main()

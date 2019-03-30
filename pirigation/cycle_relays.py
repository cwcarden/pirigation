import RPi.GPIO as GPIO
import datetime
import time
import scheduler as sch
#set GPIO mode to Broadcom SOC channel
GPIO.setmode(GPIO.BCM)

'''
GPIO HIGH is off, while GPIO LOW is on. 
GPIO Pins that run relays here use the time.sleep to execute 
runtime length.
relayDelay works well to be set at 1 or 2 seconds.  This allows the water valves to 
have time to open and close between cycles.

(ZONE FUNCTIONS)
Each zone (ex. zone_1()) has its own complete function to execute an entire cycle
of watering.  For example, zone_1 function enables the master valve to be turned on 
then the actual zone 1 valve runs on the scheduled time in the database. After
time.sleep expires, GPIO.HIGH is called on those gpio pins turning off watering and 
power to the pins
'''

#GPIO pin that is labeled for Master Vavle (MV on relay)
master_valve = (2,)
gpioPins = (3, 4, 5, 6, 7, 8, 9)

GPIO.setup(master_valve, GPIO.OUT)
GPIO.output(master_valve, GPIO.HIGH)

for pin in gpioPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
#time the relay will be turned off in seconds between intervals. 1 or 2 seconds works well
relayDelay = 1
'''
TO DO: create zone functions to turn on and off. Must have both functions 
to call from manual html form.

'''
#zone_1() executes a full cycle of turning master valve and zone 1 valve on and off
def zone_1():
    GPIO.output(master_valve, GPIO.HIGH)
    try:
        while True:
            for valve in master_valve:
                GPIO.output(valve, GPIO.LOW)
                print("master valve on")
                time.sleep(1)
                #Zone 1
                GPIO.output(gpioPins[0], GPIO.LOW)
                print("zone 1 on")
                time.sleep(sch.z1_runtime())
                GPIO.output(gpioPins[0], GPIO.HIGH)
                time.sleep(relayDelay)
                # closes or turns off power to master valve gpio pin powering relay MV
                GPIO.output(valve, GPIO.HIGH)
                print("zone 1 completed--master valve off")
                time.sleep(relayDelay)
            break
    except KeyboardInterrupt:
        print("job cancelled")

#zone_2() executes a full cycle of turning master valve and zone 2 valve on and off
def zone_2():
    GPIO.output(master_valve, GPIO.HIGH)
    try:
        while True:
            for valve in master_valve:
                GPIO.output(valve, GPIO.LOW)
                print("master valve on")
                time.sleep(1)
                #Zone 2
                GPIO.output(gpioPins[1], GPIO.LOW)
                print("zone 2 on")
                time.sleep(sch.z2_runtime())
                GPIO.output(gpioPins[1], GPIO.HIGH)
                time.sleep(relayDelay)
                # closes or turns off power to master valve gpio pin powering relay MV
                GPIO.output(valve, GPIO.HIGH)
                print("zone 2 completed--master valve off")
                time.sleep(relayDelay)
            break
    except KeyboardInterrupt:
        print("job cancelled")

#zone_3() executes a full cycle of turning master valve and zone 3 valve on and off
def zone_3():
    GPIO.output(master_valve, GPIO.HIGH)
    try:
        while True:
            for valve in master_valve:
                GPIO.output(valve, GPIO.LOW)
                print("master valve on")
                time.sleep(1)
                #Zone 3
                GPIO.output(gpioPins[2], GPIO.LOW)
                print("zone 3 on")
                time.sleep(sch.z3_runtime())
                GPIO.output(gpioPins[2], GPIO.HIGH)
                time.sleep(relayDelay)
                # closes or turns off power to master valve gpio pin powering relay MV
                GPIO.output(valve, GPIO.HIGH)
                print("zone 3 completed--master valve off")
                time.sleep(relayDelay)
            break
    except KeyboardInterrupt:
        print("job cancelled")

#zone_4() executes a full cycle of turning master valve and zone 4 valve on and off
def zone_4():
    GPIO.output(master_valve, GPIO.HIGH)
    try:
        while True:
            for valve in master_valve:
                GPIO.output(valve, GPIO.LOW)
                print("master valve on")
                time.sleep(1)
                #Zone 4
                GPIO.output(gpioPins[3], GPIO.LOW)
                print("zone 4 on")
                time.sleep(sch.z4_runtime())
                GPIO.output(gpioPins[3], GPIO.HIGH)
                time.sleep(relayDelay)
                # closes or turns off power to master valve gpio pin powering relay MV
                GPIO.output(valve, GPIO.HIGH)
                print("zone 4 completed--master valve off")
                time.sleep(relayDelay)
            break
    except KeyboardInterrupt:
        print("job cancelled")

#zone_5() executes a full cycle of turning master valve and zone 5 valve on and off
def zone_5():
    GPIO.output(master_valve, GPIO.HIGH)
    try:
        while True:
            for valve in master_valve:
                GPIO.output(valve, GPIO.LOW)
                print("master valve on")
                time.sleep(1)
                #Zone 5
                GPIO.output(gpioPins[4], GPIO.LOW)
                print("zone 5 on")
                time.sleep(sch.z5_runtime())
                GPIO.output(gpioPins[4], GPIO.HIGH)
                time.sleep(relayDelay)
                # closes or turns off power to master valve gpio pin powering relay MV
                GPIO.output(valve, GPIO.HIGH)
                print("zone 5 completed--master valve off")
                time.sleep(relayDelay)
            break
    except KeyboardInterrupt:
        print("job cancelled")
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

gpio_pins = {
    'mv': 2, 'z1': 3, 'z2': 4, 'z3': 5, 'z4': 6, 'z5': 7, 'z6': 8, 'z7': 9
    }

GPIO.setup(master_valve, GPIO.OUT)
GPIO.output(master_valve, GPIO.HIGH)

for k, v in gpio_pins:
    GPIO.setup(v, GPIO.OUT)
    GPIO.output(v, GPIO.HIGH)

#Master Valve
def mv_on():
    GPIO.output(gpio_pins['mv'], GPIO.HIGH)
    GPIO.output(gpio_pins['mv'], GPIO.LOW)

def mv_off():
    GPIO.output(gpio_pins['mv'], GPIO.HIGH)

#ZONE 1 Control
def z1_on():
    GPIO.output(gpio_pins['z1'], GPIO.HIGH)
    GPIO.output(gpio_pins['z1'], GPIO.LOW)

def z1_off():
    GPIO.output(gpio_pins['z1'], GPIO.HIGH)

#ZONE 2 Control
def z2_on():
    GPIO.output(gpio_pins['z2'], GPIO.HIGH)
    GPIO.output(gpio_pins['z2'], GPIO.LOW)

def z2_off():
    GPIO.output(gpio_pins['z2'], GPIO.HIGH)

#ZONE 3 Control
def z3_on():
    GPIO.output(gpio_pins['z3'], GPIO.HIGH)
    GPIO.output(gpio_pins['z3'], GPIO.LOW)

def z3_off():
    GPIO.output(gpio_pins['z3'], GPIO.HIGH)

#ZONE 4 Control
def z4_on():
    GPIO.output(gpio_pins['z4'], GPIO.HIGH)
    GPIO.output(gpio_pins['z4'], GPIO.LOW)

def z4_off():
    GPIO.output(gpio_pins['z4'], GPIO.HIGH)

#ZONE 5 Control
def z5_on():
    GPIO.output(gpio_pins['z5'], GPIO.HIGH)
    GPIO.output(gpio_pins['z5'], GPIO.LOW)

def z5_off():
    GPIO.output(gpio_pins['z5'], GPIO.HIGH)

#ZONE 6 Control
def z6_on():
    GPIO.output(gpio_pins['z6'], GPIO.HIGH)
    GPIO.output(gpio_pins['z6'], GPIO.LOW)

def z6_off():
    GPIO.output(gpio_pins['z6'], GPIO.HIGH)

#ZONE 7 Control
def z7_on():
    GPIO.output(gpio_pins['z7'], GPIO.HIGH)
    GPIO.output(gpio_pins['z7'], GPIO.LOW)

def z7_off():
    GPIO.output(gpio_pins['z7'], GPIO.HIGH)

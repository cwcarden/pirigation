import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

master_valve = (2,)
gpio_pins = (3, 4, 5, 6, 7, 8, 9)

GPIO.setup(master_valve, GPIO.OUT)
GPIO.output(master_valve, GPIO.HIGH)

for pin in gpio_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def mv_on():
    GPIO.output(master_valve, GPIO.HIGH)
    GPIO.output(maseter_valve, GPIO.LOW)

def mv_off():
    GPIO.output(master_valve, GPIO.HIGH)

#ZONE 1 Control
def z1_on():
    GPIO.output(gpio_pins[0], GPIO.HIGH)
    GPIO.output(gpio_pins[0], GPIO.LOW)

def z1_off():
    GPIO.output(gpio_pins[0], GPIO.HIGH)

#ZONE 2 Control
def z2_on():
    GPIO.output(gpio_pins[1], GPIO.HIGH)
    GPIO.output(gpio_pins[1], GPIO.LOW)

def z2_off():
    GPIO.output(gpio_pins[1], GPIO.HIGH)

#ZONE 3 Control
def z3_on():
    GPIO.output(gpio_pins[2], GPIO.HIGH)
    GPIO.output(gpio_pins[2], GPIO.LOW)

def z3_off():
    GPIO.output(gpio_pins[2], GPIO.HIGH)

#ZONE 4 Control
def z4_on():
    GPIO.output(gpio_pins[3], GPIO.HIGH)
    GPIO.output(gpio_pins[3], GPIO.LOW)

def z4_off():
    GPIO.output(gpio_pins[3], GPIO.HIGH)

#ZONE 5 Control
def z5_on():
    GPIO.output(gpio_pins[4], GPIO.HIGH)
    GPIO.output(gpio_pins[4], GPIO.LOW)

def z5_off():
    GPIO.output(gpio_pins[4], GPIO.HIGH)

#ZONE 6 Control
def z6_on():
    GPIO.output(gpio_pins[5], GPIO.HIGH)
    GPIO.output(gpio_pins[5], GPIO.LOW)

def z6_off():
    GPIO.output(gpio_pins[5], GPIO.HIGH)

#ZONE 7 Control
def z7_on():
    GPIO.output(gpio_pins[6], GPIO.HIGH)
    GPIO.output(gpio_pins[6], GPIO.LOW)

def z7_off():
    GPIO.output(gpio_pins[6], GPIO.HIGH)
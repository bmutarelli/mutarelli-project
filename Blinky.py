#First Test with GPIO
#Brogan Mutarelli
#Dec, 19, 2017

import time

import RPi.GPIO as GPIO

led_pin_blue = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin_blue, GPIO.OUT)

while True:
    print ("     S")
    GPIO.output(led_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(0.5)
    #
    print ("     O")
    GPIO.output(led_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(1)
    GPIO.output(led_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(1)
    GPIO.output(led_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(1)
    GPIO.output(led_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(1)
    GPIO.output(led_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(1)
    GPIO.output(led_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(1)
    #
    print ("      S")
    GPIO.output(led_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.HIGH)
    print ("On")
    time.sleep(0.5)
    GPIO.output(led_pin_blue, GPIO.LOW)
    print ("Off")
    time.sleep(3)

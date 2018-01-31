import time

import RPi.GPIO as GPIO

led_blue = 23
led_red = 22
led_green = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_blue, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
while True:
    time.sleep (1)
    GPIO.output(led_blue, GPIO.HIGH)
    GPIO.output(led_red, GPIO.LOW)
    GPIO.output(led_green, GPIO.LOW)
    time.sleep (1)
    GPIO.output(led_blue, GPIO.LOW)
    GPIO.output(led_red, GPIO.HIGH)
    GPIO.output(led_green, GPIO.LOW)
    time.sleep (1)
    GPIO.output(led_blue, GPIO.LOW)
    GPIO.output(led_red, GPIO.LOW)
    GPIO.output(led_green, GPIO.HIGH)

import time

import RPi.GPIO as GPIO

led_blue = 22
led_red = 21
led_green = 23 

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_blue, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)


pwm_red = GPIO.PWM(led_red,100)
pwm_blue = GPIO.PWM(led_blue,100)
pwm_green = GPIO.PWM(led_green,100)
while True:
    red = 100
    green = 50
    blue = 25

    count1 = 0

    while count1<50:
        pwm_red.start(red)
        red = red-1
        pwm_blue.start(blue)
        blue = blue+1
        pwm_green.start(green)
        green = green+1
        time.sleep(0.15)

    red = 25
    green = 100
    blue = 50

    count1 = 0

    while count1<50:
        pwm_red.start(red)
        red = red+1
        pwm_blue.start(blue)
        blue = blue+1
        pwm_green.start(green)
        green = green-1
        time.sleep(0.15)

    red = 50
    green = 25
    blue = 100

    count1 = 0

    while count1<50:
        pwm_red.start(red)
        red = red+1
        pwm_blue.start(blue)
        blue = blue-1
        pwm_green.start(green)
        green = green+1
        time.sleep(0.15)



pwm_red.stop()
pwm_blue.stop()
pwm_green.stop()
GPIO.cleanup

##pwm_red.start(50)
##time.sleep(1)
##pwm_red.start(75)
##time.sleep(1)
##pwm_red.start(100)
##time.sleep(1)

#Brogan Mutarelli
#PIR Test

#import libraries
import RPi.GPIO as GPIO
import time


PIR = 12
LED = 6
BUTTON = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

#While loop that check if the sensor is detecting motion
while True:
    GPIO.output(LED, GPIO.LOW)

    if GPIO.input(BUTTON):
    
        while True:
            GPIO.output(LED, GPIO.LOW)
        
            if GPIO.input(PIR):
                print("Motion Detected")
                GPIO.output(LED, GPIO.HIGH)


            else:
                print("No Motion Detected")
                GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)
            if GPIO.input(BUTTON):
                break
            
            time.sleep(0.3)
            GPIO.output(LED, GPIO.LOW)
        time.sleep(0.1)
        
    

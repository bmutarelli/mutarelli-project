#Light Up Guessing Game
#Brogan Mutarelli
#Jan 3 2018
#guess number, blue too low, red too high, green just right (1-20)
#five tries

#
import time
import random
import RPi.GPIO as GPIO

led_blue = 22
led_red = 21
led_green = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_blue, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
y_n = "Y"

def game_over():
    print("You ran out of guesses")
    
def blink(LED):   

    for i in range (5):
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.25)

def party_led():
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
#

#Title screen
while y_n == "Y":
    print("""WELCOME TO GUESS THE NUMBER! YOU GET FIVE TRIES.
    THE NUMBER WILL RANGE FROM 1 TO 20.
    THE LIGHT WILL FLASH RED IF YOU GUES IS TO HIGH, BLUE IF IT IS TOO LOW, AND GREEN IF IT IS SPOT ON!
    HAVE FUN!!!!""")

    #get random number

    ran_num = random.randint(1, 20)

    #Start loop (5 TRIES)
    guess = 1
    while guess <= 5:
        #get a guess from the user
        userG = input("Guess a number from 1 to 20:")

        if userG == "Python":
            party_led()
            break
        userG = int(userG)
        #Check if correct
        if userG == ran_num:
            print ("Great Job")
            blink(led_green)
            break
            
        elif userG < ran_num:
            print ("Too Low")
            blink(led_blue)
            guess += 1
            
        elif userG > ran_num:
            print ("Too High")
            blink(led_red)
            guess += 1

    else:
        game_over()
        
    y_n = input("Do you want to play again? (y/n)  : ").upper()


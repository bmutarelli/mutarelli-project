#Broigan Mutarelli
#DJ Raspi
#A music playing DJ machine with the input of 2 buttons



#import libraries
import RPi.GPIO as GPIO
import random
import time
import os

path_music = "/usr/share/scratch/Media/Sounds/Music Loops"
path_vocals = "/usr/share/scratch/Media/Sounds/Vocals"
path_effects = "/usr/share/scratch/Media/Sounds/Effects"

def play_random_sound(sound_path, sound_files):
    sound_file = random.choice(sound_files)
    os.system("omxplayer -o local '" + sound_path + "/" + sound_file + "' &")
    
    
def get_MP3_sounds(sound_path):
    sounds = os.listdir(sound_path)
    sound_files = [sound for sound in sounds if sound.endswith(".mp3")]
    return sound_files

#Button pins
bp1 = 6
bp2 = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(bp1, GPIO.IN)
GPIO.setup(bp2, GPIO.IN)

sounds_music = get_MP3_sounds(path_music)
sounds_vocals = get_MP3_sounds(path_vocals)
sounds_effects = get_MP3_sounds(path_effects)

##sounds_music = [sound for sound in sounds_music if sound.endswith(".mp3")]
##sounds_vocals = [sound for sound in sounds_vocals if sound.endswith(".mp3")]
os.system("clear")
title = """
    DJ Raspi
    Press Button 1 for Music Sounds
    Press Button 2 for Vocal Sounds
    Press Ctrl + C to Exit
    """

print (title)


     

while True:
    if GPIO.input(bp1):
        print("You Pressed Button 1")
        play_random_sound(path_music, sounds_music)
        time.sleep(0.1)
        
    elif GPIO.input(bp2):
        print("You Pressed Button 2")
        play_random_sound(path_vocals, sounds_vocals)
        time.sleep(0.1)

    if GPIO.input(bp2) and GPIO.input(bp1):
        print("You pressed both buttons")
        play_random_sound(path_effects, sounds_effects)
        time.sleep(0.1)
        
    time.sleep(0.1)

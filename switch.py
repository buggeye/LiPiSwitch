#! /usr/bin/python

# Imports
import RPi.GPIO as GPIO
import requests
import time
from lifxlan import LifxLAN, Light, WHITE
from gpiozero import Button
from time import sleep

# Turn off GPIO warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Variables - Add your MAC and IP number here.
lifxlan = Light("d0:23:d5:2d:4e:60", "192.168.2.1")
currentstate = 0
button = Button(14)
previousstate = lifxlan.get_power()
lightname = lifxlan.get_label()

# Show current light state
if previousstate == 0:
    print("The", lightname, "is currently OFF")
elif previousstate == 65535:
    print("The", lightname, "is currently ON")

try:
    print("Starting LiPiSwitch for the light named", lightname,"...")
    print("")
    print("lifXbutton Ready ...")
    print("")

# Loop until user quits with CTRL-C
    while True:        

        # If the Button is triggered
        if button.is_pressed and previousstate == 0:
             print("Button Pressed - Turning Light ON")

             # LifxLAN light details
             r = lifxlan.set_power("on")
             h = lifxlan.set_brightness("65535") #Set the light to full brightness
             g = lifxlan.set_color(WHITE) #Set the light to daylight

             # Record new previous state
             previousstate = 65535

             #Wait 3 seconds before looping again
             print("Waiting 3 seconds")
             time.sleep(3)
             print("")
             print("Ready")
             print("")

        elif button.is_held:
             print("Button Held - Dimming Light")

             # LifxLAN light details
             r = lifxlan.set_power("on")
             h = lifxlan.set_brightness("5000")

             #Wait 3 seconds before looping again
             print("Waiting 3 seconds")
             time.sleep(3)
             print("")
             print("Ready")
             print("")

        elif button.is_pressed and previousstate == 65535:
             print("Button Pressed - Turning Light OFF")

             # LifxLAN light details
             r = lifxlan.set_power("off")

             # Record new previous state
             previousstate = 0

             #Wait 3 seconds before looping again
             print("Waiting 3 seconds")
             time.sleep(3)
             print("")
             print("Ready")
             print("")

except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings
    GPIO.cleanup()
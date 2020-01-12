# LiPiSwitch
LifX Raspberry Pi Zero Wall Switch

To get the neccessary files, you can download the files 'switch.py' and 'forever', then the latest LIFXLAN project files from https://github.com/mclarkk/lifxlan or simply download the 'lipiswitch-complete.zip' which contains all these files and extract onto your Raspberry Pi Zero. 

Make sure you follow the step by step instruction below.

INTRODUCTION

This project was born out of necessity, when I purchased a WiFi enabled smart LIFX bulb for our bedroom. I love the idea of changing the temperature of the light, white for daytime and orange for evenings and the ability to remotely turn the light off.  In short, I love the LIFX light bulbs.
 
However, they don’t pass the wife test.  What’s the wife test?  In simple terms if your wife can not turn the light on and off just like she could with a standard bulb, then it’s useless, and you will need to remove it before she does!

All I needed was a standard wall switch that turned the bulb on or off when pressed.
 
After searching the internet for solutions, I found exactly… NONE.  Sure there is the Flic Bluetooth button, but that requires a hub or a phone to be near by. And like most other options, it requires an internet connection as it utilises the IFTTT service.
 
Quite by accident I found the most excellent lifexlan project from ML Clark on github.  This brilliant piece of coding simply uses the official LIFX API to control the bulbs with a Python script. Finally, we now have a platform that suits the Raspberry Pi Zero W perfectly.
 
What this means is that we can use the Pi to control the light using the same WiFi network that the bulb is on.  No lag, just instant on and off with the flick of a wall switch.
 
 
WARNINGS

Before you start, a warning regarding 240v light switches. This project utilises a standard Australian wall switch.  While it does not require you to change any 240v wiring, it does mean pulling the light switch from the wall and adding the new (low voltage) switch into your wall panel.  You can build this project and test it, but you will need to employ the services of a licensed electrician to install that switch into the wall plate. 
 
Also, how you get power to your Raspberry Pi Zero is up to you and outside of the scope of this project.  I recommend only powering your Pi Zero using the micro USB power port.
 
While you could use the official Raspberry Pi power supply, I found that an Apple iPhone charger (the small ones) are great for powering up a Raspberry Pi Zero W. We will not be using any peripherals such as keyboards and mice, so the 1amp from the charger will be plenty. 

What you will need:
1.   LIFX Light Bulb
     a. You need to have setup your LIFX light bulb using the LIFX app before attempting this project. This project     communicates with the LIFX bulb directly over WiFi, so it needs to be on the same SSID as what your Pi Zero will be on.
 
2.   Raspberry Pi Zero W with SD card
     a. The Pi Zero comes in two flavours (with and without pin headers).  If you are like me, and can’t solder for the life of you, I recommend the Raspberry Pi Zero WH, so that you can simply connect the switch wires to the pins.
 
3.   Raspberry Pi USB Power Supply or similar quality power supply.

4.   Momentary (Bell Press) Switch
     a. Such as the Clipsal Push Button Switch https://www.clipsal.com/products/detail?catno=30PBBP&tab-document-1=1 or the Clipsal Bell Press Standard Rocker https://www.clipsal.com/products/detail?catno=30MBPR&tab-document-1=1 these switches are compatible with most other brands such as HPM. They simply snap into the Wall Gang Plate and can easily be removed by leveraging with flat head screw driver.  You can purchase these directly from your local electrical wholesaler.
 

5.   Low Voltage Cable
     a. You can use any low voltage electrical cable. I used some left over telephone cable or you could use some jumper cable or even cat 5/6 ethernet cable.  Your cable needs to be long enough to extend from your Pi Zero to the wall switch. Your Pi will only output a maximum of +3.3V through the momentary switch and cable.

6.   2 Pin Female Polarized Header Connector
     a. Again, because of my bad soldering skills, I used a pin header connector to attach the Low Voltage Cable to the GPIO pins on the Pi Zero.    You can find some here https://core-electronics.com.au/2-pin-female-polarized-header-connector.html,

7.   Polarized Header Connectors – Crimp Pins

a.   While still requiring some solder, they are a lot easier than trying to solder directly to the PCB of Pi Zero. You can find the Crimp Pins here https://core-electronics.com.au/polarized-connectors-crimp-pins.html.


Instructions
Pi Zero W setup
 
1.   Download, extract and image your SD Card with Raspbian Lite 
     a. Follow the installation guide here https://www.raspberrypi.org/documentation/installation/installing-images/README.md

2.   Headless setup of the Pi Zero W 
     a. Follow these instructions to setup your Pi Zero headless (without a keyboard and monitor) https://core-electronics.com.au/tutorials/raspberry-pi-zerow-headless-wifi-setup.html
     b. I had to remove the WPA line in the wpasupplicant.conf file in order for it to connect to my wifi, even though I am running WPA2 security, it seems to automatically find the correct security protocol.

3.   Copy the LiPiSwitch script onto your Pi Zero
     a. Copy the entire lipiswitch folder onto your Pi Zero using your PC or MAC

4.   SSH into your Pi
     a. On a MAC simply open a Terminal and type “SSH pi@raspberrypi.local”.  On a PC use an app such a PuTTy to connect using SSH.
     b. The default password is “raspberry”

5.   Run sudo raspi-config
     a. There are a number of things to setup in the raspi-config:   
        -  Change User Password
           Change the default password to your own password
        -  Network Options
           Change the default hostname to LiPiSwitch1
        -  Boot Options
           B1 – Ensure the Pi Zero boots using Console Autologin
        -  Localisation Options
           I1 – Change Locale
           Select en_AU.UT-8 UTF-8
           I2 – Change Timezone
           Select Australia
        -  Interfacing Options
           Enable SSH
        -  Advanced Options
           Expand the Filesystem to fill your entire SD Card
        -  Update
           Auto update your Pi Zero to make sure you have the latest Raspbian
           
     b. Reboot and check that you can now SSH into your Pi Zero without the need for the SSH file in your boot folder.

6.   Move the LiPiSwitch folder to your home folder
     a. Make sure you have a stable SSH connection to your Pi Zero using your new hostname, such as pi@LiPiSwitch1.local
     b. Type sudo mv /boot/lipiswitch /home/pi/

7.   Install Python3 pip
     a. Type sudo apt install python3-pip

8.   Install GPIO Zero
     a. Type sudo pip3 install gpiozero

9.   Install lifxlan
     a. Type sudo pip3 install lifxlan

10.  Find your lights
     a. Type cd lipiswitch/
     b. Type pyhton3 find.py
     c. Note down the MAC address and IP address of your light

11.  Edit the LiPiSwitch Script
     a. Type sudo nano switch.py
     b. Find the section called “# Edit me”
     c. Change the line “lifxlan = Light…” to include your lights MAC Address and IP Number.
     d.	Save and exit nano by pressing CTRL + X and overwrite the file.

12.  Test Lights
     a. Type python3 switch.py
     b. Test to see if your switch turns the light on
     c. To exit the script press CTRL-C

13.  Make the script auto start and self restart
     a. Type sudo nano /etc/profile
     b. Add the following as the last lines:
        i.  cd lipiswitch/
        ii. sudo python3 ./forever switch.py
     c. Type sudo reboot
 
 
Switch Setup
1.   Wire up your switch
     a. Use the Low Voltage Cable to connect one wire to the ‘C’, Common, Positive or Live terminal of your switch, and another wire to connect to the ‘1’, Negative or Neutral terminal.
     b. Solder the other end of your cable using the head connector and crimp pins.

2.   Plug and play
     a. Plug the cable into the Pi Zero using pin BCM 14 and Ground which is also known as Pin 6 and 8.  As this is just a switch it does not matter what polarity it is.

3.   Install your wall switch and provide power to Pi Zero
     a. You will need a licenced electrician to replace your wall switch with a two-gang wall plate containing your existing light switch and your new LiPiSwitch.  You keep the existing mechanical light switch in order to manually turn the bulb on and off.  This is a must have safety feature, so that you can safely replace the bulb.
     b. Your Pi Zero will then need to be located close to a power point. There are multiple options that you can explore for the position of your Pi Zero and power supply.  I recommend that you discuss your options with a licensed electrician.  There are a few things that you can consider.
        i.  You will need the ability to physically turn your Pi Zero on and off using the switch on the power point. 
        ii. You could hide your Pi Zero within the wall cavity.  Just make sure you have plenty of air space in the cavity. 
        iii.You could install a cable tidy hole near your power point to run your power cable through the wall and in to a power point.
        iv  You could have your electrician wire up a surface mount power point (the ones they put into the roof space for plugging downlights into) and have it switched using the existing wall switch.  Your USB power supply would then be in the roof space (or possibly even in the wall cavity behind the switch). This has the benefit of being able to turn the power off to the Pi along with the light socket without ever seeing the power supply or cable.
 
And that’s about it.  Enjoy!
 
Full qudos goes to the excellent lifxlan python project by ML Clark available from https://github.com/mclarkk/lifxlan

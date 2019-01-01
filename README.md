# Raspberry Pi Parking Assistant

### Setup Instructions
1. [Raspberry Pi Initial Setup](#raspberry-pi-initial-setup)
2. [SSH Setup for Windows](#ssh-setup-for-windows)
3. [Download the GitHub Repo](#download-the-github-repo)
4. [Download Required Python Packages](#download-required-python-packages)
5. [Connect the Sensors](#connect-the-sensors)

### Required Materials

1. Raspberry Pi 3b+
2. Micro SD Card
3. Pi Traffic Light - [Amazon](https://www.amazon.com/gp/product/B00RIIGD30/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)
4. Ultrasonic Distance Sensor HC-SR04 - [Amazon](https://www.amazon.com/SainSmart-HC-SR04-Ranging-Detector-Distance/dp/B004U8TOE6/ref=asc_df_B004U8TOE6/?tag=hyprod-20&linkCode=df0&hvadid=312127837151&hvpos=1o2&hvnetw=g&hvrand=16154594324665021790&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9008164&hvtargid=pla-459285090715&psc=1&tag=&ref=&adgrpid=57636291530&hvpone=&hvptwo=&hvadid=312127837151&hvpos=1o2&hvnetw=g&hvrand=16154594324665021790&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9008164&hvtargid=pla-459285090715)
5. PIR Motion Sensor HC-SR501 - [Amazon](https://www.amazon.com/DIYmall-HC-SR501-Motion-Infrared-Arduino/dp/B012ZZ4LPM/ref=asc_df_B012ZZ4LPM/?tag=hyprod-20&linkCode=df0&hvadid=312141147291&hvpos=1o3&hvnetw=g&hvrand=17007910937892278118&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9008164&hvtargid=pla-570427408451&psc=1&tag=&ref=&adgrpid=68997874944&hvpone=&hvptwo=&hvadid=312141147291&hvpos=1o3&hvnetw=g&hvrand=17007910937892278118&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9008164&hvtargid=pla-570427408451)
6. Jumper Wires
7. Resistors

<br><br><br>
## Raspberry Pi Initial Setup

### Required Materials
1. Raspberry Pi 3b+
2. Micro SD Card

The steps below describe how to set up a Raspberry Pi for the first time, and enable SSH. SSH allows you to remotely connect to the Raspberry Pi from another computer. This allows you to develop/troubleshoot on your Pi without needing to connect keyboards and monitors.

### Step 1: Install Raspbian on the SD Card and the Raspberry Pi

For easy installation, use the [NOOBS package](https://www.raspberrypi.org/documentation/installation/noobs.md) from the Raspberry Pi website.

For more advanced installation, follow the instructions [here](https://www.raspberrypi.org/documentation/installation/installing-images/).

After saving to the SD Card, put the SD card into the Raspberry Pi and boot it. Follow the on-screen instructions for installing Raspbian and configuring your WiFi, timezone, language, etc.

### Step 2: Set up a static IP address on the Pi

First, check the default IP address settings for your network. Boot the RPI, open the terminal and type `ip a`.

The IP address of your RPI should be listed under the eth0 header (if connected to ethernet), or the wlan0 header (if using WiFi). It should look something like this: 198.168.0.XXX. The default IP format is the first three sets of numbers. For many networks, it will look like 198.168.0.XXX. On my network, the last "0" is a "7" (i.e. 198.168.7.XXX). When you're following the instructions in the link below, be sure to use your network's standard IP format. For example, the instructions below assume the IP is 192.168.0.XXX. However, in my case, I need to use 192.168.7.XXX.  

The official instructions for setting up a static IP address are [here](https://www.raspberrypi.org/learning/networking-lessons/rpi-static-ip-address/).

Be sure to follow the "Testing" instructions in the above link, by rebooting your Pi and confirming the correct IP address is set.

### Step 3: Enable SSH on your Pi

The latest Raspbian distributions, by default, do not allow for SSH. To enable it, do the following:

1. Type `sudo raspi-config` in a terminal.
2. Select `Interfacing Options`.
3. Select `SSH`
4. Select `Yes` > `Ok` > `Finish`

The above is adopted form the official instructions [here](https://www.raspberrypi.org/documentation/remote-access/ssh/).

<br><br><br>
## SSH Setup for Windows

### Step 1: Ping the Raspberry Pi
First, confirm that the Pi can be reached over the network. Type `cmd` into the program search bar, and open the Windows command line.
In the command line, type `ping 198.168.0.XXX`, using the static IP address you selected in "Step 2" above. If you get a network response, then the Pi can be reached.

### Step 2: Download the PuTTY and WinSCP Clients
Next, Download [PuTTY](https://www.putty.org/) and [WinSCP](https://winscp.net/eng/download.php).

PuTTY allows us to SSH into the Pi. WinSCP is a file transfer program that allows us to transfer files to the Pi remotely over the home network.

### Step 3: Set up PuTTY

Open PuTTY, and put the static IP you set up in the `Host Name (or IP address)` box (do not include the `/24` at the end of the IP you set up... e.g. if you followed the official instructions exactly, you would enter `192.168.0.2` here). Keep the port as 22. Select `SSH` as the connection type.

To save the IP address for future reference, you can enter a name under `Saved Sessions` and click `Save`. Then, whenever you open PuTTY, you can select the name, click `Load` and then `Open`.

Click `Open` to estable an SSH connection. The default username is `pi`, and the default password is `raspberry`. If you changed the password on the Raspbian setup, be sure to use that password. If the machine connects without an error, then SSH is set up correctly.

### Step 4: Set up WinSCP

Open WinSCP, and enter the static IP you used above, keep the Port as 22, and enter the username `pi`, and either the default password `raspberry` or the new password if you changed it. Click `Save` if you'd like to save the IP address for future reference. When you connect, you should be able to see the files and folders on the Pi. You can use this to transfer files onto the Pi remotely.

<br><br><br>
## Download the GitHub Repo

### Step 1: SSH into the Pi

Open PuTTY, and establish an SSH connection with the Pi.

### Step 2: Download Git Repository

To download the scripts from this repository, in the PuTTY SSH window, type the following:

```
git clone https://github.com/reowen/Park-Assist.git
```

This will create a folder called "Park-Assist" in your home directory with all of the scripts for this project.

<br><br><br>
## Download Required Python Packages

### Pi Traffic Light

The traffic light uses the [RPi.GPIO library](https://pypi.org/project/RPi.GPIO/). To install this on your Pi, use PuTTY to SSH into the Pi. After connecting, type the following:

```
pip install RPi.GPIO
```

You'll see "Successfully install RPi.GPIO" if it worked.

The official documentation for the Python modules for the light is [here](http://wiki.lowvoltagelabs.com/pitrafficlight_python_example).


<br><br><br>
## Connect the Sensors

### GPIO Pin Reference

![GPIO Reference](https://myelectronicslab.com/wp-content/uploads/2016/06/raspbery-pi-3-gpio-pinout-40-pin-header-block-connector-1-1.png)

### Pi Traffic Light

The official connection documentation is [here](http://wiki.lowvoltagelabs.com/pitrafficlight). For the Pi 3B+, we connect to GPIO pins 9, 10, and 11, and a corresponding grounding wire. To do this position the Pi with the HDMI plug facing towards you (so the USB plugs are to the right on the board, and the GPIO pins are at the back). Then, on the front row of GPIO pins, count 7 pins from the right, and place the light to the left of the 7th pin, with the lights pointing away from you. If that description is confusing, refer to the GPIO pin reference image above, and play around with positioning the light until you can get it working.

For wiring and mounting the light in my garage, instead of directly placing the lights on the GPIO pin board, I used female-to-male jumper wires and mounted the lights through the wires.

### PIR Motion Sensor

Documentation on connecting this sensor can be found [here](https://www.mysensors.org/build/motion). 

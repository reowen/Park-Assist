
"""
This script contains the classes and functions that control the sensors, and initialize the Raspberry Pi's GPIO board.

The master function for controlling the Parking Assistant is in the park_assist.py script. It references the
class objects and functions in this module.
"""

import RPi.GPIO as GPIO
import time
import warnings

class StopLight:
    """ The StopLight class controls the Pi stoplight. """
    def __init__(self, red_pin=9, yellow_pin=10, green_pin=11):
        """
        Initializes a StopLight object, and sets the red, yellow, and green GPIO pin positions. The default pin positions are 9, 10, and 11 respectively.
        However, a second light can also be connected to pins 19 (red), 13 (yellow), and 26 (green).

        Args:
            red_pin (int): The GPIO pin number for the red light. By default this is 9.
            yellow_pin (int): The GPIO pin number for the yellow light. By default this is 10.
            green_pin (int): The GPIO pin number for the green light. By default this is 11.
        """

        # Validate the pin positions
        assert red_pin in [9, 19], "red_pin must equal either 9 or 19."
        assert yellow_pin in [10, 13], "yellow_pin must equal either 10 or 13."
        assert green_pin in [11, 26], "green_pin must equal either 11 or 26."
        assert [red_pin, yellow_pin, green_pin] in [[9, 10, 11], [19, 13, 26]], "Pins must be position (red_pin=9, yellow_pin=10, green_pin=11), or (red_pin=19, yellow_pin=13, green_pin=26)"

        # Save the PIN numbers as instance variables
        self.red_pin = red_pin
        self.yellow_pin = yellow_pin
        self.green_pin = green_pin

        # Pin Setup:
        GPIO.setup([red_pin, yellow_pin, green_pin], GPIO.OUT) # Set the LED pins as outputs

    def toggle_lights(self, red=False, yellow=False, green=False, all=False):
        """
        Controls the stoplights. If the color arguments are set to True, it will turn on the corresponding lights. All colors are
        set to False by default, so not explicitly setting a color to True will turn it off (i.e., this function with no arguments
        will turn off all the lights.

        Args:
            red (bool): If =True, the function will turn on the red light. If =False, it will turn it off. By default, this argument =False.
            yellow (bool): If =True, the function will turn on the yellow light. If =False, it will turn it off. By default, this argument =False.
            green (bool): If =True, the function will turn on the green light. If =False, it will turn it off. By default, this argument =False.
            all (bool): If =True, the function will turn on all the lights. If =False, it will only turn on the colors specified as true.
        """
        # Validate arguments
        assert isinstance(red, bool), "'red' must be a boolean (True or False)."
        assert isinstance(yellow, bool), "'yellow' must be a boolean (True or False)."
        assert isinstance(green, bool), "'green' must be a boolean (True or False)."
        assert isinstance(all, bool), "'all' must be a boolean (True or False)."

        # Toggle the lights
        if all:
            GPIO.output(self.red_pin, True)
            GPIO.output(self.yellow_pin, True)
            GPIO.output(self.green_pin, True)
        else:
            GPIO.output(self.red_pin, red)
            GPIO.output(self.yellow_pin, yellow)
            GPIO.output(self.green_pin, green)

    def blink(self, red=False, yellow=False, green=False, all=False):
        """
        Function that blinks the lights. Takes the corresponding color, and blinks the colors that are set to True.
        """
        self.toggle_lights() # Turn off all lights.
        self.toggle_lights(red=red, yellow=yellow, green=green, all=all) # Turn on specified lights.
        time.sleep(0.5) # Pause for half a second.
        self.toggle_lights() # Turn off all lights.

    def blink_multi(self, blinks=5, red=False, yellow=False, green=False, all=False):
        """
        Function that blinks the lights a specified number of times. By default, the function blinks 5 times.

        Args:
            blinks (int): An integer with the number of times the light will blink. By default, the light blinks 5 times.
            red (bool): If =True, the function will blink the red light. If =False, it will remain off. By default, this argument =False.
            yellow (bool): If =True, the function will blink the yellow light. If =False, it will remain off. By default, this argument =False.
            green (bool): If =True, the function will blink the green light. If =False, it will remain off. By default, this argument =False.
            all (bool): If =True, the function will blink all the lights. If =False, it will only blink the specified colors. By default, this argument =False.
        """
        # Validate the blinks argument
        assert isinstance(blinks, int), "'blinks' must be an integer."

        # Blink the specified number of times
        for i in range(0, blinks):
            self.blink(red=red, yellow=yellow, green=green, all=all)
            time.sleep(0.5)

    def test_sensor(self):
        """
        Runs a test to ensure the lights are working correctly.
        """
        print("All lights on...")
        self.toggle_lights(all=True)
        time.sleep(1)

        print("Red light on...")
        self.toggle_lights(red=True)
        time.sleep(1)

        print("Yellow light on...")
        self.toggle_lights(yellow=True)
        time.sleep(1)

        print("Green light on...")
        self.toggle_lights(green=True)
        time.sleep(1)

        print("Blink red.")
        self.blink(red=True)

        print("Blink yellow.")
        self.blink(yellow=True)

        print("Blink green.")
        self.blink(green=True)

        print("Blink all.")
        self.blink(all=True)

        print("Blink red 3 times.")
        self.blink_multi(blinks=3, red=True)

        print("Blink yellow 3 times.")
        self.blink_multi(blinks=3, yellow=True)

        print("Blink green 3 times.")
        self.blink_multi(blinks=3, green=True)

        print("Blink all 3 times.")
        self.blink_multi(blinks=3, all=True)


class MotionSensor():
    """ Class for controlling and reading the PIR motion sensor. """

    def __init__(self, pin=14):
        assert isinstance(pin, int), "'pin' argument must be an integer."
        # Assign GPIO pin number as instance variable
        self.pin = pin
        # Set GPIO pin as an input
        GPIO.setup(pin, GPIO.IN)
        print("PIR Sensor set to GPIO pin: {}".format(self.pin))
        print("PIR motion sensor initializating...")
        time.sleep(5)
        print("PIR motion Sensor activated.")

    def detect_motion(self):
        """ Returns True if motion is detected, False otherwise. """
        if GPIO.input(self.pin) == True:
            return True
        else:
            return False

    def test_sensor(self):
        """ Tests that the motion detector is working correctly by blinking the stoplights when motion is detected. """  
        lgt = StopLight()
        lgt.blink_multi(blinks=3, all=True)

        try:
            print("Loop initialized. Press ctrl+c to end.")
            while True:
                if self.detect_motion():
                    print("\nMotion Detected!\n")
                    lgt.blink_multi(all=True)
        except KeyboardInterrupt:
            print("Program ended...")
            pass


class DistanceSensor():
    """ Controls the Distance Sensor """

    def __init__(self, trigger_pin=18, echo_pin=15):
        """
        Sets the GPIO pin values for the trigger and echo pins on the distance sensor, then sets the trigger pin 
        as an output on the Pi, and the echo pin as an input. 
        
        Args: 
            trigger_pin (int): The GPIO pin used for the trigger. By default, this is GPIO18. 
            echo_pin (int): The GPIO pin used for the echo. By default, this is GPIO15. 
        """
        # Validate arguments
        assert isinstance(trigger_pin, int), "'trigger_pin' argument must be an integer."
        assert isinstance(echo_pin, int), "'echo_pin' argument must be an integer."

        # Assign GPIO pin numbers as instance variables
        self.trigger = trigger_pin
        self.echo = echo_pin

        # Setup GPIO pins
        print("Initializing distance sensor...")
        GPIO.setup(trigger_pin, GPIO.OUT) # trigger as output pin
        GPIO.setup(echo_pin, GPIO.IN) # echo as input pin
        GPIO.output(trigger_pin, False)
        time.sleep(2)
        print("Distance sensor initialized.")

    def find_distance(self):
        """
        Takes a distance reading using the sensor, by counting the number of milliseconds between the trigger 
        and echo times. Returns the read distance in centimeters. 
        """
        # Initialize the trigger
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        # Log the start and stop times
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()

        duration = pulse_end - pulse_start
        distance = duration * 17150 # converts the measured duration to centimeters 
        return round(distance, 2)

    def test_sensor(self):
        """ Tests the sensor by taking a distance reading, and printing the results in the terminal. """
        dist = self.find_distance()
        print("Distance: {0}cm.".format(dist))


# Helper functions for initializing and ending session
def initialize_session(pin_mode='BCM'):
    """
    Initializes the GPIO board on the Pi.

    Args:
        pin_mode (str): Determines which pin mode to set. Must equal either 'BCM' (to set the pin scheme to GPIO.BCM), or 'BOARD'.
                        By default, this is 'BCM'.
    """
    mode = GPIO.getmode()
    moderef = {10: 'BOARD', 11:'BCM'}
    # If the GPIO mode is already set, prints the current mode.
    if mode:
        if moderef[mode] == pin_mode:
            warnings.warn('Mode already set to {}!'.format(pin_mode))
        else:
            raise Exception("GPIO mode already set to {0}, cannot set to {1}.".format(moderef[GPIO.getmode()], pin_mode))
    # If the GPIO mode is not set, sets the designated pin scheme.
    else:
        if pin_mode == 'BCM':
            GPIO.setmode(GPIO.BCM)
        elif pin_mode == 'BOARD':
            GPIO.setmode(GPIO.BOARD)
        else:
            raise Exception("'pin_mode' must equal either 'BCM' or 'BOARD'.")
        print("Set GPIO mode to: {}.".format(moderef[GPIO.getmode()]))


def close_session(channels=None):
    """ Closes the session by cleaning the GPIO channels on the Pi. """
    if channels:
        GPIO.cleanup(channels)
        print("Cleaned the following channels: {}".format(channels))
    else:
        GPIO.cleanup()
        print("All GPIO pins cleaned.")


if __name__ == "__main__":
    initialize_session()
    
    lgt = StopLight() 
    lgt.test_sensor() 

    mtn = MotionSensor(pin=14)
    mtn.test_sensor()

    ds = DistanceSensor()
    ds.test_sensor()

    close_session()

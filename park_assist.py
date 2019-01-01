
import RPi.GPIO as GPIO
import time

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
        GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
        GPIO.setup(red_pin, GPIO.OUT) # Set red LED pin as an output
        GPIO.setup(yellow_pin, GPIO.OUT) # Set yellow LED pin as an output
        GPIO.setup(green_pin, GPIO.OUT) # Set green LED pin as an output

    def toggle_red(self, on=True, blink=False):
        """
        Turns on or off the red light.

        Args:
            on (bool): If on=True, the function will turn on the light. If =False, it will turn off the light. By default, on=True.
            blink (bool): If blink=True, the function will make the light blink for 5 seconds. By default, the light will not blink.
        """
        # Validate arguments
        assert isinstance(on, bool), "'on' must be a boolean (True or False)."
        assert isinstance(blink, bool), "'blink' must be a boolean (True or False)."

        if not blink:
            GPIO.output(self.red_pin, on)
        elif blink:
            for sec in range(0, 5):
                GPIO.output(self.red_pin, True)
                time.sleep(0.5)
                GPIO.output(self.red_pin, False)
                time.sleep(0.5)

    def toggle_yellow(self, on=True, blink=False):
        """
        Turns on or off the yellow light.

        Args:
            on (bool): If on=True, the function will turn on the light. If =False, it will turn off the light. By default, on=True.
            blink (bool): If blink=True, the function will make the light blink for 5 seconds. By default, the light will not blink.
        """
        # Validate arguments
        assert isinstance(on, bool), "'on' must be a boolean (True or False)."
        assert isinstance(blink, bool), "'blink' must be a boolean (True or False)."

        if not blink:
            GPIO.output(self.yellow_pin, on)
        elif blink:
            for sec in range(0, 5):
                GPIO.output(self.yellow_pin, True)
                time.sleep(0.5)
                GPIO.output(self.yellow_pin, False)
                time.sleep(0.5)

    def toggle_green(self, on=True, blink=False):
        """
        Turns on or off the green light.

        Args:
            on (bool): If on=True, the function will turn on the light. If =False, it will turn off the light. By default, on=True.
            blink (bool): If blink=True, the function will make the light blink for 5 seconds. By default, the light will not blink.
        """
        # Validate arguments
        assert isinstance(on, bool), "'on' must be a boolean (True or False)."
        assert isinstance(blink, bool), "'blink' must be a boolean (True or False)."

        if not blink:
            GPIO.output(self.green_pin, on)
        elif blink:
            for sec in range(0, 5):
                GPIO.output(self.green_pin, True)
                time.sleep(0.5)
                GPIO.output(self.green_pin, False)
                time.sleep(0.5)

    def toggle_all(self, on=True, blink=False):
        """
        Turns on or off all the lights at the same time.

        Args:
            on (bool): If on=True, the function will turn on the light. If =False, it will turn off the light. By default, on=True.
            blink (bool): If blink=True, the function will make the light blink for 5 seconds. By default, the light will not blink.
        """
        # Validate arguments
        assert isinstance(on, bool), "'on' must be a boolean (True or False)."
        assert isinstance(blink, bool), "'blink' must be a boolean (True or False)."

        if not blink:
            GPIO.output(self.green_pin, on)
            GPIO.output(self.yellow_pin, on)
            GPIO.output(self.red_pin, on)
        elif blink:
            for sec in range(0, 5):
                GPIO.output(self.green_pin, True)
                GPIO.output(self.yellow_pin, True)
                GPIO.output(self.red_pin, True)
                time.sleep(0.5)
                GPIO.output(self.green_pin, False)
                GPIO.output(self.yellow_pin, False)
                GPIO.output(self.red_pin, False)
                time.sleep(0.5)


if __name__ == "__main__":
    # Test the red, green and yellow are working correctly:
    lgt = StopLight(red_pin=19, yellow_pin=13, green_pin=11)

    print("Red light on...")
    lgt.toggle_red()
    time.sleep(2)
    lgt.toggle_red(on=False)

    print("Yellow light on...")
    lgt.toggle_yellow()
    time.sleep(2)
    lgt.toggle_yellow(on=False)

    print("Green light on...")
    lgt.toggle_green()
    time.sleep(2)
    lgt.toggle_green(on=False)

    print("All lights on...")
    lgt.toggle_all()
    time.sleep(2)
    lgt.toggle_all(on=False)

    print("Blink red.")
    lgt.toggle_red(blink=True)

    print("Blink yellow.")
    lgt.toggle_yellow(blink=True)

    print("Blink green.")
    lgt.toggle_green(blink=True)

    print("Blink all.")
    lgt.toggle_all(blink=True)

    GPIO.cleanup()

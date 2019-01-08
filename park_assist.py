
"""
This script contains the master function for running the parking assistant. It calls the class objects and functions
defined in the sensors.py script.
"""

# Import the sensors module
import sensors

def run_park_assistant(green_range=80, yellow_range=(60, 80), red_range=(20,60), red_flash=20:
    """ A master function for running the park assistant algorithm. """
    # Step 1: Initialize the sensors session
    sensors.initialize_session()

    # Step 2: Initialize the sensors using the default GPIO pin numbers
    stoplight = sensors.StopLight()
    motion_sensor = sensors.MotionSensor()
    distance_sensor = sensors.DistanceSensor()

    # Step 3: Blink the lights to signal the parking assistant is fully initialized
    print("Parking Assistant fully initialized...")
    stoplight.blink_multi(blinks=5, all=True)

    # Step 4: Initialize the parking assistant to be triggered by the motion sensor
    try:
        print("Motion sensor started. Press Ctrl+C to stop...")
        while True:
            if motion_sensor.detect_motion():
                stoplight.blink(all=True)
                # Start reading distance
                while True:
                    distance = distance_sensor.find_distance()
                    # Flash appropriate light if distance within specified ranges. 
                    if distance > green_range:
                        stoplight.toggle_lights(green=True)
                    if distance < yellow_range[1] and distance > yellow_range[0]:
                        stoplight.toggle_lights(yellow=True)
                    if distance < red_range[1] and distance > red_range[0]:
                        stoplight.toggle_lights(red=True)
                    if distance < red_flash:
                        stoplight.blink_multi(blinks=5, red=True)

    except KeyboardInterrupt:
        print("Program ended...")

    # Close the sensors session
    finally:
        sensors.close_session()

if __name__ == "__main__":
    run_park_assistant()

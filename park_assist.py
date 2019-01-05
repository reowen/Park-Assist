
"""
This script contains the master function for running the parking assistant. It calls the class objects and functions
defined in the sensors.py script.
"""

# Import the sensors module
import sensors

def run_park_assistant():
    # Initialize the sensors session
    sensors.initialize_session()

    # Initialize the sensors using the default GPIO pin numbers
    stoplight = sensors.StopLight()
    motion_sensor = sensors.MotionSensor()
    distance_sensor = sensors.DistanceSensor()

    # Blink the lights to signal the parking assistant is fully initialized
    print("Parking Assistant fully initialized...")
    stoplight.blink_multi(blinks=5, all=True)

    # Initialize the parking assistant to be triggered by the motion sensor
    try:
        print("Motion sensor started. Press Ctrl+C to stop...")
        while True:
            if motion_sensor.detect_motion():
                stoplight.blink(all=True)
                # Start reading distance
                while True:
                    distance = distance_sensor.find_distance()
                    # If the distance reading exceeds 80 cm
                    if distance > 80:
                        stoplight.toggle_lights(green=True)
                    if distance < 80 and distance > 60:
                        stoplight.toggle_lights(yellow=True)
                    if distance < 60 and distance > 20:
                        stoplight.toggle_lights(red=True)
                    if distance < 20:
                        stoplight.blink_multi(blinks=5, red=True)

    except KeyboardInterrupt:
        print("Program ended...")

    # Close the sensors session
    finally:
        sensors.close_session()

if __name__ == "__main__":
    run_park_assistant()

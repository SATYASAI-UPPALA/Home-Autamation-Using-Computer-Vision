import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Define the pins connected to the LEDs
led_pins = [13, 12, 11, 10, 9]  # GPIO pins for 5 LEDs

# Set up the GPIO pins as outputs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Define the function to control the LEDs
def led(total):
    if total == 0:
        GPIO.output(led_pins[0], GPIO.LOW)
        GPIO.output(led_pins[1], GPIO.LOW)
        GPIO.output(led_pins[2], GPIO.LOW)
        GPIO.output(led_pins[3], GPIO.LOW)
        GPIO.output(led_pins[4], GPIO.LOW)
    elif total ==1:
        GPIO.output(led_pins[0], GPIO.HIGH)
        GPIO.output(led_pins[1], GPIO.LOW)
        GPIO.output(led_pins[2], GPIO.LOW)
        GPIO.output(led_pins[3], GPIO.LOW)
        GPIO.output(led_pins[4], GPIO.LOW)

    elif total ==2:
        GPIO.output(led_pins[0], GPIO.LOW)
        GPIO.output(led_pins[1], GPIO.HIGH)
        GPIO.output(led_pins[2], GPIO.LOW)
        GPIO.output(led_pins[3], GPIO.LOW)
        GPIO.output(led_pins[4], GPIO.LOW)

    elif total==3:
        GPIO.output(led_pins[0], GPIO.LOW)
        GPIO.output(led_pins[1], GPIO.LOW)
        GPIO.output(led_pins[2], GPIO.HIGH)
        GPIO.output(led_pins[3], GPIO.LOW)
        GPIO.output(led_pins[4], GPIO.LOW)
     
    elif total==4:
        GPIO.output(led_pins[0], GPIO.LOW)
        GPIO.output(led_pins[1], GPIO.LOW)
        GPIO.output(led_pins[2], GPIO.LOW)
        GPIO.output(led_pins[3], GPIO.HIGH)
        GPIO.output(led_pins[4], GPIO.LOW)

    elif total==5:
        GPIO.output(led_pins[0], GPIO.LOW)
        GPIO.output(led_pins[1], GPIO.LOW)
        GPIO.output(led_pins[2], GPIO.LOW)
        GPIO.output(led_pins[3], GPIO.LOW)
        GPIO.output(led_pins[4], GPIO.HIGH)
        

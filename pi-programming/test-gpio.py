import RPi.GPIO as GPIO
from time import sleep
# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

# Set up the GPIO channels - one input and one output
GPIO.setup(22, GPIO.OUT)

# Output to pin 12

while(True):
    GPIO.output(22, GPIO.HIGH)
    print("high")
    sleep(3)
    GPIO.output(22, GPIO.LOW)
    print("low")
    sleep(3)






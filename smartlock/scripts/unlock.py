import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

GPIO.output(37, True)
time.sleep(0.5)	
GPIO.cleanup()


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

GPIO.output(37, False)
GPIO.output(7, True)
time.sleep(2)	
GPIO.cleanup()

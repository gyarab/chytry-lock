import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)


GPIO.cleanup()
GPIO.output(3, True)
time.sleep(2)	
GPIO.cleanup()

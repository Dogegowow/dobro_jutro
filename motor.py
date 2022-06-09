from time import sleep
import RPi.GPIO as GPIO
def setup(step, dir, mos):
  
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dir, GPIO.OUT)
    GPIO.setup(step, GPIO.OUT)
    GPIO.setup(mos, GPIO.OUT)
    GPIO.output(mos, GPIO.LOW)

    MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
    GPIO.setup(MODE, GPIO.OUT)
    RESOLUTION = {'Full': (0, 0, 0),
                  'Half': (1, 0, 0),
                  '1/4': (0, 1, 0),
                  '1/8': (1, 1, 0),
                  '1/16': (0, 0, 1),
                  '1/32': (1, 0, 1)}
    GPIO.output(MODE, RESOLUTION['1/4'])

    

def run(stepPin, dirPin, dir, mos, dist):
    delay = .005 / 12
    GPIO.output(mos, GPIO.HIGH)
    GPIO.output(dirPin, dir)
    for x in range(int(dist*300)):
        GPIO.output(stepPin, GPIO.HIGH)
        sleep(delay)
        GPIO.output(stepPin, GPIO.LOW)
        sleep(delay)
        
    #ugasni mosfet
    GPIO.output(mos, GPIO.LOW)
    GPIO.cleanup()


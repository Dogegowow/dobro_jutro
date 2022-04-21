from time import sleep
import RPi.GPIO as GPIO
def setup():
    #motor1
    DIR = 20   # Direction GPIO Pin
    STEP = 21  # Step GPIO Pin
    MOS = 23
    #motor2
    DIR2 = 5
    STEP2 = 6
    MOS2 = 24
    #settings
    CW = 1     # Clockwise Rotation
    CCW = 0    # Counterclockwise Rotation
    SPR = 200   # Steps per Revolution (360 / 7.5)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.setup(DIR2, GPIO.OUT)
    GPIO.setup(STEP2, GPIO.OUT)
    GPIO.setup(MOS, GPIO.OUT)
    GPIO.setup(MOS2, GPIO.OUT)
    GPIO.output(DIR, CW)
    GPIO.output(MOS, GPIO.LOW)
    GPIO.output(DIR2, CW)
    GPIO.output(MOS2, GPIO.LOW)


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
    for x in range(int(dist*3200)):
        GPIO.output(stepPin, GPIO.HIGH)
        sleep(delay)
        GPIO.output(stepPin, GPIO.LOW)
        sleep(delay)
        
    #ugasni mosfet
    GPIO.output(mos, GPIO.LOW)
    GPIO.cleanup()


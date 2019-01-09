import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#The sensor in the front
GPIO_trig1 = 19
GPIO_echo1 = 26

GPIO.setup(GPIO_trig1, GPIO.OUT)
GPIO.setup(GPIO_echo1, GPIO.IN)
GPIO.setwarnings(False)

#The sensor 
GPIO_trig2 = 27
GPIO_echo2 = 22

GPIO.setup(GPIO_trig2, GPIO.OUT)
GPIO.setup(GPIO_echo2, GPIO.IN)

#The sensor 
GPIO_trig3 = 5
GPIO_echo3 = 6

GPIO.setup(GPIO_trig3, GPIO.OUT)
GPIO.setup(GPIO_echo3, GPIO.IN)

def distance():
    GPIO.output(GPIO_trig1, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_trig1, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_echo1)==0:
        StartTime = time.time()

    while GPIO.input(GPIO_echo1)==1:
        StopTime = time.time()

    TimeE = StopTime - StartTime

    dist = (TimeE*34300)/2

    return dist

def distance2():
    GPIO.output(GPIO_trig2, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_trig2, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_echo2)==0:
        StartTime = time.time()

    while GPIO.input(GPIO_echo2)==1:
        StopTime = time.time()

    TimeE = StopTime - StartTime

    dist = (TimeE*34300)/2

    return dist

def distance3():
    GPIO.output(GPIO_trig3, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_trig3, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_echo3)==0:
        StartTime = time.time()

    while GPIO.input(GPIO_echo3)==1:
        StopTime = time.time()

    TimeE = StopTime - StartTime

    dist = (TimeE*34300)/2

    return dist
if __name__ == '__main__':
    try:
        while True:
            front = distance()
            left = distance2()
            right = distance3()
            print("Measured Distance1 = "+str(front)+" cm")
            print("Measured Distance2 = "+str(left)+" cm")
            print("Measured Distance3 = "+str(right)+" cm")
            #time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()

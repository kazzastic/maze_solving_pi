import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#MOTOR NUMBER 1
in1 = 12
in2 = 16
en = 20
temp1 = 1

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
value=100
p = GPIO.PWM(en, 1000)
p.start(value)

#MOTOR NUMBER 2
in3 = 24
in4 = 23
em = 25

GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(em, GPIO.OUT)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

q = GPIO.PWM(em, 1000)
q.start(value)

GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
try:
    while True:
        if(GPIO.input(14) == False and GPIO.input(15) == False):
            GPIO.output(in1, False)
            GPIO.output(in2, True)
            GPIO.output(in3, True)
            GPIO.output(in4, False)
            print("Straight")
        elif(GPIO.input(14) == True and GPIO.input(15) == False):
            GPIO.output(in1, False)
            GPIO.output(in2, True)
            GPIO.output(in3, False)
            GPIO.output(in4, False)
            print("Left")
        elif(GPIO.input(14) == False and GPIO.input(15) == True):
            GPIO.output(in1, True)
            GPIO.output(in2, True)
            GPIO.output(in3, True)
            GPIO.output(in4, False)
            print("Right")
        else:
            GPIO.output(in1, True)
            GPIO.output(in2, True)
            GPIO.output(in3, False)
            GPIO.output(in4, False)
            print("Back")
    
except KeyboardInterrupt:
    print("\nwow dude really?wow!")
    GPIO.cleanup()

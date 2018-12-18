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

p = GPIO.PWM(en, 1000)
p.start(100)

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
q.start(100)

GPIO.setup(14, GPIO.IN)
#GPIO.setup(, GPIO.IN)
try:
    while True:
        if(GPIO.input(14) == False):
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            print("forward")
        elif(GPIO.input(14) == True):
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
            print("this shall not move!")
        else:
            print("why?")
    '''        
    while True:
        if(GPIO.input(14) == False):
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            print("forward")
        elif(GPIO.input(14) == True):
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
            print("this shall not move!")
        else:
            print("why?")
    '''      
except KeyboardInterrupt:
    print("wow dude really?wow!")
    GPIO.cleanup()

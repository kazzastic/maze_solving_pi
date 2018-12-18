import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_trig = 5
GPIO_echo = 6

GPIO.setup(GPIO_trig, GPIO.OUT)
GPIO.setup(GPIO_echo, GPIO.IN)
GPIO.setwarnings(False)

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



def distance():
    GPIO.output(GPIO_trig, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_trig, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_echo)==0:
        StartTime = time.time()

    while GPIO.input(GPIO_echo)==1:
        StopTime = time.time()

    TimeE = StopTime - StartTime

    dist = (TimeE*34300)/2

    return dist

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured Distance = "+str(dist)+" cm")
            if (dist > 20):
                GPIO.output(in1, False)
                GPIO.output(in2, True)
                GPIO.output(in3, True)
                GPIO.output(in4, False)
                print("Straight")
            else:
                GPIO.output(in1, False)
                GPIO.output(in2, True)
                GPIO.output(in3, False)
                GPIO.output(in4, False)
                print("Left")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()

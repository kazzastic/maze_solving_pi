import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#The sensor in the front
GPIO_trig1 = 5
GPIO_echo1 = 6

GPIO.setup(GPIO_trig1, GPIO.OUT)
GPIO.setup(GPIO_echo1, GPIO.IN)
GPIO.setwarnings(False)

#The sensor on the left
GPIO_trig2 = 19
GPIO_echo2 = 26

GPIO.setup(GPIO_trig2, GPIO.OUT)
GPIO.setup(GPIO_echo2, GPIO.IN)

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
<<<<<<< HEAD
value=25
=======
value=30
'''
PWN means the speed of the rotation of the wheels/motors of your robot 
'''
>>>>>>> 3311dc58c90c36602d375d33170e436c8381dc68
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

'''
Sets the PWM meaning how fast the tires/ motors are supposed to move 
'''
q = GPIO.PWM(em, 1000)
q.start(value)


'''
Distance is being calculated for the Ultrasonic Sensor on the front
'''
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
'''
Distance is being calculated for the Ultrasonic Sensor on the left
'''
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


if __name__ == '__main__':
    try:
        while True:
            front = distance()
            left = distance2()
            print("Measured Distance = "+str(front)+" cm")
            print("Measured Distance = "+str(left)+" cm")
<<<<<<< HEAD

            if(front < 10 and left > 10):
                GPIO.output(in1, True)  #counter_clockwise
                GPIO.output(in2, False)
                GPIO.output(in3, True)
                GPIO.output(in4, False) #counter_clockwise
=======
            if (front < 25 or left < 25):
                GPIO.output(in1, False)
                GPIO.output(in2, True)
                GPIO.output(in3, False)
                GPIO.output(in4, False)
                print("Left")
            elif (front < 11 and left > 11):
                GPIO.output(in1, False)
                GPIO.output(in2, True)
                GPIO.output(in3, False)
                GPIO.output(in4, False)
>>>>>>> 3311dc58c90c36602d375d33170e436c8381dc68
                print("Left")
                time.sleep(0.6)
            elif(front <10 and left < 10):
                GPIO.output(in1, False) #counter_clockwise
                GPIO.output(in2, True)
                GPIO.output(in3, False)
                GPIO.output(in4, True) #counter_clockwise
                print("Right")
                time.sleep(0.6)
            else:
                GPIO.output(in1, False) #counter_clockwise
                GPIO.output(in2, True)
                GPIO.output(in3, True)
                GPIO.output(in4, False) #counter_clockwise
                print("Straight")
<<<<<<< HEAD
            #time.sleep(1)
=======
            time.sleep(0.5)
>>>>>>> 3311dc58c90c36602d375d33170e436c8381dc68

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()

import RPi.GPIO as GPIO
import time

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

value=25
'''
PWN means the speed of the rotation of the wheels/motors of your robot 
'''
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


if __name__ == '__main__':
    try:
        while True:
            GPIO.output(in1, False) #counter_clockwise
            GPIO.output(in2, True)
            GPIO.output(in3, True)
            GPIO.output(in4, False) #counter_clockwise
            print("Straight")
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()

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

#The sensor on the right
GPIO_trig3 = 27
GPIO_echo3 =22

GPIO.setup(GPIO_trig3, GPIO.OUT)
GPIO.setup(GPIO_echo3, GPIO.IN)

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

value=40
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


'''
Distance is being calculated for the Ultrasonic Sensor on the front
'''
def distance():
    
    GPIO.output(GPIO_trig1, False)                 #Set TRIG as LOW
    print "Waitng For Sensor To Settle"
    time.sleep(2)                            #Delay of 2 seconds

    GPIO.output(GPIO_trig1, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(GPIO_trig1, False)                 #Set TRIG as LOW

    while GPIO.input(GPIO_echo1)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(GPIO_echo1)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points

    if distance > 2 and distance < 400:      #Check whether the distance is within range
        print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    else:
        print "Out Of Range"                   #display out of range
        
    return distance
'''
Distance is being calculated for the Ultrasonic Sensor on the left
'''
def distance2():
 GPIO.output(GPIO_trig2, False)                 #Set TRIG as LOW
    print "Waitng For Sensor To Settle"
    time.sleep(2)                            #Delay of 2 seconds

    GPIO.output(GPIO_trig2, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(GPIO_trig2, False)                 #Set TRIG as LOW

    while GPIO.input(GPIO_echo2)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(GPIO_echo2)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points

    if distance > 2 and distance < 400:      #Check whether the distance is within range
        print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    else:
        print "Out Of Range"
    return distance
'''
Distance is being calculated for the Ultrasonic Sensor on the right 
'''
def distance3():
    
    GPIO.output(GPIO_trig3, False)                 #Set TRIG as LOW
    print "Waitng For Sensor To Settle"
    time.sleep(2)                            #Delay of 2 seconds

    GPIO.output(GPIO_trig3, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(GPIO_trig3, False)                 #Set TRIG as LOW

    while GPIO.input(GPIO_echo3)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(GPIO_echo3)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points

    if distance > 2 and distance < 400:      #Check whether the distance is within range
        print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    else:
        print "Out Of Range"   

    return distance

if __name__ == '__main__':
    try:
        while True:
            front = distance3()
            left = distance2()
            right = distance()
            print("Measured Distance = "+str(front)+" cm")
            print("Measured Distance = "+str(left)+" cm")
            print("Measured Distance = "+str(right)+" cm")
            
            if(front < 10 and left >10 and right >10):
                if(right > left):
                    GPIO.output(in1, False) #counter_clockwise
                    GPIO.output(in2, True)
                    GPIO.output(in3, False)
                    GPIO.output(in4, True) #counter_clockwise
                    print("Right")
                    time.sleep(0.6)
                else:
                    GPIO.output(in1, True)  #counter_clockwise
                    GPIO.output(in2, False)
                    GPIO.output(in3, True)
                    GPIO.output(in4, False) #counter_clockwise
                    print("Left")
                    time.sleep(0.6)
            elif(front < 10 and left < 10 and right > 10):
                GPIO.output(in1, False) #counter_clockwise
                GPIO.output(in2, True)
                GPIO.output(in3, False)
                GPIO.output(in4, True) #counter_clockwise
                print("Right")
                time.sleep(0.6)
            elif(front < 10 and left > 10 and right < 10):
                GPIO.output(in1, True)  #counter_clockwise
                GPIO.output(in2, False)
                GPIO.output(in3, True)
                GPIO.output(in4, False) #counter_clockwise
                print("Left")
                time.sleep(0.6)
            else:
                GPIO.output(in1, False) #counter_clockwise
                GPIO.output(in2, True)
                GPIO.output(in3, True)
                GPIO.output(in4, False) #counter_clockwise
                print("Straight")
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()

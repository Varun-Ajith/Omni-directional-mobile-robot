import RPi.GPIO as GPIO
import time

# Define pin numbers
frontEchoPin = 7
frontTriggerPin = 6
leftEchoPin = 11
leftTriggerPin = 10
rightEchoPin = 9
rightTriggerPin = 8
lrightTriggerPin = 22
lrightEchoPin = 23
lleftTriggerPin = 24
lleftEchoPin = 25

motorL1P = 52
motorL1N = 53
motorL2P = 54
motorL2N = 55
motorR1P = 56
motorR1N = 57
motorR2P = 58
motorR2N = 59

# Define maximum distances
maxFrontDistance = 25.00
maxLeftDistance = maxRightDistance = 20.00
maxLeftLateral = maxRightLateral = 10.00

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(frontTriggerPin, GPIO.OUT)
GPIO.setup(frontEchoPin, GPIO.IN)
GPIO.setup(leftTriggerPin, GPIO.OUT)
GPIO.setup(leftEchoPin, GPIO.IN)
GPIO.setup(rightTriggerPin, GPIO.OUT)
GPIO.setup(rightEchoPin, GPIO.IN)
GPIO.setup(lrightTriggerPin, GPIO.OUT)
GPIO.setup(lrightEchoPin, GPIO.IN)
GPIO.setup(lleftTriggerPin, GPIO.OUT)
GPIO.setup(lleftEchoPin, GPIO.IN)

GPIO.setup(motorL1P, GPIO.OUT)
GPIO.setup(motorL1N, GPIO.OUT)
GPIO.setup(motorL2P, GPIO.OUT)
GPIO.setup(motorL2N, GPIO.OUT)
GPIO.setup(motorR1P, GPIO.OUT)
GPIO.setup(motorR1N, GPIO.OUT)
GPIO.setup(motorR2P, GPIO.OUT)
GPIO.setup(motorR2N, GPIO.OUT)


def moveBackward():
    print("Backward.")
    GPIO.output(motorL1P, GPIO.LOW)
    GPIO.output(motorL1N, GPIO.HIGH)
    GPIO.output(motorL2P, GPIO.LOW)
    GPIO.output(motorL2N, GPIO.HIGH)
    GPIO.output(motorR1P, GPIO.LOW)
    GPIO.output(motorR1N, GPIO.HIGH)
    GPIO.output(motorR2P, GPIO.LOW)
    GPIO.output(motorR2N, GPIO.HIGH)


def moveForward():
    print("Forward.")
    GPIO.output(motorL1P, GPIO.HIGH)
    GPIO.output(motorL1N, GPIO.LOW)
    GPIO.output(motorL2P, GPIO.HIGH)
    GPIO.output(motorL2N, GPIO.LOW)
    GPIO.output(motorR1P, GPIO.HIGH)
    GPIO.output(motorR1N, GPIO.LOW)
    GPIO.output(motorR2P, GPIO.HIGH)
    GPIO.output(motorR2N, GPIO.LOW)


def moveLeft():
    print("Left.")
    GPIO.output(motorL1P, GPIO.LOW)
    GPIO.output(motorL1N, GPIO.HIGH)
    GPIO.output(motorL2P, GPIO.HIGH)
    GPIO.output(motorL2N, GPIO.LOW)
    GPIO.output(motorR1P, GPIO.HIGH)
    GPIO.output(motorR1N, GPIO.LOW)
    GPIO.output(motorR2P, GPIO.LOW)
    GPIO.output(motorR2N, GPIO.HIGH)

def moveRight():
    print("Right.")
    GPIO.output(motorL1P, GPIO.HIGH)
    GPIO.output(motorL1N, GPIO.LOW)
    GPIO.output(motorL2P, GPIO.LOW)
    GPIO.output(motorL2N, GPIO.HIGH)
    GPIO.output(motorR1P, GPIO.LOW)
    GPIO.output(motorR1N, GPIO.HIGH)
    GPIO.output(motorR2P, GPIO.HIGH)
    GPIO.output(motorR2N, GPIO.LOW)

def moveLeftLateral():
    print("Left Lateral.")
    GPIO.output(motorL1P, GPIO.LOW)
    GPIO.output(motorL1N, GPIO.HIGH)
    GPIO.output(motorL2P, GPIO.HIGH)
    GPIO.output(motorL2N, GPIO.LOW)
    GPIO.output(motorR1P, GPIO.LOW)
    GPIO.output(motorR1N, GPIO.HIGH)
    GPIO.output(motorR2P, GPIO.HIGH)
    GPIO.output(motorR2N, GPIO.LOW)

def moveRightLateral():
    print("Right Lateral.")
    GPIO.output(motorL1P, GPIO.HIGH)
    GPIO.output(motorL1N, GPIO.LOW)
    GPIO.output(motorL2P, GPIO.LOW)
    GPIO.output(motorL2N, GPIO.HIGH)
    GPIO.output(motorR1P, GPIO.HIGH)
    GPIO.output(motorR1N, GPIO.LOW)
    GPIO.output(motorR2P, GPIO.LOW)
    GPIO.output(motorR2N, GPIO.HIGH)

def checkDistance(triggerPin, echoPin):
    GPIO.output(triggerPin, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(triggerPin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(triggerPin, GPIO.LOW)
    pulse_start = time.time()
    while GPIO.input(echoPin) == 0:
        pulse_start = time.time()
    pulse_end = time.time()
    while GPIO.input(echoPin) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)


# Main loop
try:
    while True:
        frontDistanceCm = checkDistance(frontTriggerPin, frontEchoPin)
        if frontDistanceCm < maxFrontDistance:
            print("Too close")
            leftDistanceCm = checkDistance(leftTriggerPin, leftEchoPin)
            if leftDistanceCm < maxLeftDistance:
                print("Left too close")
            rightDistanceCm = checkDistance(rightTriggerPin, rightEchoPin)
            if rightDistanceCm < maxRightDistance:
                print("Right too close")
            lleftDistanceCm = checkDistance(lleftTriggerPin, lleftEchoPin)
            if lleftDistanceCm < maxLeftLateral:
                print("Lateral Left too close")
            lrightDistanceCm = checkDistance(lrightTriggerPin, lrightEchoPin)
            if lrightDistanceCm < maxRightLateral:
                print("Lateral Right too close")
        else:
            print("OK")
            moveForward()
        time.sleep(0.09) 
except KeyboardInterrupt:
    GPIO.cleanup()

import RPi.GPIO as GPIO
import time

pin = 12
pin_l = 32

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin_l, GPIO.OUT)

q = GPIO.PWM(pin, 200)
L = GPIO.PWM(pin_l, 200)
q.start(0)
L.start(0)

try:
    while True:
        L.ChangeFrequency(30)
        q.ChangeFrequency(300)
        for c in range(0, 101, 2):
            L.ChangeDutyCycle(100-c)
            q.ChangeDutyCycle(c)
            time.sleep(0.03)

        time.sleep(2)

        for c in range(0, 101 , 2):
            q.ChangeDutyCycle(100-c)
            L.ChangeDutyCycle(c)
            time.sleep(0.03)

        time.sleep(2)

except KeyboardInterrupt:
    L.stop()
    q.stop()
    GPIO.cleanup()
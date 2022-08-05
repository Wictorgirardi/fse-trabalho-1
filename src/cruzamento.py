import RPi.GPIO as GPIO

from time import sleep
from threading import Thread

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(1, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


def semaforo_1():
  while True:
    GPIO.output(12, GPIO.HIGH)
    sleep(1)
    GPIO.output(12, GPIO.LOW)

    GPIO.output(20, GPIO.HIGH)
    sleep(15)
    GPIO.output(20, GPIO.LOW)

    GPIO.output(16, GPIO.HIGH)
    sleep(3)
    GPIO.output(16, GPIO.LOW)

    GPIO.output(12, GPIO.HIGH)
    sleep(10)
    GPIO.output(12, GPIO.LOW)
  
def semaforo_2():
  while True:
    GPIO.output(21, GPIO.HIGH)
    sleep(15)
    GPIO.output(21, GPIO.LOW)

    GPIO.output(1, GPIO.HIGH)
    sleep(8)
    GPIO.output(1, GPIO.LOW)

    GPIO.output(26, GPIO.HIGH)
    sleep(3)
    GPIO.output(26, GPIO.LOW)

    GPIO.output(21, GPIO.HIGH)
    sleep(15)
    GPIO.output(21, GPIO.LOW)
    

semaforo_1 = Thread(target=semaforo_1)
semaforo_1.start()

semaforo_2 = Thread(target=semaforo_2)
semaforo_2.start()

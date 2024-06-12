# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

def rotate_degrees_1(degrees):
    steps_per_revolution = 512  # 假設一次完整轉動需要 2048 步
    steps = int(steps_per_revolution * degrees / 360)  # 計算需要旋轉的步數
    
    for _ in range(steps):
        for halfstep in range(len(seq1)):
            for pin in range(len(Pin)):
                GPIO.output(Pin[pin], seq1[halfstep][pin])
            time.sleep(0.01)

def rotate_degrees_2(degrees):
    steps_per_revolution = 512  # 假設一次完整轉動需要 2048 步
    steps = int(steps_per_revolution * degrees / 360)  # 計算需要旋轉的步數
    
    for _ in range(steps):
        for halfstep in range(len(seq2)):
            for pin in range(len(Pin)):
                GPIO.output(Pin[pin], seq2[halfstep][pin])
            time.sleep(0.01)

Pin = [31,33,35,37]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)



# Define sequence for 28BYJ-48 stepper motor
seq1 = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]
seq2 = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1]
]

while True:
    # rotate_degrees_1(6)
    print('逆時鐘')
    for i in range(5):
        rotate_degrees_1(6)
        time.sleep(0.01)
    print('順時鐘')
    for i in range(5):
        rotate_degrees_2(6)
        time.sleep(0.01)

GPIO.cleanup()

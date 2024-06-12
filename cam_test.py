from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
num = 0
while True:
    camera.capture(f'imgs/image{num}.jpg')
    num+=1
    print(f'img{num}OK')
    sleep(2)
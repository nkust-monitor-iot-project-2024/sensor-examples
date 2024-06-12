import RPi.GPIO as GPIO
import time

# 設定GPIO模式
GPIO.setmode(GPIO.BOARD)

# 設定感測器的GPIO引腳編號
sensor_pin = 11

# 設定GPIO引腳為輸入模式
GPIO.setup(sensor_pin, GPIO.IN)

print("按下Ctrl+C退出程式")

try:
    while True:
        # 讀取GPIO引腳的狀態
        # sensor_status = GPIO.input(sensor_pin)
        
        if GPIO.input(sensor_pin) ==1:
            print("偵測到有人經過!")
        else:
            print("沒有偵測到人")
        
        time.sleep(0.5)

except KeyboardInterrupt:
    print("程式結束")

finally:
    GPIO.cleanup()

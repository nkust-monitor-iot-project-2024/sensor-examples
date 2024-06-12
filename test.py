import subprocess
import time
import re
from balance import mpu6050
import RPi.GPIO as GPIO
from picamera import PiCamera
import pyaudio
import wave

# 麥克風前置
chunk = 1024                     # 記錄聲音的樣本區塊大小
sample_format = pyaudio.paInt16  
channels = 2                     # 聲道數量
fs = 22050                       # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
mp3_num = 1
seconds = 10                     # 錄音秒數
filename = "audio"            # 錄音檔名

# 相機前置
camera = PiCamera()
img_num = 1

# 啟用藍牙探測
subprocess.call('sudo bluetoothctl discoverable on', shell=True)

# 平衡感測前置
mpu = mpu6050(0x68)

# 紅外線前置
GPIO.setmode(GPIO.BOARD)
sensor_pin = 11
GPIO.setup(sensor_pin, GPIO.IN)

# 開啟 PyAudio 串流
p = pyaudio.PyAudio()
stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk*2, input=True)

while True:
    # 檢查藍牙裝置是否連接
    output = subprocess.run(['sudo', 'bluetoothctl', 'info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if output.returncode != 0:
        # 開始陀螺儀偵測
        gyro_data = mpu.get_gyro_data()
        if gyro_data['x']>=15 or gyro_data['y']>=15 or gyro_data['z']>=15:
            print('偵測到裝置被移動!開啟相機以及麥克風')
            #拍照開始
            camera.capture(f'imgs/image{img_num}.jpg')
            img_num+=1
            print(f'img{img_num}OK')
            time.sleep(0.5)

            #麥克風開啟
            print('開啟麥克風')
            frames = []
            for _ in range(0, int(fs / chunk * seconds)):
                data = stream.read(chunk)
                frames.append(data)

            print('開始寫入')
            with wave.open(f'{filename}{mp3_num}.mp3', 'wb') as wf:
                wf.setnchannels(channels)
                wf.setsampwidth(p.get_sample_size(sample_format))
                wf.setframerate(fs)
                wf.writeframes(b''.join(frames))

            mp3_num+=1
            print('錄音完畢')

        #開始紅外線偵測
        if GPIO.input(sensor_pin) ==1:
            print("偵測到有人經過!開啟相機")
            #拍照開始
            camera.capture(f'imgs/image{img_num}.jpg')
            img_num+=1
            print(f'img{img_num}OK')
            time.sleep(1)

    else:
        # 如果有藍芽連上 顯示裝置名稱
        pattern = r'Name: (.*)'
        match = re.search(pattern, str(output.stdout, 'utf-8'))
        print(f'Connected to: {match.group(1)}')
        time.sleep(1)
    time.sleep(0.1)

# 關閉 PyAudio 串流
stream.stop_stream()
stream.close()
p.terminate()

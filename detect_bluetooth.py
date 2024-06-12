import subprocess
import time
import re

# 啟用藍牙探測
subprocess.call('sudo bluetoothctl discoverable on', shell=True)

while True:
    try:
        # 檢查藍牙裝置是否連接
        output = subprocess.check_output('sudo bluetoothctl info', shell=True, universal_newlines=True)
        if 'Connected: yes' in output:
            # Get the device name
            pattern = r'Name: (.*)'
            match = re.search(pattern, output)
            print(f'Connected to: {match.group(1)}')
        else:
            print('No devices connected.')
    except subprocess.CalledProcessError:
        print('Error: Unable to get Bluetooth device info.')
    
    time.sleep(1)
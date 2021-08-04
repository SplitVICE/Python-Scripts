# This script is meant to keep Heroku dynos awake by making a request every 25 minutes

import time
import subprocess

sleep_time = 1500 # 1500 == 25 minutes
website = ""

def cmd(command):
    try:
        subprocess.call(command,shell=True)
    except:
        print("Error at cmd " + command)

while True:
    cmd('curl ' + website)
    time.sleep(sleep_time)

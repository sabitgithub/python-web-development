"""
Digital Clock In Console Mod
"""

import time,os

while True:
    os.system('cls')
    lt=time.localtime()
    result=time.strftime('%I:%M:%S %p',lt)
    print(result)
    time.sleep(1)
    
import os
import sys
from time import sleep

from ppadb.client import Client

os.system('"..\\adb\.\\adb start-server"')

adb = Client(host="127.0.0.1", port=5037)
devices = adb.devices()

if len(devices) == 0:
    os.system('start cmd /c ..\\pyscrcpy\.\\adb  kill-server')
    sys.exit('No device!')

DEVICE = devices[0]

DEVICE.shell("settings put system screen_brightness 0") #* Set screen brightness to 0 to use less energy, heat less etc.

MONEYX = int(input("input money counter X: ")) #! Use developer mode to know exact X and Y
MONEYY = int(input("input money counter Y: "))
CLOSEX = int(input("input close icon X (default 100): "))
CLOSEY = int(input("input close icon Y (default 180): "))
SWIPEX = int(input("input swipe X (default 550): "))
SWIPEY1 = int(input("input swipe Y 1 (default 2200): "))
SWIPEY2 = int(input("input swipe Y 2 (default 1000): "))

def main():
    DEVICE.shell(f"input tap {MONEYX} {MONEYY}") # input tap x y #* tap on money counter
    sleep(0.75)
    DEVICE.shell(f"input touchscreen swipe {SWIPEX} {SWIPEY2} {SWIPEX} {SWIPEY1} 100") # input touchscreen swipe x0 y0 x1 y1 duration #* swipe from bottom to top to show ads
    sleep(0.2)
    DEVICE.shell(f"input touchscreen swipe {SWIPEX} {SWIPEY2} {SWIPEX} {SWIPEY1} 100") # input touchscreen swipe x0 y0 x1 y1 duration #* swipe from bottom to top to show ads
    sleep(0.3)
    DEVICE.shell(f"input tap {CLOSEX} {CLOSEY}") # input tap x y #* tap on back button

while True:
    main()

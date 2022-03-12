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

device = devices[0]

device.shell("settings put system screen_brightness 0") # Set screen brightness to 0 to use less energy, heat less etc.

DISPLAYWIDTH = int(device.shell("dumpsys display | grep mDisplayWidth").strip().split("=")[1])
DISPLAYHEIGHT = int(device.shell("dumpsys display | grep mDisplayHeight").strip().split("=")[1])

MONEYX = int(DISPLAYWIDTH*0.8)
MONEYY = int(DISPLAYHEIGHT*0.265)

BACKX = int(DISPLAYWIDTH*0.075)
BACKY = int(DISPLAYHEIGHT*0.065)

def main():
    device.shell(f"input tap {MONEYX} {MONEYY}") # input tap x y #* tap on money counter
    sleep(1)
    device.shell(f"input touchscreen swipe {DISPLAYWIDTH*0.5} {DISPLAYHEIGHT*0.9} {DISPLAYWIDTH*0.5} {DISPLAYHEIGHT*0.4} 100") # input touchscreen swipe x0 y0 x1 y1 duration #* swipe from bottom to top to show ads
    sleep(0.2)
    device.shell(f"input touchscreen swipe {DISPLAYWIDTH*0.5} {DISPLAYHEIGHT*0.9} {DISPLAYWIDTH*0.5} {DISPLAYHEIGHT*0.4} 100") # input touchscreen swipe x0 y0 x1 y1 duration #* swipe from bottom to top to show ads
    sleep(0.3)
    device.shell(f"input tap {BACKX} {BACKY}") # input tap x y #* tap on back button

while True:
    main()

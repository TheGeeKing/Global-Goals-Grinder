import os
import sys
from time import sleep

import cv2
import numpy as np
from ppadb.client import Client
from pyautogui import click, screenshot

# os.system('start cmd /c ..\\adb\.\\adb start-server')
os.system('start cmd /c ..\\pyscrcpy\.\\adb start-server')
os.system('start cmd /c ..\\pyscrcpy\.\\scrcpy.exe --max-fps 20 -b 6M')

adb = Client(host="127.0.0.1", port=5037)
devices = adb.devices()

if len(devices) == 0:
    os.system('start cmd /c ..\\pyscrcpy\.\\adb  kill-server')
    sys.exit('No device!')

device = devices[0]

device.shell("input keyevent 164")
device.shell("settings put system screen_brightness 0")

def max_confidence(liste):
    files_results=[]
    for element in liste:
        for ele in element:
            files_results.extend(e for e in ele if isinstance(e, float))
    higher=max(files_results)
    index = files_results.index(higher)
    return liste[index]


def take_screenshot():
    screenshot_screen = screenshot()
    screenshot_screen = np.array(screenshot_screen)
    screenshot_screen = cv2.cvtColor(np.array(screenshot()), cv2.COLOR_BGR2GRAY)
    return screenshot_screen


def check_screenshot(file):
    results = []
    for ele in file:
        results.append([ele])
        screenshot_screen = take_screenshot()
        video = cv2.imread(ele)
        video = np.array(video)
        video = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

        screenshot_main = cv2.matchTemplate(screenshot_screen, video, cv2.TM_CCOEFF_NORMED)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(screenshot_main)
        index = len(results)-1
        results[index].insert(1, [maxVal, maxLoc])
    data = max_confidence(results)
    return data[1][0], data[1][1] #* returns maxVal, maxLoc


def files(folder):
    if folder == "video":
        folder = "video"
    elif folder == "close":
        folder = "close"
    elif folder == "ok":
        folder = "ok"
    else: raise FileNotFoundError("Folder not found")
    files_results=[]
    for ele in os.listdir(folder):
        full_path = os.path.join(folder, ele)
        if os.path.isfile(full_path):
            files_results.append(full_path)
    return files_results

#* Defines files paths
video_files = files("video")
close_files = files("close")
ok_files = files("ok")

# TODO: check if previous step worked, timeout if no 'close' button and check through states and continue normal behaviour or stop after a certain time
def main():
    print("Scanning for the video logo")
    (video_maxVal, video_maxLoc) = check_screenshot(file=video_files)
    print(video_maxVal)
    if video_maxVal>0.95:
        print("Found the video logo")
        (startX, startY) = video_maxLoc
        click(startX+10, startY+10)
        click(startX+10, startY+10)
        sleep(1)
        (close_maxVal, close_maxLoc) = check_screenshot(file=close_files)
        while close_maxVal<0.95:
            print("Waiting for the close button to appear")
            print(close_maxVal)
            sleep(0.5)
            screenshot_close = check_screenshot(file=close_files)
        print(close_maxVal)
        print("Clicking on close button")
        (startX, startY) = close_maxLoc
        click(startX+10, startY+10)
        sleep(0.5)
        (ok_maxVal, ok_maxLoc) = check_screenshot(file=ok_files)
        if ok_maxVal>0.95:
            print("Clicking on 'ok' button")
            (startX, startY) = ok_maxLoc
            click(startX+15, startY+15)
            sleep(0.1)

while True:
    main()

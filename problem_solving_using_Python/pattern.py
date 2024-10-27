"""Draw pattern using pyAutoGui"""
import pyautogui
import time

n = int(input())

time.sleep(2)

for i in range(1, n+1):
    pyautogui.typewrite('#' *i)
    pyautogui.press('enter')
    # pyautogui.typewrite('\n')
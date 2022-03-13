import mouse
import time
from pynput import keyboard
import pyautogui

combination = [
    {keyboard.KeyCode(char="n")},
    {keyboard.KeyCode(char="N")}
]
exitCombination = [
    {keyboard.KeyCode(char="e")},
    {keyboard.KeyCode(char="E")}
]
current = set()


# def execute():
#     pyautogui.hotkey("winleft", "prtsc")


def mouseMovement():
    while True:
        mouse.move(1900, 350, absolute=True, duration=3)
        time.sleep(4)
        mouse.move(2100, 350, absolute=True, duration=3)
        time.sleep(4)


def on_press(key):
    if any([key in COMBO for COMBO in combination]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in combination):
            mouseMovement()


def on_release(key):
    if any([key in COMBO for COMBO in combination]):
        current.remove(key)


def onExit(key):
    if any([key in combo for combo in exitCombination]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in combination):
            exit()


def onExitRelease(key):
    if any([key in COMBO for COMBO in combination]):
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()

# with keyboard.Listener(on_press=onExit, on_release=onExitRelease) as listner:
#     listner.join()
import math
import operator
import time
from functools import reduce
import mouse
import pyautogui
from PIL import Image
from PIL import ImageChops
import firebase_admin
from firebase_admin import credentials

img1 = Image.open(r"C:\Users\NikhilBajpai\Pictures\Screenshots\Screenshot (12).png")

# img2 = Image.open("Screenshot (7).png")
img2 = Image.open(r"C:\Users\NikhilBajpai\Pictures\Screenshots\Screenshot (13).png")


def rmsDiff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
                            map(lambda h, i: h * (i ** 2), h, range(256))
                            ) / (float(im1.size[0]) * im1.size[1]))


print(rmsDiff(img1, img2))


def TakeScreenShot():
    pyautogui.hotkey("winleft", "prtsc")


def mouseMovement():
    while True:
        mouse.move(1900, 350, absolute=True, duration=3)
        rmsDiff()
        time.sleep(4)
        print("hehehaha")
        mouse.move(2100, 350, absolute=True, duration=3)
        time.sleep(4)
        print("hehehaha444444")


print(mouseMovement())

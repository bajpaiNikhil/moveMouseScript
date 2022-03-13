from functools import reduce

import mouse
import time
from pynput import keyboard
import pyautogui
from PIL import Image
from PIL import ImageChops
import math, operator

img1 = Image.open("Screenshot (6).png")

img2 = Image.open("Screenshot (7).png")


# def equal(img1, img2):
#     print(ImageChops.difference(img1, img2).getbbox())
#     return ImageChops.difference(img1, img2).getbbox() is None
def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
                            map(lambda h, i: h * (i ** 2), h, range(256))
                            ) / (float(im1.size[0]) * im1.size[1]))


print(rmsdiff(img1, img2))


def mouseMovement():
    while True:
        mouse.move(1900, 350, absolute=True, duration=3)
        time.sleep(4)

        mouse.move(2100, 350, absolute=True, duration=3)
        time.sleep(4)

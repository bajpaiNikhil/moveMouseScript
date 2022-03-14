import math
import operator
import time
from functools import reduce
import mouse
import pyautogui
import pyscreenshot
from PIL import Image
from PIL import ImageChops
import firebase_admin
from firebase_admin import credentials
import os
from firebase_admin import db

import config

cred = credentials.Certificate(config.FIREBASE_CONFIG_KEY)

databaseApp = firebase_admin.initialize_app(cred, {
    "databaseURL": config.DATABASE_URL
})


def writeData():
    ref = db.reference(f"/")
    change = "ScreenChange"
    ref.update({
        change: {
            "About": "The rms difference between two image is not same",
            "Threat": "Now that's and avenger level threat"
        }
    })
    print("data written in firebase")


def rmsDiff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2).histogram()
    # calculate rms
    return math.sqrt(reduce(operator.add,
                            map(lambda h, i: h * (i ** 2), h, range(256))
                            ) / (float(im1.size[0]) * im1.size[1]))


def takeScreenShot():
    image = pyscreenshot.grab()  # can pass the size of the box will do once it is completed
    image.save(fr"C:\Users\NikhilBajpai\Pictures\Screenshots\iamStupid{i}.png".format(i))
    # image.save(r"C:\Users\NikhilBajpai\Pictures\Screenshots\iamStupid.png") #to take the first screenshot
    print("screenShot done")


def mouseMovement():
    global i
    i = 1
    while True:
        mouse.move(1900, 350, absolute=True, duration=3)
        takeScreenShot()
        img1 = Image.open(
            r"C:\Users\NikhilBajpai\Pictures\Screenshots\iamStupid.png")  # static image do change the file name
        img2 = Image.open(
            fr"C:\Users\NikhilBajpai\Pictures\Screenshots\iamStupid{i}.png".format(i))
        a = rmsDiff(img1, img2)
        if a > 1.0:
            print("break reached " + str(a) + str(i))
            writeData()
            break
        else:
            os.remove(fr"C:\Users\NikhilBajpai\Pictures\Screenshots\iamStupid{i}.png".format(i))
            i += 1
            print("pass reached" + str(a) + str(i))
            pass
        time.sleep(4)
        print("hehehahaFirstSleep")
        mouse.move(1950, 350, absolute=True, duration=3)
        time.sleep(4)
        print("hehehahaAfterSleep")


if __name__ == '__main__':
    mouseMovement()

import RPi.GPIO as GPIO
from time import sleep, asctime, localtime
from PIL import Image
from time import sleep
from pathlib import Path
import base64
import os
# PiCamera
from picamera import PiCamera
# import database
import config.database as DataBase
# base_dir
base_dir_image = 'images/'
# RPi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

## event gpio
GPIO.add_event_detect(4, GPIO.RISING, detectGPIO)


def detectGPIO():
    path = camera()
    main(path)


def camera():

    # 217 photo
    # name file
    name = localtime().tm_mday.__str__()+'-'+localtime().tm_mon.__str__() + \
        '-'+localtime().tm_year.__str__()
    # path file
    pathPhoto = base_dir_image+'photo'+name+'.jpg'
    camera = PiCamera()
    print('start camera')
    camera.start_preview()
    sleep(3)
    camera.capture(pathPhoto)
    camera.stop_preview()
    print('stop camera')
    return pathPhoto


def main(path):
    try:
        print('name path camera')
        print(path)
        # remove file
        # os.remove(pathPhoto)
        print('****** info file ******')
        image = Path(path)
        print(image.name)
        print(image.suffix)
        print(image.stem)

        if not image.exists():
            print("Oops, file doesn't exist!")
        else:
            print("Yay, the file exists!")
            print(os.path.join(path))
            im = Image.open(os.path.join(path))
            print('Información imagen photo')
            print(im)
            print(im.show())

            with open(os.path.join(path), "rb") as img_file:
                string_img = base64.b64encode(img_file.read())
                # string_img base64
                print('save database files photo')
                DataBase.saveImage(path, string_img)
    finally:
        pass

# # And... nothing more to do. let's wait.
while True:
    sleep(10)

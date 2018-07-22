import cv2
import sys, os

__author__ = 'N.A. Supun Kavinda'


class ImageRead:

    def __init__(self):
        pass

    def image_reader(self):
        # img_path = path + "Supun Kavinda.png"
        # img_path = path + "bee patterns!1.png"
        # img_path = path + "bee patterns pvt ltd.png"
        # img_path = path + "address1.png"

        current_path = os.path.abspath(sys.modules[ImageRead.__module__].__file__)
        current_path = current_path.replace('Scanner\ImageRead.py', '') + 'QRImages\\frame1.png'

        img = cv2.imread(current_path, cv2.IMREAD_GRAYSCALE)
        return img

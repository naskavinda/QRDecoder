import cv2

__author__ = 'N.A. Supun Kavinda'


class ThresholdBinaryInvAndOTSU:

    def __init__(self, image):
        self.__image = image

    def add_threshold(self):
        th = 0
        max_val = 255
        return cv2.threshold(self.__image, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

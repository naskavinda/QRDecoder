from Mask.ReadMask import ReadMask
from Mask.Pattern01 import Pattern01
from Mask.Pattern02 import Pattern02
from Mask.Pattern03 import Pattern03
from Mask.Pattern04 import Pattern04
from Mask.Pattern05 import Pattern05
from Mask.Pattern06 import Pattern06
from Mask.Pattern07 import Pattern07
from Mask.Pattern08 import Pattern08

__author__ = 'N.A. Supun Kavinda'


class PatternsFactory:
    def __init__(self, binary_matrix):
        self.__binary_matrix = binary_matrix

        read_mask = ReadMask(binary_matrix)
        self.__mask_pattern = read_mask.read_mask()

    def create(self):
        if self.__mask_pattern == '111':
            return Pattern01(self.__binary_matrix)
        elif self.__mask_pattern == '110':
            return Pattern02(self.__binary_matrix)
        elif self.__mask_pattern == '101':
            return Pattern03(self.__binary_matrix)
        elif self.__mask_pattern == '100':
            return Pattern04(self.__binary_matrix)
        elif self.__mask_pattern == '011':
            return Pattern05(self.__binary_matrix)
        elif self.__mask_pattern == '010':
            return Pattern06(self.__binary_matrix)
        elif self.__mask_pattern == '001':
            return Pattern07(self.__binary_matrix)
        elif self.__mask_pattern == '000':
            return Pattern08(self.__binary_matrix)
        else:
            return NotImplementedError('This Pattern is not implement yet.')

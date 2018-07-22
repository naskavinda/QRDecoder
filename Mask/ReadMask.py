__author__ = 'N.A. Supun Kavinda'


class ReadMask:

    def __init__(self, matrix):
        """ This Constructor Required Binary Matrix """
        self.__matrix = matrix

    def read_mask(self):
        return str(self.__matrix[8][2]) + str(self.__matrix[8][3]) + str(self.__matrix[8][4])

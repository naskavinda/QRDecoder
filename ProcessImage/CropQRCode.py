import numpy

__author__ = 'N.A. Supun Kavinda'


class CropQRCode:
    def __init__(self, image):
        self.__image = image

    def __get_first_corner_coordinate(self):

        for i in range(len(self.__image)):
            for j in range(len(self.__image[0])):
                if self.__image[i][j] == 1:
                    return i, j

    def __get_second_corner_coordinate(self):
        for i in range(len(self.__image) - 1, -1, -1):
            for j in range(len(self.__image[0])):
                if self.__image[i][j] == 1:
                    return i, j

    def __get_third_corner_coordinate(self):

        for i in range(len(self.__image)):
            for j in range(len(self.__image[0]) - 1, -1, -1):
                if self.__image[i][j] == 1:
                    return i, j

    def extract_qr_code(self):
        x1, y1 = self.__get_first_corner_coordinate()
        x2, y2 = self.__get_second_corner_coordinate()
        x3, y3 = self.__get_third_corner_coordinate()
        if y1 == y2:
            for i in range(x1):
                self.__image = numpy.delete(self.__image, 0, 0)

            for i in range(len(self.__image) - 1, x2 - x1, -1):
                self.__image = numpy.delete(self.__image, len(self.__image) - 1, 0)

            for j in range(y1):
                self.__image = numpy.delete(self.__image, 0, 1)

            for j in range(len(self.__image[0]) - 1, y3 - y2, -1):
                self.__image = numpy.delete(self.__image, len(self.__image[0]) - 1, 1)

        else:
            return NotImplementedError('This image crop method is not implemented')

        return self.__image

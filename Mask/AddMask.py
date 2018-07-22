from abc import ABC, abstractmethod

__author__ = 'N.A. Supun Kavinda'


class AddMask(ABC):

    def __init__(self, matrix):
        self.__matrix = matrix

    def add_mask(self):
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[0])):
                if not ((i < 9 and (j < 9 or j > len(self.__matrix[0]) - 9)) or (i > len(self.__matrix) - 9 and j < 9)):
                    self.change_pixel(i, j, self.__matrix)
        return self.__matrix

    @abstractmethod
    def change_pixel(self, i, j, matrix):
        pass

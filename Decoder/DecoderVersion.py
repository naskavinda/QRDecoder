from abc import ABC, abstractmethod

from Decoder.Decoder import Decoder

__author__ = 'N.A. Supun Kavinda'


class DecoderVersion(ABC):
    def __init__(self, unmask_matrix):
        self.__unmask_matrix = unmask_matrix

    def decoder(self):
        __encode_mode = self.__get_encode_mode()
        __binary_array = self.__binary_data_array()
        if __encode_mode == '0100':
            return Decoder.decode_bytes_array(__binary_array)
        else:
            return NotImplementedError(__encode_mode, ' This encode mode is not implemented')

    def __get_encode_mode(self):
        rows = len(self.__unmask_matrix)
        cols = len(self.__unmask_matrix[0])
        return str(self.__unmask_matrix[rows - 1][cols - 1]) + str(self.__unmask_matrix[rows - 1][cols - 2]) + str(
            self.__unmask_matrix[rows - 2][cols - 1]) + str(self.__unmask_matrix[rows - 2][cols - 2])

    def __binary_data_array(self):
        """
        This method return total binary values included in word.
        :return: array
        """
        self.data_array = []
        __is_down_to_up = True
        j = len(self.__unmask_matrix[0]) - 1  # cols
        while j > 0:
            if __is_down_to_up:
                for i in range(len(self.__unmask_matrix) - 1, -1, -1):  # rows
                    self.__fill_array(i, j)
                    __is_down_to_up = False
            else:
                for i in range(len(self.__unmask_matrix)):
                    self.__fill_array(i, j)
                    __is_down_to_up = True
            if j is 8:
                j = j - 3
            else:
                j = j - 2
        return self.data_array

    def __fill_array(self, i, j):
        """
        Add binary value to the array. If binary value is part of QRCode included word.
        :param i:
        :param j:
        """
        if not self.is_skip_point(i, j):
            self.data_array.append(str(self.__unmask_matrix[i][j]))
        if not self.is_skip_point(i, j - 1):
            self.data_array.append(str(self.__unmask_matrix[i][j - 1]))

    @abstractmethod
    def is_skip_point(self, i, j):
        """
        This method return the true when that specific point should skip. otherwise return false
        :type i: int
        :type j: int
        """
        pass

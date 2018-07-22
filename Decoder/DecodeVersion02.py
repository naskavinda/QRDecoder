from Decoder.DecoderVersion import DecoderVersion

__author__ = 'N.A. Supun Kavinda'


class DecodeVersion02(DecoderVersion):

    def __init__(self, unmask_matrix):
        self.__unmask_matrix = unmask_matrix
        super().__init__(unmask_matrix)

    def is_skip_point(self, i, j):
        if (9 > i and 9 > j) or (9 > i and j > len(self.__unmask_matrix) - 9) or (
                i > (len(self.__unmask_matrix) - 9) and j < 9) or (
                (len(self.__unmask_matrix) - 4) > i > 15 and (len(self.__unmask_matrix[0]) - 4) > j > 15):
            return True
        elif i == 6 or j == 6:
            return True
        else:
            return False

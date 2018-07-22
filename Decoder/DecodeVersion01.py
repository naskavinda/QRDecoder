from Decoder.DecoderVersion import DecoderVersion

__author__ = 'N.A. Supun Kavinda'

class DecodeVersion01(DecoderVersion):

    def __init__(self, unmask_matrix):
        super().__init__(unmask_matrix)

    def is_skip_point(self, i, j):
        if (9 > i and 9 > j) or (9 > i and j > 12) or (i > 12 and j < 9):
            return True
        elif i == 6 or j == 6:
            return True
        else:
            return False

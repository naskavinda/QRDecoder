from Mask.AddMask import AddMask

__author__ = 'N.A. Supun Kavinda'


class Pattern08(AddMask):

    def __init__(self, matrix):
        super().__init__(matrix)

    def change_pixel(self, i, j, matrix):
        if (i * j) % 2 + (i * j) % 3 == 0:
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1

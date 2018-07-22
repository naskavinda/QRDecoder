__author__ = 'N.A. Supun Kavinda'


class PrintMatrix:
    def __init__(self):
        pass

    @staticmethod
    def print_matrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end='')
            print()

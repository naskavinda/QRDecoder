from ProcessMatrix.QRCodeDetails import QRCodeDetails

__author__ = 'N.A. Supun Kavinda'


class ImageMatrix:

    def __init__(self, image):
        self.__image = image

    def convert_to_qr_matrix(self):

        rows, cols = self.__image.shape
        # print("rows : ", rows, " cols : ", cols)
        length_of_pixels = QRCodeDetails(self.__image).length_of_block()

        matrix = [[0 for x in range(int(rows / length_of_pixels))] for y in range(int(cols / length_of_pixels))]

        a = 0
        for i in range(rows):
            if i % length_of_pixels == 0:
                b = 0
                for j in range(cols):
                    if j % length_of_pixels == 0:
                        matrix[a][b] = self.__image[i, j]
                        b = b + 1
                a = a + 1
                # print()
        # print(matrix)
        return matrix

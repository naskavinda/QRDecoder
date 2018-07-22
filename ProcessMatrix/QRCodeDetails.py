__author__ = 'N.A. Supun Kavinda'


class QRCodeDetails:
    __matrix = None
    __version_length = [21, 25, 29, 33, 57, 117, 177]
    __version = [1, 2, 3, 4, 10, 25, 40]

    def __init__(self, matrix):
        QRCodeDetails.__matrix = matrix

    @staticmethod
    def get_version():
        version, __ = QRCodeDetails.__cal()
        return version

    @staticmethod
    def length_of_block():
        __, length_of_block = QRCodeDetails.__cal()
        return length_of_block

    @staticmethod
    def __cal():
        rows, cols = len(QRCodeDetails.__matrix), len(QRCodeDetails.__matrix[0])
        for i in range(len(QRCodeDetails.__version_length)):
            __length = QRCodeDetails.__version_length[i]
            if rows % __length == 0:
                return QRCodeDetails.__version[i], rows / __length
        raise NotImplementedError("This Version Calculation is not implemented")

        # if rows % 21 == 0:
        #     return 1, rows / 21
        # elif rows % 25 == 0:
        #     return 2, rows / 25
        # elif rows % 29 == 0:
        #     return 3, rows / 29
        # elif rows % 33 == 0:
        #     return 4, rows / 33
        # elif rows % 57 == 0:
        #     return 10, rows / 57
        # elif rows % 117 == 0:
        #     return 25, rows / 117
        # elif rows % 177 == 0:
        #     return 40, rows / 177
        # else:
        #     raise NotImplementedError("This Version Calculation is not implemented")

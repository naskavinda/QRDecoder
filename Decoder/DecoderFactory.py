from Decoder.DecodeVersion02 import DecodeVersion02
from Decoder.DecodeVersion01 import DecodeVersion01
from ProcessMatrix.QRCodeDetails import QRCodeDetails

__author__ = 'N.A. Supun Kavinda'


class DecoderFactory:
    def __init__(self, unmask_matrix):
        self.__unmask_matrix = unmask_matrix

    def create(self):
        __version = QRCodeDetails(self.__unmask_matrix).get_version()
        print("version ", __version)
        
        if __version == 1:
            return DecodeVersion01(self.__unmask_matrix)
        elif __version == 2:
            return DecodeVersion02(self.__unmask_matrix)
        # elif __version == 3:
        #     return DecodeVersion03(self.__unmask_matrix)
        # elif __version == 4:
        #     return DecodeVersion04(self.__unmask_matrix)
        # elif __version == 5:
        #     return DecodeVersion05(self.__unmask_matrix)
        # elif __version == 6:
        #     return DecodeVersion06(self.__unmask_matrix)
        # elif __version == 7:
        #     return DecodeVersion07(self.__unmask_matrix)
        # elif __version == 8:
        #     return DecodeVersion08(self.__unmask_matrix)
        else:
            return NotImplementedError('This Pattern is not implement yet.')

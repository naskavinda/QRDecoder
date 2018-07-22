from Decoder.DecoderFactory import DecoderFactory
from ProcessImage.CropQRCode import CropQRCode
from Scanner.ImageRead import ImageRead
from Mask.PatternsFactory import PatternsFactory
from ProcessImage.ThresholdBinaryInvAndOTSU import ThresholdBinaryInvAndOTSU
from ProcessMatrix.ImageToQR import ImageMatrix
from ProcessImage.Mapper import Mapper

__author__ = 'N.A. Supun Kavinda'

if __name__ == '__main__':
    # Initialize ImageRead Object
    image_read = ImageRead()

    # Read Image
    img = image_read.image_reader()

    # Add Threshold To Image
    ret, threshold_image_output = ThresholdBinaryInvAndOTSU(img).add_threshold()

    # 255 replace by 1
    matrix_replace_by_one = Mapper.replace_by_one(threshold_image_output)

    # crop the QR Code from image
    crop_matrix = CropQRCode(matrix_replace_by_one).extract_qr_code()

    # Scale down the matrix
    scale_down_matrix = ImageMatrix(crop_matrix).convert_to_qr_matrix()

    # Add mask add get un mask matrix
    unmask_matrix = PatternsFactory(scale_down_matrix).create().add_mask()

    # PrintMatrix.print_matrix(unmask_matrix)

    final_result = DecoderFactory(unmask_matrix).create()

    print('QR Code = ', final_result.decoder())

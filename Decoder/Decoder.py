class Decoder:
    def __init__(self):
        pass

    @staticmethod
    def decode_bytes_array(binary_array):
        """
        This method give the included word in QRCode.
        :rtype: str
        """
        length = 8
        __binary_length_of_word = ''
        for i in range(4, 4 + length):
            __binary_length_of_word = __binary_length_of_word + binary_array[i]

        i = 1
        word = ''
        length_of_word = int(__binary_length_of_word, 2)
        print("length of word ", length_of_word)
        while i <= length_of_word:
            character = ''
            for j in range(4 + length * i, 4 + length * (i + 1)):
                character = character + binary_array[j]
            char_int_value = int(character, 2)
            word += str(char_int_value) if 0 <= char_int_value < 10 else chr(char_int_value)
            i = i + 1
        return word

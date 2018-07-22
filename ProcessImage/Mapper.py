class Mapper:
    def __init__(self):
        pass

    @staticmethod
    def replace_by_one(image):
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 255:
                    image[i][j] = 1
        return image

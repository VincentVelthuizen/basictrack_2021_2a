from PIL import Image
import numpy as np


def brighten(file_name):
    image = Image.open(file_name)

    pixel_array = np.array(image)
    # new_pixel_array = []
    #
    # for row in pixel_array:
    #     # new_row = []
    #     #
    #     # for pixel in row:
    #     #     new_row.append(pixel + 100)
    #     new_row = [pixel + 100 for pixel in row]  # list comprehension
    #
    #     new_pixel_array.append(new_row)

    new_pixel_array = [[pixel + 100 for pixel in row] for row in pixel_array]

    new_pixel_array = np.array(new_pixel_array).astype('uint8')

    new_image = Image.fromarray(new_pixel_array)
    new_image.show()
    new_image.save("fruit_brightened.png")


if __name__ == '__main__':
    brighten("fruit_brightened.png")

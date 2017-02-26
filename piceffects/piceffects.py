import numpy as np
from PIL import Image

def img_to_arr(name = 'pics/kvetina.jpg'):
    pic = Image.open(name)
    pix = np.array(pic)
    return pix

def img_inv(pix):
    return 255-pix

def img_grayscale(pix):
    return np.dot(pix[..., :3], [0.299, 0.587, 0.114])

def img_red_channel(pix):
    return np.dot(pix[..., :3], [1.0, 0, 0])

def img_green_channel(pix):
    return np.dot(pix[..., :3], [0, 1.0, 0])

def img_blue_channel(pix):
    return np.dot(pix[..., :3], [0, 0, 1.0])

def img_downscale2(pix):
    return pix[::2, ::2]

def img_darker(pix):
    return pix//2

def img_lighter(pix):
    return pix*2
    # return 255-((255-pix)//2)

def img_rotate(pix):
    pass

def main():
    pix = img_to_arr()
    # print(img_grayscale(pix))

    # Inverse colors
    # Image.fromarray(img_inv(pix)).show()

    # Grayscale
    # Image.fromarray(img_grayscale(pix)).show()

    # Channels
    Image.fromarray(img_red_channel(pix)).show()
    # Image.fromarray(img_green_channel(pix)).show()
    # Image.fromarray(img_blue_channel(pix)).show()

    # Down scale 2x
    # Image.fromarray(img_downscale2(pix)).show()
    # print(pix[::3, ::3])
    # print(img_darker(pix))
    # Image.fromarray(img_lighter(pix)).show()


    # print((pix[1,1,]//2))

main()
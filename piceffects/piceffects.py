import numpy as np
from PIL import Image


def to_arr(name='pics/kvetina.jpg'):
    pic = Image.open(name)
    pix = np.array(pic)
    return pix


def inv(pix):
    return 255 - pix


def grayscale(pix):
    return pix@[0.299, 0.587, 0.114]
    # return np.dot(pix[..., :3], [0.299, 0.587, 0.114])


def red_channel(pix):
    return pix@[1.0, 0, 0]


def green_channel(pix):
    return pix@[0, 1.0, 0]


def blue_channel(pix):
    return pix@[0, 0, 1.0]


def downscale2(pix):
    return pix[::2, ::2]


def darker(pix):
    return pix // 2


def lighter(pix):
    npix = np.array(pix)
    npix[npix > 255 // 2] = 255 // 2
    npix *= 2
    return npix

def del_channels(pix, channels):
    npix = np.array(pix)
    for i in channels:
        npix[..., i:i+1] = 0
    return npix



def main():
    pix = to_arr()
    # print(grayscale(pix))

    # Inverse colors
    # Image.fromarray(inv(pix)).show()

    # Grayscale
    # Image.fromarray(grayscale(pix)).show()

    # Channels
    # Image.fromarray(red_channel(pix)).show()
    # Image.fromarray(green_channel(pix)).show()
    # Image.fromarray(blue_channel(pix)).show()

    # Down scale 2x
    # Image.fromarray(downscale2(pix)).show()
    # print(pix[::3, ::3])
    # print(darker(pix))
    # Image.fromarray(lighter(pix)).show()
    # Image.fromarray(pix).show()


    Image.fromarray(del_channels(pix, [0,1])).show()
    print(blue_channel(pix))
    # print((pix[1,1,]//2))


main()

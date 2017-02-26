import numpy as np
from PIL import Image


def to_arr(name='pics/kvetina.jpg'):
    pic = Image.open(name)
    pix = np.array(pic)
    return pix


def inv(pix):
    return 255 - pix


def grayscale(pix):
    return (pix @ [0.299, 0.587, 0.114]).astype(np.uint8)


def red_channel(pix):
    return pix @ [1.0, 0, 0]


def green_channel(pix):
    return pix @ [0, 1.0, 0]


def blue_channel(pix):
    return pix @ [0, 0, 1.0]


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
        npix[..., i:i + 1] = 0
    return npix


def sharp(pix):
    gpix = grayscale(pix)
    effect = np.array([-1, -1, -1, -1, 8, -1, -1, -1, -1])
    pmask = np.array(gpix)

    for i in range(1, len(gpix) - 1):
        for j in range(1, len(gpix[i]) - 1):
            vector = gpix[i - 1:i + 2, j - 1:j + 2].flatten()
            pmask[i, j] = np.sum(vector * effect)

    # pmask[pmask < 0] = 0
    # pmask[pmask > 255] = 255

    npix = np.dstack((pix[..., 0] + pmask, pix[..., 1] + pmask, pix[..., 2] + pmask))
    npix[npix < 0] = 0
    npix[npix > 255] = 255
    return npix.astype(np.uint8)


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


    # Image.fromarray(del_channels(pix, [0])).show()
    # Image.fromarray(sharp(pix)).show()
    # Image.fromarray(pix).show()
    # print((pix[1,1,]//2))

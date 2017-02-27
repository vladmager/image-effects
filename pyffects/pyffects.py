from PIL import Image, ImageQt
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QImage


import piceffects as pic


class ImageLable(QtWidgets.QLabel):
    def __init__(self, image):
        super().__init__()
        self.image = ImageQt.ImageQt(Image.open(image))
        # self.setScaledContents(True)
        self.pixmap = QtGui.QPixmap.fromImage(self.image)
        self.setPixmap(self.pixmap)


    def paint(self, pixmap):
        self.setPixmap(pixmap)
        self.show()

def buttonClicked():
    print('bla')

def apply_modifier(func, image_widget):
    # pixmap -> array
    pixmap = image_widget.pixmap
    image = ImageQt.fromqpixmap(pixmap)
    data = np.array(image)
    modifided_image = Image.fromarray(func(data))
    # array -> pixmap
    pixmap = ImageQt.toqpixmap(modifided_image)
    image_widget.pixmap = pixmap
    image_widget.update()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        with open('uis/main.ui') as f:
            uic.loadUi(f, self)

        self.label = ImageLable('pics/lena.png')

        self.scrollArea = self.findChild(QtWidgets.QScrollArea, 'scrollArea')
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.label)

        self.gray_button = self.findChild(QtWidgets.QPushButton, 'restore_btn')
        self.gray_button.clicked.connect(self.restore_img)

        self.inv_button = self.findChild(QtWidgets.QPushButton, 'inv_btn')
        self.inv_button.clicked.connect(lambda: self.apply_effect(pic.inv))

        self.grayscale_button = self.findChild(QtWidgets.QPushButton, 'grayscale_btn')
        self.grayscale_button.clicked.connect(lambda: self.apply_effect(pic.grayscale_uint8))

        self.red_ch_button = self.findChild(QtWidgets.QPushButton, 'red_ch_btn')
        self.red_ch_button.clicked.connect(lambda: self.apply_effect(pic.red_channel))

        self.green_ch_button = self.findChild(QtWidgets.QPushButton, 'green_ch_btn')
        self.green_ch_button.clicked.connect(lambda: self.apply_effect(pic.green_channel))

        self.blue_ch_button = self.findChild(QtWidgets.QPushButton, 'blue_ch_btn')
        self.blue_ch_button.clicked.connect(lambda: self.apply_effect(pic.blue_channel))

        self.downscale_button = self.findChild(QtWidgets.QPushButton, 'downscale_btn')
        self.downscale_button.clicked.connect(lambda: self.apply_effect(pic.downscale))

        self.darken_button = self.findChild(QtWidgets.QPushButton, 'darken_btn')
        self.darken_button.clicked.connect(lambda: self.apply_effect(pic.darken))

        self.lighten_button = self.findChild(QtWidgets.QPushButton, 'lighten_btn')
        self.lighten_button.clicked.connect(lambda: self.apply_effect(pic.lighten))

        self.sharp_button = self.findChild(QtWidgets.QPushButton, 'sharp_btn')
        self.sharp_button.clicked.connect(lambda: self.apply_effect(pic.sharp))





    def apply_effect(self, func):
        pixmap = self.label.pixmap
        image = ImageQt.fromqpixmap(pixmap)
        data = pic.to_arr(image)
        modifided_image = pic.to_img(func(data))
        pixmap = ImageQt.toqpixmap(modifided_image)
        self.label.paint(pixmap)

    def restore_img(self):
        self.label.paint(self.label.pixmap)


def main():
    app = QtWidgets.QApplication([])

    window = MainWindow()


    # label = QtWidgets.QLabel()
    # image = ImageQt.ImageQt(Image.open('pics/lena.png'))
    # pixmap = QtGui.QPixmap.fromImage(image)
    # label.setPixmap(pixmap)

    window.show()
     # pic.to_arr()
    # window.apply_effect(pic.lighter)
    # window.apply_effect(pic.grayscale)

    return app.exec()
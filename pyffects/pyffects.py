from PIL import Image, ImageQt
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QFileDialog

import piceffects as pic


class ImageLable(QtWidgets.QLabel):
    def __init__(self, image):
        super().__init__()
        self.image = ImageQt.ImageQt(Image.open(image))
        self.origin_pixmap = QtGui.QPixmap.fromImage(self.image)
        self.pixmap = self.origin_pixmap
        self.setPixmap(self.pixmap)


    def paint(self, pixmap = None):
        if not pixmap:
            pixmap = self.origin_pixmap
        self.pixmap = pixmap
        self.setPixmap(self.pixmap)
        self.show()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        with open('uis/main.ui') as f:
            uic.loadUi(f, self)

        self.img_label = ImageLable('pics/lena.png')

        self.scrollArea = self.findChild(QtWidgets.QScrollArea, 'scrollArea')
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.img_label)

        self.action_open = self.findChild(QtWidgets.QAction, 'actionOpen_File')
        self.action_open.triggered.connect(self.open_file)

        self.action_save = self.findChild(QtWidgets.QAction, 'actionSave_File')
        self.action_save.triggered.connect(self.save_file)

        self.load_buttons()


    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Open file',  '~', "Image files (*.jpg *.png)")
        self.img_label.origin_pixmap = QtGui.QPixmap(path)
        self.img_label.paint()
        pass

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Save file', 'new_image.jpg', "Image file (*.jpg)")
        result_pic = ImageQt.fromqpixmap(self.img_label.pixmap)
        result_pic.save(path)
        pass

    def load_buttons(self):
        # Buttons
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
        pixmap = self.img_label.pixmap
        image = ImageQt.fromqpixmap(pixmap)
        data = pic.to_arr(image)
        modifided_image = pic.to_img(func(data))
        pixmap = ImageQt.toqpixmap(modifided_image)
        self.img_label.paint(pixmap)

    def restore_img(self):
        self.img_label.paint(self.img_label.origin_pixmap)


def main():
    app = QtWidgets.QApplication([])

    window = MainWindow()


    # img_label = QtWidgets.QLabel()
    # image = ImageQt.ImageQt(Image.open('pics/lena.png'))
    # pixmap = QtGui.QPixmap.fromImage(image)
    # img_label.setPixmap(pixmap)

    window.show()
     # pic.to_arr()
    # window.apply_effect(pic.lighter)
    # window.apply_effect(pic.grayscale)

    return app.exec()
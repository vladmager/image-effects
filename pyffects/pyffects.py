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


    def paint(self, event):
        self.setPixmap(self.pixmap)
        self.show()



def main():
    app = QtWidgets.QApplication([])

    window = QtWidgets.QMainWindow()

    with open('uis/main.ui') as f:
        uic.loadUi(f, window)

    # label = QtWidgets.QLabel()
    # image = ImageQt.ImageQt(Image.open('pics/lena.png'))
    # pixmap = QtGui.QPixmap.fromImage(image)
    # label.setPixmap(pixmap)

    label = ImageLable('pics/lena.png')


    scrollArea = window.findChild(QtWidgets.QScrollArea, 'scrollArea')
    scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
    scrollArea.setWidget(label)

    window.show()
    # pic.to_arr()

    return app.exec()
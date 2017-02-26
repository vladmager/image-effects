
from PyQt5 import QtWidgets, uic, QtGui
from PIL import Image, ImageQt



def main():
    app = QtWidgets.QApplication([])

    window = QtWidgets.QMainWindow()

    with open('uis/main.ui') as f:
        uic.loadUi(f, window)

    label = QtWidgets.QLabel()
    image = ImageQt.ImageQt(Image.open('pics/lena.png'))
    pixmap = QtGui.QPixmap.fromImage(image)
    label.setPixmap(pixmap)

    scrollArea = window.findChild(QtWidgets.QScrollArea, 'scrollArea')
    scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
    scrollArea.setWidget(label)

    window.show()

    return app.exec()
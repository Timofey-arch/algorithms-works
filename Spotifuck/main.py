from Composition import Composition
from LinkedList import LinkedList
from PyQt5 import QtWidgets
import sys
from Interface.SpotiFuckDesign import Ui_SpotiFuck
from Interface.AddPlaylistWindow import Ui_AddPlayListWindow


class SpotiFuckMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SpotiFuckMainWindow, self).__init__()
        self.ui = Ui_SpotiFuck()
        self.ui.setupUi(self)


class AddPlaylistWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddPlaylistWindow, self).__init__()
        self.ui = Ui_AddPlayListWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication([])
    application = SpotiFuckMainWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

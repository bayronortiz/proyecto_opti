# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from views.main_window import MainWindow
import sys

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


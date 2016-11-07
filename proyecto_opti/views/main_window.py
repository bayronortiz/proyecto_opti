# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
sys.path.append('../')
from pyuic_classes.ui_main_window import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
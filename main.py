# run the file to start

# importing libraries and a file
import sys
from PyQt5.QtWidgets import *
import windows

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = windows.Window()

# start the app
sys.exit(App.exec())


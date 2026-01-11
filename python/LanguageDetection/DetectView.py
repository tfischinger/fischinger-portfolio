import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from langdet_gui import Ui_MainWindow
from DetectController import DetectController

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.DetectController = DetectController(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

from PyQt6.uic.properties import QtWidgets


class CurrencyConverterView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Currency Converter")

        self.Betrag = QtWidgets.QDoubleSpinBox(self)
        self.Betrag.setGeometry(80, 10, 62, 22)

        self.label = QtWidgets.QLabel("Betrag:", self)
        self.label.setGeometry(20, 10, 61, 21)

        self.label_2 = QtWidgets.QLabel("Base-Währung:", self)
        self.label_2.setGeometry(190, 10, 101, 21)

        self.Waehrung = QtWidgets.QLineEdit(self)
        self.Waehrung.setGeometry(290, 10, 113, 21)

        self.ausgabefeld = QtWidgets.QTextEdit(self)
        self.ausgabefeld.setGeometry(3, 70, 641, 211)

        self.calculateButton = QtWidgets.QPushButton("Umrechnen", self)
        self.calculateButton.setGeometry(480, 10, 91, 31)

        self.exitButton = QtWidgets.QPushButton("Exit", self)
        self.exitButton.setGeometry(84, 310, 171, 31)

        self.resetButton = QtWidgets.QPushButton("Zurücksetzen", self)
        self.resetButton.setGeometry(370, 320, 141, 24)

        self.label_3 = QtWidgets.QLabel("Ziel-Währung:", self)
        self.label_3.setGeometry(190, 40, 101, 21)

        self.zielWaehrung = QtWidgets.QLineEdit(self)
        self.zielWaehrung.setGeometry(290, 40, 113, 21)

    def get_input(self):
        return self.Betrag.value(), self.Waehrung.text(), self.zielWaehrung.text()

    def set_output(self, result):
        self.ausgabefeld.setText(str(result))

    def clear_fields(self):
        self.Betrag.clear()
        self.Waehrung.clear()
        self.zielWaehrung.clear()
        self.ausgabefeld.clear()

    def show_error(self, message):
        self.ausgabefeld.setText(message)
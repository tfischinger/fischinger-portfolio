from PyQt6.QtWidgets import *
from ui_SSPGui import Ui_MainWindow



class SSPView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.resetButton.clicked.connect(controller.reset)
        self.ui.spielzugButton.clicked.connect(lambda: controller.spielzug(self.get_Auswahl()))


    def reset(self)->None:
        """
        Die Methode Reset setzt die Runden, letzter Spielzug, compWins und Spielerwins auf den Startwert.
        Das Spiel beginnt neu
        :return:
        """
        self.ui.zugauswahl.setCurrentIndex(0)
        self.ui.anzahlRunden.setText("0")
        self.ui.spielerWins.setText("0")
        self.ui.compWins.setText("0")
        self.ui.letzterZug.setText("Erster Zug")

    def set_runden(self, r: str):
        self.ui.anzahlRunden.setText(r)  # Korrektur: setze den Text des QLabel oder QLineEdit

    def set_letzterZug(self, s: str, c: str):
        text = "Spieler: [" + s + "], Computer: [" + c + "]"
        self.ui.letzterZug.setText(text)

    def set_spielerWins(self, sw: str):
        self.ui.spielerWins.setText(sw)

    def set_compWins(self, cw: str):
        self.ui.compWins.setText(cw)

    def get_Auswahl(self) -> str:
        return self.ui.zugauswahl.currentText()




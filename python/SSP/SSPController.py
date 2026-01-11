import sys
from PyQt6.QtWidgets import QApplication

from SSP import SSP
from SSPView import SSPView


class SSPController:

    def __init__(self):
        self.model = SSP()
        self.view = SSPView(self)

    def reset(self):
        """
        Die Methode Reset im Controller ruft die reset von Model und view ab
        Um die GUI und die SPieldaten zu resetten.
        :return:
        """
        self.model.reset()
        self.view.reset()

    def spielzug(self, sp: str):
        """
        Die Methode spielzug ist die Methode welche ausgeführt wird wenn man einen Spielzug macht.
        Es wird die Spielerwahl mit eineer durch random generierten computerauswahl verglichen.
        :param spielerWahl:
        :return:
        """
        print("methode in der methode betreten")
        self.model.spielzug(sp)
        print("methode in der methode wieder betreten")
        print(self.model.spielerWahl)
        print(self.model.computerWahl)
        self.view.set_letzterZug(self.model.spielerWahl, self.model.computerWahl)
        print("letzter Zug gesetzt")
        self.view.set_runden(str(self.model.runde))
        print("runden gesetzt")
        self.view.set_spielerWins(str(self.model.spielerWin))
        print("spielerwin gesetzt")
        self.view.set_compWins(str(self.model.computerWin))
        print("computerwin gesetzt")

if __name__ == '__main__':
        app = QApplication([])
        c = SSPController()
        c.view.show()
        sys.exit(app.exec())

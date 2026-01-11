# SSP.py
import random

auswahl = ["Schere", "Stein", "Papier"]

class SSP:
    def __init__(self):
#        self.view = SSPView()
        self.runde = 0
        self.computerWahl = None
        self.spielerWahl = None
        self.ergebnis = "Schere, Stein, Papier!"
        self.computerWin = 0
        self.spielerWin = 0

    def spielzug(self, spielerWahl: str):
        """
        Die Methode spielzug ist die Methode welche ausgeführt wird wenn man einen Spielzug macht.
        Es wird die Spielerwahl mit eineer durch random generierten computerauswahl verglichen.
        :param spielerWahl:
        :return:
        """
        print("methode betreten")
        self.zufall = random.choice(auswahl)
        print("Es wurde" +self.zufall + "ausgewählt")
        self.computerWahl = self.zufall
        print(self.computerWahl)
        self.spielerWahl = spielerWahl
        print(self.spielerWahl)

        if self.computerWahl == self.spielerWahl:
            self.ergebnis = "Unentschieden!"
            self.runde += 1
            print(self.ergebnis)
        elif (self.spielerWahl, self.computerWahl) in [
            ("Schere", "Papier"),
            ("Papier", "Stein"),
            ("Stein", "Schere")
        ]:
            self.ergebnis = "Spieler gewinnt!"
            print(self.ergebnis)
            self.spielerWin += 1
            self.runde += 1
        else:
            self.ergebnis = "Computer gewinnt!"
            print(self.ergebnis)
            self.computerWin += 1
            self.runde += 1

    def reset(self):
        """
        Die Methode Reset setzt die Runden, letzter Spielzug, compWins und Spielerwins auf den Startwert.
        Das Spiel beginnt neu
        :return:
        """
        self.runde = 0
        self.spielerWin = 0
        self.computerWin = 0
        self.ergebnis = "Schere, Stein, Papier!"
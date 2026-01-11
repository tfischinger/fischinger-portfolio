import sys

from PyQt6.QtWidgets import QApplication

import CurrencyConverter
import currencyGUI
class CurrencyController:
    def __init__(self):
        # Erstelle die View und das Model
        self.view = currencyGUI()
        self.model = CurrencyConverter()

        # Verbinde die View und das Model
        self.view.calculateButton.clicked.connect(self.convert_currency)
        self.view.resetButton.clicked.connect(self.reset_fields)
        self.view.exitButton.clicked.connect(self.exit_app)

    def convert_currency(self):
        amount, base_currency, target_currency = self.view.get_input()

        # Umrechnung durchführen
        if not base_currency or not target_currency:
            self.view.show_error("Bitte geben Sie sowohl die Base-Währung als auch die Ziel-Währung ein.")
            return

        result = self.model.convert(amount, base_currency, target_currency)
        if result is not None:
            self.view.set_output(f"{amount} {base_currency} = {result} {target_currency}")
        else:
            self.view.show_error("Fehler bei der Umrechnung. Überprüfen Sie die Währungscodes.")

    def reset_fields(self):
        self.view.clear_fields()

    def exit_app(self):
        self.view.close()

    def run(self):
        # Zeige die View und starte die Anwendung
        self.view.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = CurrencyConverter()
    controller.run()
    sys.exit(app.exec())
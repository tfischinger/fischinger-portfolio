from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QApplication
from DetectModel import DetectModel

class DetectController:
    def __init__(self, view):
        self.view = view
        self.model = DetectModel()
        self.view.checkButton.clicked.connect(self.check_language)
        self.view.resetButton.clicked.connect(self.reset_fields)
        self.view.closeButton.clicked.connect(self.close_application)

    def check_language(self):
        text = self.view.textEdit.toPlainText()
        if not text.strip():
            self.show_error("Text is empty!", "Please enter some text to detect the language.")
            return
        result = self.model.detect_language(text)
        if result:
            print("if erreicht")
            reliable = "Reliable" if result["reliable"] else "Unreliable"
            print("reliable gesetzt")
            language_name = self.model.get_language_name(result["short"])
            print("language name gesetzt")
            prob = result["prob"]
            print("prob gesetzt")
            result_text = f"Language: {language_name}\nConfidence: {reliable}\nProbability: {prob}%"
            print("result gesetzt")
            self.view.textBrowser.setText(result_text)
            print("result in view gesetzt")
        else:
            self.show_error("Error", "Failed to detect language. Please try again.")

    def reset_fields(self):
        self.view.textEdit.clear()
        self.view.textBrowser.clear()

    def close_application(self):
        self.view.close()

    def show_error(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec()

# bkfinances.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class BKFinances(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BKFinances v1.1")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def setup_ui(self):
        # Exemple simple : affichage d'une boîte au lancement
        QMessageBox.information(self, "Bienvenue", "Bienvenue dans BKFinances v1.1 !")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BKFinances()
    window.show()
    sys.exit(app.exec_())

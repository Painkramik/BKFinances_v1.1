import sys
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

def enregistrer_historique(action, cible, details):
    conn = sqlite3.connect("bkfinances.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historique (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            heure TEXT,
            action TEXT,
            cible TEXT,
            details TEXT
        )
    """)

    from datetime import datetime
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    heure = now.strftime("%H:%M:%S")

    cursor.execute("""
        INSERT INTO historique (date, heure, action, cible, details)
        VALUES (?, ?, ?, ?, ?)
    """, (date, heure, action, cible, details))

    conn.commit()
    conn.close()

class BKFinances(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BKFinances v1.1")
        self.setGeometry(100, 100, 800, 600)

        # Liste simulée de comptes
        self.comptes = [
            {"id": 1, "nom": "Compte courant", "favori": False},
            {"id": 2, "nom": "Livret A", "favori": True},
            {"id": 3, "nom": "Épargne", "favori": False}
        ]
        
        self.raccourcis = [
            {"id": 2, "nom": "Livret A"},
            {"id": 3, "nom": "Épargne"}
        ]
        self.setup_ui()

    def toggle_favori(self, compte_id):
        for compte in self.comptes:
            if compte["id"] == compte_id:
                compte["favori"] = not compte["favori"]
                state = "épinglé" if compte["favori"] else "retiré des favoris"
                QMessageBox.information(self, "Favoris", f"{compte['nom']} est maintenant {state}.")
                break


    def setup_ui(self):
        # Message d'accueil
        QMessageBox.information(self, "Bienvenue", "Bienvenue dans BKFinances v1.1 !")

        # Bouton de test pour enregistrer dans l'historique
        bouton_test = QPushButton("Enregistrer un test", self)
        bouton_test.setGeometry(50, 100, 200, 40)
        bouton_test.clicked.connect(self.action_test)

    def action_test(self):
        try:
            enregistrer_historique("test", "interface", "Ceci est un test d'enregistrement")
            QMessageBox.information(self, "Historique", "Action test enregistrée !")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Échec de l'enregistrement :\n{e}")

    def acces_rapide(self, compte):
        QMessageBox.information(self, "Raccourci", f"Accès rapide vers le compte : {compte['nom']}")

    def setup_ui(self):
        # Message d'accueil
        QMessageBox.information(self, "Bienvenue", "Bienvenue dans BKFinances v1.1 !")

        # Bouton de test pour enregistrer dans l'historique
        bouton_test = QPushButton("Enregistrer un test", self)
        bouton_test.setGeometry(50, 100, 200, 40)
        bouton_test.clicked.connect(self.action_test)

        # ⬇️ Ce bouton manquait, ajoute-le ici
        bouton_favori = QPushButton("Basculer favori - Compte 1", self)
        bouton_favori.setGeometry(50, 160, 250, 40)
        bouton_favori.clicked.connect(lambda: self.toggle_favori(1))

        # Raccourcis vers les comptes utilisés souvent
        y = 220
        for compte in self.raccourcis:
            bouton_rapide = QPushButton(f"Accès rapide : {compte['nom']}", self)
            bouton_rapide.setGeometry(50, y, 300, 40)
            bouton_rapide.clicked.connect(lambda _, c=compte: self.acces_rapide(c))
            y += 50


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BKFinances()
    window.show()
    sys.exit(app.exec_())

# Ajout des favoris + raccourcis rapides

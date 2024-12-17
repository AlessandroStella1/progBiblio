import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListView, QComboBox

from prenotazioneposto.model.PrenotazionePosto import PrenotazionePosto


class VistaInserisciPrenotazioniPosto(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazioniPosto, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        self.combo_studenti = QComboBox()
        self.combostudenti_model = QStandardItemModel(self.combo_studenti)
        if os.path.isfile('listastudenti/data/lista_studenti_salvata.pickle'):
            with open('listastudenti/data/lista_studenti_salvata.pickle', 'rb') as f:
                self.lista_studenti_salvata = pickle.load(f)
            for studente in self.lista_studenti_salvata:
                item = QStandardItem()
                item.setText(studente.nome + " " + studente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.combostudenti_model.appendRow(item)
            self.combo_studenti.setModel(self.combostudenti_model)
        v_layout.addWidget(QLabel("Studente"))
        v_layout.addWidget(self.combo_studenti)

        self.combo_posto = QComboBox()
        self.update_posti()

        v_layout.addWidget(QLabel("Studente"))
        v_layout.addWidget(self.combo_studenti)
        v_layout.addWidget(QLabel("Posto"))
        v_layout.addWidget(self.combo_posto)

        btn_ok = QPushButton("Prenota Posto")
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuova Prenotazione Posto')

    def update_posti(self):
        self.combo_posto.clear()
        for posto in self.controller.get_posti_disponibili():
            self.combo_posto.addItem(f"Posto {posto.id}")

    def add_prenotazione(self):
        studente = self.lista_studenti_salvata[self.combo_studenti.currentIndex()]
        posto = self.controller.model.posti[self.combo_posto.currentIndex()]
        prenotazione = PrenotazionePosto(studente.id, studente, posto)
        self.controller.aggiungi_prenotazione_posto(prenotazione)
        self.callback()
        self.close()

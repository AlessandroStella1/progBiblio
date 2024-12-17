import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox

from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__(parent=None)
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("data (dd/MM/yyyy)"))
        self.text_data = QLineEdit(self)
        v_layout.addWidget(self.text_data)

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

        self.combo_libri = QComboBox()
        self.combolibri_model = QStandardItemModel(self.combo_libri)
        if os.path.isfile('listalibri/data/lista_libri_salvata.pickle'):
            with open('listalibri/data/lista_libri_salvata.pickle', 'rb') as f:
                self.lista_libri_salvata = pickle.load(f)
            self.lista_libri_disponibili = [s for s in self.lista_libri_salvata if s.is_disponibile()]
            for libro in self.lista_libri_disponibili:
                item = QStandardItem()
                item.setText(libro.titolo)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.combolibri_model.appendRow(item)
            self.combo_libri.setModel(self.combolibri_model)
        v_layout.addWidget(QLabel("libro"))
        v_layout.addWidget(self.combo_libri)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuova Prenotazione')

    def add_prenotazione(self):
        data = self.text_data.text()
        studente = self.lista_studenti_salvata[self.combo_studenti.currentIndex()]
        libro = self.lista_libri_disponibili[self.combo_libri.currentIndex()]
        if data == "" or not studente or not libro:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(Prenotazione((studente.cognome+studente.nome).lower(), studente, libro, data))
            libro.prenota()
            with open('listalibri/data/lista_libri_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_libri_salvata, f, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()
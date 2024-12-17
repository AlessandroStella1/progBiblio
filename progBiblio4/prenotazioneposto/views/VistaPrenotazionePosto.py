from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from prenotazioneposto.controller.ControllorePrenotazionePosto import ControllorePrenotazionePosto

class VistaPrenotazionePosto(QWidget):
    def __init__(self, prenotazione, disdici_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazionePosto, self).__init__(parent)
        self.controller = ControllorePrenotazionePosto(prenotazione)
        self.disdici_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_posto = QLabel(f"Posto {self.controller.get_posto_prenotazione()}")
        font_posto = label_posto.font()
        font_posto.setPointSize(30)
        label_posto.setFont(font_posto)
        v_layout.addWidget(label_posto)

        label_studente = QLabel(f"Studente: {self.controller.get_studente_prenotazione().nome} {self.controller.get_studente_prenotazione().cognome}")
        font_studente = label_studente.font()
        font_studente.setPointSize(30)
        label_studente.setFont(font_studente)
        v_layout.addWidget(label_studente)

        label_data = QLabel(f"Data: {self.controller.get_data_prenotazione()}")
        font_data = label_data.font()
        font_data.setPointSize(30)
        label_data.setFont(font_data)
        v_layout.addWidget(label_data)

        btn_disdici = QPushButton("Disdici")
        btn_disdici.clicked.connect(self.disdici_prenotazione_click)
        v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.setWindowTitle(f"Posto {self.controller.get_posto_prenotazione()}")

    def disdici_prenotazione_click(self):
        self.disdici_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()


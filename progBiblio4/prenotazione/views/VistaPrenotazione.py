from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione


class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, disdici_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controller = ControllorePrenotazione(prenotazione)
        self.disdici_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_titolo = QLabel(self.controller.get_libro_prenotazione().titolo)
        font_titolo = label_titolo.font()
        font_titolo.setPointSize(30)
        label_titolo.setFont(font_titolo)
        v_layout.addWidget(label_titolo)

        v_layout.addItem(QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding))

        label_studente = QLabel("Studente: {} {}".format(self.controller.get_studente_prenotazione().nome, self.controller.get_studente_prenotazione().cognome))
        font_studente = label_studente.font()
        font_studente.setPointSize(30)
        label_studente.setFont(font_studente)
        v_layout.addWidget(label_studente)

        label_data = QLabel("data: {}".format(self.controller.get_data_prenotazione()))
        font_data = label_data.font()
        font_data.setPointSize(30)
        label_data.setFont(font_data)
        v_layout.addWidget(label_data)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_disdici = QPushButton("Disdici")
        btn_disdici.clicked.connect(self.disdici_prenotazione_click)
        v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_libro_prenotazione().titolo)

    def disdici_prenotazione_click(self):
        self.disdici_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from studente.controller.ControlloreStudente import ControlloreStudente


class VistaStudente(QWidget):
    def __init__(self, studente, elimina_studente, elimina_callback, parent=None):
        super(VistaStudente, self).__init__(parent)
        self.controller = ControlloreStudente(studente)
        self.elimina_studente = elimina_studente
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_studente() + " " + self.controller.get_cognome_studente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_studente()))
        v_layout.addWidget(self.get_label_info("Indirizzo", self.controller.get_indirizzo_studente()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_studente()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_studente()))
        v_layout.addWidget(self.get_label_info("Età", self.controller.get_eta_studente()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))



        #v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_studente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_studente() + " " + self.controller.get_cognome_studente())

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label



    def elimina_studente_click(self):
        self.elimina_studente(self.controller.get_id_studente())
        self.elimina_callback()
        self.close()
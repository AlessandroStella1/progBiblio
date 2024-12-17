from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from libro.model.Libro import Libro


class VistaInserisciLibro(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciLibro, self).__init__()
        self.controller = controller
        self.callback = callback


        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("titolo", "Titolo")
        self.add_info_text("categoria", "Categoria")


        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_libro)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Libro")


    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_libro(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.aggiungi_libro(Libro(
            (self.qlines["titolo"].text() + self.qlines["categoria"].text()).lower(),
            self.qlines["titolo"].text(),
            self.qlines["categoria"].text())

        )
        self.callback()
        self.close()
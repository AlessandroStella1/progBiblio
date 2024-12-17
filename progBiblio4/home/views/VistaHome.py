from PyQt5 import uic

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy



from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listalibri.views.VistaListaLibri import VistaListaLibri
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaprenotazioniposto.controller.ControlloreListaPrenotazioniPosto import ControlloreListaPrenotazioniPosto
from listaprenotazioniposto.views.VistaListaPrenotazioniPosto import VistaListaPrenotazioniPosto
from listastudenti.views.VistaListaStudenti import VistaListaStudenti


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        uic.loadUi('Vista/HOMEForm.ui',self)
        self.show()
        grid_layout = QGridLayout()


        grid_layout.addWidget(self.get_generic_button("Lista Libri", self.go_lista_libri), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Studenti", self.go_lista_studenti), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_lista_prenotazioni), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni Posto", self.go_lista_prenotazioni_posto), 1, 2)

        self.setLayout(grid_layout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Biblioteca")
        self.controller_lista_prenotazioni_posto = ControlloreListaPrenotazioniPosto()
        self.controller_lista_prenotazioni_posto.elimina_prenotazioni_scadute()
        # Imposta un timer per controllare le prenotazioni scadute periodicamente
        self.setup_timer()



    def get_generic_button(self, titolo, on_click=None):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_lista_libri(self):
        self.vista_lista_libri = VistaListaLibri()
        self.vista_lista_libri.show()

    def go_lista_studenti(self):
        self.vista_lista_studenti = VistaListaStudenti()
        self.vista_lista_studenti.show()

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_lista_prenotazioni_posto(self):
        self.vista_lista_prenotazioni_posto = VistaListaPrenotazioniPosto()
        self.vista_lista_prenotazioni_posto.show()

    def setup_timer(self):
    # Timer che scatta ogni 10 minuti (600000 millisecondi)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.controller_lista_prenotazioni_posto.elimina_prenotazioni_scadute)
        self.timer.start(600000)  # Controlla ogni 10 minuti



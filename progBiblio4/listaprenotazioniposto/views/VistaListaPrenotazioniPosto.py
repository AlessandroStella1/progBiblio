from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton
from listaprenotazioniposto.controller.ControlloreListaPrenotazioniPosto import ControlloreListaPrenotazioniPosto
from listaprenotazioniposto.views.VistaInserisciPrenotazioniPosto import VistaInserisciPrenotazioniPosto
from prenotazioneposto.views.VistaPrenotazionePosto import VistaPrenotazionePosto

class VistaListaPrenotazioniPosto(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPrenotazioniPosto, self).__init__(parent)
        self.controller = ControlloreListaPrenotazioniPosto()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        book_button = QPushButton("Prenota Posto")
        book_button.clicked.connect(self.show_new_prenotazione_posto)
        buttons_layout.addWidget(book_button)

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Prenotazioni Posto')

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)

        for prenotazione in self.controller.get_lista_delle_prenotazioni_posto():
            item = QStandardItem()
            item.setText(f"Studente: {prenotazione.studente.nome} {prenotazione.studente.cognome} - Posto {prenotazione.posto.id}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)

        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            prenotazione = self.controller.get_prenotazione_posto_by_index(selected)
            if prenotazione is None:
                print("Errore: prenotazione non trovata.")
                return
            self.vista_prenotazione_posto = VistaPrenotazionePosto(prenotazione,
                                                                   self.controller.elimina_prenotazione_posto,
                                                                   self.update_ui)
            self.vista_prenotazione_posto.show()

    def show_new_prenotazione_posto(self):
        self.vista_inserisci_prenotazioni_posto = VistaInserisciPrenotazioniPosto(self.controller, self.update_ui)
        self.vista_inserisci_prenotazioni_posto.show()
        pass

    def closeEvent(self, event):
        try:
            self.controller.save_data()
            print("Dati salvati con successo.")
        except Exception as e:
            print(f"Errore durante il salvataggio dei dati: {e}")


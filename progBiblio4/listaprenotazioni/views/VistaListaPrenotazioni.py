from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaprenotazioni.views.VistaInserisciPrenotazione import VistaInserisciPrenotazione

from prenotazione.views.VistaPrenotazione import VistaPrenotazione



class VistaListaPrenotazioni(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPrenotazioni, self).__init__(parent)

        self.controller = ControlloreListaPrenotazioni()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        book_button = QPushButton("Prenota Libro")
        book_button.clicked.connect(self.show_new_prenotazione)
        buttons_layout.addWidget(book_button)

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle('Lista Prenotazioni')



    def update_ui(self):
        # Crea un nuovo modello della lista
        self.listview_model = QStandardItemModel(self.list_view)

        # Aggiungi le prenotazioni da get_lista_delle_prenotazioni
        for prenotazione in self.controller.get_lista_delle_prenotazioni():
            item = QStandardItem()
            item.setText(f"{prenotazione.studente.cognome} {prenotazione.studente.nome} - Libro")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            prenotazione = self.controller.get_prenotazione_by_index(selected)
            self.vista_prenotazione = VistaPrenotazione(prenotazione,
                                                        self.controller.elimina_prenotazione_by_id, self.update_ui)
            self.vista_prenotazione.show()


    def show_new_prenotazione(self):
        self.vista_inserisci_prenotazione = VistaInserisciPrenotazione(self.controller, self.update_ui)
        self.vista_inserisci_prenotazione.show()
        pass

    def closeEvent(self, event):
        self.controller.save_data()
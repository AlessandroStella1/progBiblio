from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listastudenti.controller.ControlloreListaStudenti import ControlloreListaStudenti
from listastudenti.views.VistaInserisciStudente import VistaInserisciStudente
from studente.views.VistaStudente import VistaStudente


class VistaListaStudenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaStudenti, self).__init__(parent)

        self.controller = ControlloreListaStudenti()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_studente)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista Studenti")

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        studente_selezionato = self.controller.get_studente_by_index(selected)
        self.vista_studente = VistaStudente(studente_selezionato, self.controller.elimina_studente_by_id, self.update_ui)
        self.vista_studente.show()

    def show_new_studente(self):
        self.vista_inserisci_studente = VistaInserisciStudente(self.controller, self.update_ui)
        self.vista_inserisci_studente.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for studente in self.controller.get_lista_degli_studenti():
            item = QStandardItem()
            item.setText(studente.nome + " " + studente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()

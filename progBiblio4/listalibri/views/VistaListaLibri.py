from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from libro.views.VistaLibro import VistaLibro
from listalibri.controller.ControlloreListaLibri import ControlloreListaLibri
from listalibri.views.VistaInserisciLibro import VistaInserisciLibro


class VistaListaLibri(QWidget):
    def __init__(self, parent = None):
        super(VistaListaLibri, self).__init__(parent)

        self.controller = ControlloreListaLibri()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        for libro in self.controller.get_lista_dei_libri():
            item = QStandardItem()
            item.setText(libro.titolo)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_libro)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Libri')

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        libro_selezionato = self.controller.get_libro_by_index(selected)
        self.vista_libro = VistaLibro(libro_selezionato,  self.controller.elimina_libro_by_id, self.update_ui)
        self.vista_libro.show()

    def show_new_libro(self):
        self.vista_inserisci_libro = VistaInserisciLibro(self.controller, self.update_ui)
        self.vista_inserisci_libro.show()

    def update_ui(self):
        self.list_view_model = QStandardItemModel(self.list_view)
        for libro in self.controller.get_lista_dei_libri():
            item = QStandardItem()
            item.setText(libro.titolo)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from libro.controller.ControlloreLibro import ControlloreLibro


class VistaLibro(QWidget):
    def __init__(self, libro, elimina_libro, elimina_callback, parent=None):
        super(VistaLibro, self).__init__(parent)
        self.controller = ControlloreLibro(libro)
        self.elimina_libro = elimina_libro
        self.elimina_callback = elimina_callback

        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()
        label_titolo = QLabel(self.controller.get_titolo_libro())
        font_titolo = label_titolo.font()
        font_titolo.setPointSize(30)
        label_titolo.setFont(font_titolo)
        v_layout.addWidget(label_titolo)


        label_categoria = QLabel("Categoria: {}".format(self.controller.get_categoria_libro()))
        font_categoria = label_categoria.font()
        font_categoria.setPointSize(15)
        label_categoria.setFont(font_categoria)
        v_layout.addWidget(label_categoria)
        h_layout.addLayout(v_layout)

        #v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        h_layout.addItem(QSpacerItem(50, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout2 = QVBoxLayout()
        label_disponibile = QLabel(self.controller.get_libro_disponibile())
        font_disponibile = label_disponibile.font()
        font_disponibile.setPointSize(20)
        label_disponibile.setFont(font_disponibile)
        v_layout2.addWidget(label_disponibile)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_libro_click)

        v_layout.addWidget(btn_elimina)

        h_layout.addLayout(v_layout2)

        self.setLayout(h_layout)
        self.setWindowTitle(libro.titolo)

    def elimina_libro_click(self):
        self.elimina_libro(self.controller.get_id_libro())
        self.elimina_callback()
        self.close()


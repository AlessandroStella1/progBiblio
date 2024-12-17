from listalibri.model.ListaLibri import ListaLibri


class ControlloreListaLibri():
    def __init__(self):
        super(ControlloreListaLibri, self).__init__()
        self.model = ListaLibri()

    def aggiungi_libro(self, libro):
        self.model.aggiungi_libro(libro)

    def get_lista_dei_libri(self):
        return self.model.get_lista_libri()

    def get_libro_by_index(self, index):
        return self.model.get_libro_by_index(index)

    def elimina_libro_by_id(self, id):
        self.model.rimuovi_libro_by_id(id)

    def save_data(self):
        self.model.save_data()
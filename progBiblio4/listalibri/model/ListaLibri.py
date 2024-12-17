import json
import pickle
import os.path

from libro.model.Libro import Libro


class ListaLibri():

    def __init__(self):
        super(ListaLibri, self).__init__()
        self.lista_libri = []
        if os.path.isfile('listalibri/data/lista_libri_salvata.pickle'):
            with open('listalibri/data/lista_libri_salvata.pickle', 'rb') as f:
                self.lista_libri = pickle.load(f)
        else:
            with open('listalibri/data/lista_libri_iniziali.json') as f:
                lista_libri_iniziali = json.load(f)
            for libro_iniziale in lista_libri_iniziali:
                self.aggiungi_libro(Libro(libro_iniziale["id"], libro_iniziale["titolo"], libro_iniziale["categoria"]))


    def aggiungi_libro(self, libro):
        self.lista_libri.append(libro)

    def get_libro_by_index(self, index):
        return self.lista_libri[index]

    def get_lista_libri(self):
        return self.lista_libri

    def rimuovi_libro_by_id(self, id):
        def is_selected_libro(libro):
            if libro.id == id:
                return True
            return False
        self.lista_libri.remove(list(filter(is_selected_libro, self.lista_libri))[0])

    def save_data(self):
        with open('listalibri/data/lista_libri_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_libri, handle, pickle.HIGHEST_PROTOCOL)
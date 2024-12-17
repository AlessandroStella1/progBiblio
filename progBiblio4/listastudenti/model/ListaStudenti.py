import os
import pickle


class ListaStudenti():
    def __init__(self):
        super(ListaStudenti, self).__init__()
        self.lista_studenti = []
        if os.path.isfile('listastudenti/data/lista_studenti_salvata.pickle'):
            with open('listastudenti/data/lista_studenti_salvata.pickle', 'rb') as f:
                self.lista_studenti = pickle.load(f)

    def aggiungi_studente(self, studente):
        self.lista_studenti.append(studente)

    def rimuovi_studente_by_id(self, id):
        def is_selected_studente(studente):
            if studente.id == id:
                return True
            return False
        self.lista_studenti.remove(list(filter(is_selected_studente, self.lista_studenti))[0])

    def get_studente_by_index(self, index):
        return self.lista_studenti[index]

    def get_lista_studenti(self):
        return self.lista_studenti

    def save_data(self):
        with open('listastudenti/data/lista_studenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_studenti, handle, pickle.HIGHEST_PROTOCOL)


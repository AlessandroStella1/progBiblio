from listastudenti.model.ListaStudenti import ListaStudenti


class ControlloreListaStudenti():
    def __init__(self):
        super(ControlloreListaStudenti, self).__init__()
        self.model = ListaStudenti()

    def aggiungi_studente(self, studente):
        self.model.aggiungi_studente(studente)

    def get_lista_degli_studenti(self):
         return self.model.get_lista_studenti()

    def get_studente_by_index(self, index):
        return self.model.get_studente_by_index(index)

    def elimina_studente_by_id(self, id):
        self.model.rimuovi_studente_by_id(id)

    def save_data(self):
        self.model.save_data()
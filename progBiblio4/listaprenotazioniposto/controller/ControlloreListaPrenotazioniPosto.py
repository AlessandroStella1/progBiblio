from listaprenotazioniposto.model.ListaPrenotazioniPosto import ListaPrenotazioniPosto


class ControlloreListaPrenotazioniPosto():
    def __init__(self):
        self.model = ListaPrenotazioniPosto()

    def aggiungi_prenotazione_posto(self, prenotazione):
        self.model.aggiungi_prenotazione_posto(prenotazione)

    def elimina_prenotazione_posto(self, id):
        return self.model.rimuovi_prenotazione_posto(id)

    def get_lista_delle_prenotazioni_posto(self):
        return self.model.get_lista_prenotazioni_posto()


    def get_prenotazione_posto_by_index(self, index):
        return self.model.get_prenotazione_posto_by_index(index)

    def get_posti_disponibili(self):
        return self.model.get_posti_disponibili()

    def elimina_prenotazioni_scadute(self):
        return self.model.elimina_prenotazioni_scadute()

    def save_data(self):
        self.model.save_data()

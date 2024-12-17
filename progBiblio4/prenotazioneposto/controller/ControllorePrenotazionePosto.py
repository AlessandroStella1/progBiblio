


class ControllorePrenotazionePosto():
    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_id_prenotazione(self):
        print(self.model.id)
        return self.model.id

    def get_studente_prenotazione(self):
        return self.model.studente

    def get_data_prenotazione(self):
        return self.model.data_prenotazione

    def get_posto_prenotazione(self):
        return self.model.posto
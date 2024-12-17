class ControlloreStudente():
    def __init__(self, studente):
        self.model = studente

    def get_id_studente(self):
        return self.model.id

    def get_nome_studente(self):
        return self.model.nome

    def get_cognome_studente(self):
        return self.model.cognome

    def get_cf_studente(self):
        return self.model.cf

    def get_indirizzo_studente(self):
        return self.model.indirizzo

    def get_email_studente(self):
        return self.model.email

    def get_telefono_studente(self):
        return self.model.telefono

    def get_eta_studente(self):
        return self.model.eta
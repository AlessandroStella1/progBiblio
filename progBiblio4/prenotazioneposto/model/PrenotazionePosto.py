from datetime import datetime, timedelta

class PrenotazionePosto():
    def __init__(self, id, studente, posto):
        self.id = id
        self.studente = studente
        self.posto = posto
        self.data_prenotazione = datetime.now()

    def scaduta(self):
        return self.data_prenotazione + timedelta(hours=3) < datetime.now()


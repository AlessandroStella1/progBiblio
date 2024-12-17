import os
import pickle

from posto.model.Posto import Posto


class ListaPrenotazioniPosto():
    def __init__(self):
        self.lista_prenotazioni_posto = []
        self.posti = [Posto(i) for i in range(100)]
        if os.path.isfile('listaprenotazioniposto/data/lista_prenotazioni_posto_salvata.pickle'):
            with open('listaprenotazioniposto/data/lista_prenotazioni_posto_salvata.pickle', 'rb') as f:
                self.lista_prenotazioni_posto = pickle.load(f)

    def aggiungi_prenotazione_posto(self, prenotazione):
        self.lista_prenotazioni_posto.append(prenotazione)
        #prenotazione.posto.prendi()

    def rimuovi_prenotazione_posto(self, id):
        for prenotazione in self.lista_prenotazioni_posto:
            if prenotazione.id == id:
                prenotazione.posto.libera()
                self.lista_prenotazioni_posto.remove(prenotazione)
                return True
        return False

    def get_posti_disponibili(self):
        return [posto for posto in self.posti if posto.is_disponibile()]

    def get_lista_prenotazioni_posto(self):
        return self.lista_prenotazioni_posto

    def get_prenotazione_posto_by_index(self, index):
        return self.lista_prenotazioni_posto[index]

    def elimina_prenotazioni_scadute(self):
        prenotazioni_da_eliminare = [prenotazione for prenotazione in self.get_lista_prenotazioni_posto() if
                                     prenotazione.scaduta()]
        for prenotazione in prenotazioni_da_eliminare:
            self.rimuovi_prenotazione_posto(prenotazione.id)

        if prenotazioni_da_eliminare:
            print(f"Eliminate {len(prenotazioni_da_eliminare)} prenotazioni scadute.")
            self.save_data()

    def save_data(self):
        try:
            os.makedirs(os.path.dirname('listaprenotazioniposto/data/lista_prenotazioni_posto_salvata.pickle'), exist_ok=True)
            with open('listaprenotazioniposto/data/lista_prenotazioni_posto_salvata.pickle', 'wb') as handle:
                pickle.dump(self.lista_prenotazioni_posto, handle, pickle.HIGHEST_PROTOCOL)
            print("Prenotazioni salvate correttamente.")
        except Exception as e:
            print(f"Errore durante il salvataggio delle prenotazioni: {e}")

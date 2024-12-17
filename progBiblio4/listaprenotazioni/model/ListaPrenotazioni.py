import os
import pickle






class ListaPrenotazioni():
    def __init__(self):
        super(ListaPrenotazioni, self).__init__()
        self.lista_prenotazioni = []

        if os.path.isfile('listaprenotazioni/data/lista_prenotazioni_salvata.pickle'):
            with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'rb') as f:
                self.lista_prenotazioni = pickle.load(f)



    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)



    def rimuovi_prenotazione_by_id(self, id):
        """Rimuove la prenotazione identificata dall'ID e aggiorna lo stato del libro"""
        for prenotazione in self.lista_prenotazioni:
            print(f"Controlla prenotazione: {prenotazione}, ID: {prenotazione.id}, target ID: {id}")
            if prenotazione.id == id:
                print(f"Ritorna {prenotazione.libro} disponibile")

                # Carica la lista dei libri direttamente all'interno del metodo
                if os.path.isfile('listalibri/data/lista_libri_salvata.pickle'):
                    with open('listalibri/data/lista_libri_salvata.pickle', 'rb') as f:
                        self.lista_libri_salvata = pickle.load(f)
                else:
                    self.lista_libri_salvata = []

                # Cerca il libro prenotato nella lista dei libri
                for libro in self.lista_libri_salvata:
                    if libro.id == prenotazione.libro.id:
                        libro.disponibile = True  # Rendi il libro disponibile
                        break

                # Rimuovi la prenotazione dalla lista
                self.lista_prenotazioni.remove(prenotazione)

                # Salva i dati aggiornati delle prenotazioni e dei libri
                self.save_data()
                self.salva_lista_libri()

    """

    def rimuovi_prenotazione_by_id(self, id: Any) -> bool:
        for prenotazione in self.lista_prenotazioni:
            print(f"Controlla prenotazione: {prenotazione}, ID: {prenotazione.id}, target ID: {id}")
            if prenotazione.id == id:
                print(f"Ritorna {prenotazione.libro} disponibile")
                prenotazione.libro.disponibile = True
                self.lista_prenotazioni.remove(prenotazione)
                self.save_data()
                return True
        return False
        
    """


    def get_prenotazione_by_index(self, index):
        return self.lista_prenotazioni[index]

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    def save_data(self):
        with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)

    def salva_lista_libri(self):
        """Salva la lista dei libri in lista_libri_salvata.pickle"""
        with open('listalibri/data/lista_libri_salvata.pickle', 'wb') as f:
            pickle.dump(self.lista_libri_salvata, f, pickle.HIGHEST_PROTOCOL)

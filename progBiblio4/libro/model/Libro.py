class Libro():
    def __init__(self, id, titolo, categoria):
        super(Libro, self).__init__()
        self.id = id
        self.titolo = titolo
        self.categoria = categoria
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

    def prenota(self):
        self.disponibile = False
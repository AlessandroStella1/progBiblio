class Posto():
    def __init__(self, id):
        self.id = id
        self.disponibile = True

    def prendi(self):
        self.disponibile = False

    def libera(self):
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

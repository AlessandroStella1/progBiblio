class ControlloreLibro():
    def __init__(self, libro):
        self.model = libro

    def get_id_libro(self):
        return self.model.id

    def get_titolo_libro(self):
        return self.model.titolo

    def get_categoria_libro(self):
        return self.model.categoria

    def get_libro_disponibile(self):
        if(self.model.is_disponibile()):
            return "DISPONIBILE"
        else:
            return "NON DISPONIBILE"
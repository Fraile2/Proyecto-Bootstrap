class Padre():
    def __init__(self, nombre) -> None:
        self.nombre=nombre

class Hijo(Padre):
    def __init__(self, nombre, apellidos) -> None:
        super().__init__(nombre)
        self.apellidos=apellidos
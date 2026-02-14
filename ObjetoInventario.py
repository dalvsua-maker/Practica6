import json

class ObjetoInventario:

    def __init__(self,nombre,categoria,contenedor,usos,energia,elemento=None):
        self.nombre=nombre
        self.categoria=categoria
        self.contenedor=contenedor
        self.usos=usos
        self.elemento=elemento
        self.energia=energia

    
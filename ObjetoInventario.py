import json

class ObjetoInventario:
    {
"nombre": "Poción de energía",
"categoria": "recuperacion",
"contenedor": "frasco",
"usos": 2,
"elemento": "electricidad",
"energia": 12
},
    def __init__(self,nombre,categoria,contenedor,usos,energia,elemento=None):
        self.nombre=nombre
        self.categoria=categoria
        self.contenedor=contenedor
        self.usos=usos
        self.elemento=elemento
        self.energia=energia

    
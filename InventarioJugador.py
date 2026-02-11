import json

class InventarioJugador:
    def __init__(self,ruta):
      with open(ruta, 'r', encoding='utf-8') as archivo:
             # 1. Definimos el atributo como una lista vacía (opcional pero buena práctica)
            self.objetos = []
            self.objetos  = json.load(archivo)
           
    def buscarPorEnergia(self,max_energia):
        return [objeto.get("nombre") for objeto in self.objetos if objeto["energia"] <= max_energia]
   






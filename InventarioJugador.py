import json

class InventarioJugador:
    def __init__(self,ruta):
      with open(ruta, 'r', encoding='utf-8') as archivo:
             # 1. Definimos el atributo como una lista vacía (opcional pero buena práctica)
            self.objetos = []
            self.objetos  = json.load(archivo)
           
    def buscarPorEnergia(self,max_energia):
        return [objeto.get("nombre") for objeto in self.objetos if objeto["energia"] <= max_energia]
   

    def usarObjeto(self,nombre, elemento=None):
        for objeto in self.objetos:
            if objeto["nombre"] == nombre:
                if objeto["usos"]>=1:
                    objeto["usos"]-=1
                if objeto["usos"]==0:
                    self.objetos.remove(objeto)
                return True
            else:
                return False





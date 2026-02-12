import json


class InventarioJugador:
    def __init__(self, ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:

            self.objetos = []
            self.objetos = json.load(archivo)

    def buscarPorEnergia(self, max_energia):
        return [
            objeto.get("nombre")
            for objeto in self.objetos
            if objeto["energia"] <= max_energia
        ]

    def mostrar(self):
        print("\n" + "=" * 80)
        # Imprime la cabecera usando f-strings con formato de alineación:
        # '<' alinea a la izquierda, '>' a la derecha, y el número define el ancho total de la columna.
        print(
            f"{'NOMBRE':<25} | {'CATEGORÍA':<15} | {'ELEM.':<15} | {'ENERGÍA':>7} | {'USOS':>4}"
        )
        print("-" * 80)

        for item in self.objetos:
            elem = item.get("elemento") if item.get("elemento") else "N/A"
            nombre = item.get("nombre", "Sin nombre")
            cat = item.get("categoria", "Sin cat.")
            energia = item.get("energia", 0)
            usos = item.get("usos", 0)
            print(f"{nombre:<25} | {cat:<15} | {elem:<15} | {energia:>7} | {usos:>4}")

        print("=" * 80 + "\n")

    def usarObjeto(self, nombre, elemento=None):
        for objeto in self.objetos:
            if objeto["nombre"] == nombre and (
                objeto["elemento"].casefold() == elemento.casefold()
                or objeto["elemento"] == None
            ):
                if objeto["usos"] >= 1:
                    objeto["usos"] -= 1
                if objeto["usos"] == 0:
                    self.objetos.remove(objeto)
                return True
            else:
                return False

    def consultarUsos(self, nombre=None, categoria=None, elemento=None):
        match = []
        for objeto in self.objetos:
            #Para encapsular condiciones usamos if((condicion multiple1)and(condicion multiple2))
            if (
                (nombre is None or nombre.casefold() == objeto["nombre"].casefold())
                and (categoria is None or categoria.casefold() == objeto["categoria"].casefold())
                and (elemento is None or elemento.casefold() == objeto["elemento"].casefold())
            ):
                match.append(objeto)
        if len(match) > 0:
            for objeto in match:
                print(f"{objeto['nombre']} usos: {objeto['usos']}")
        else:
            print("No hay coincidencias")

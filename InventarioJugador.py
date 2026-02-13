import json
import unicodedata

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

    @staticmethod
    def normalizar(texto):
        """Elimina acentos y convierte a minúsculas"""
        if texto is None:
            return None
        texto_nfd = unicodedata.normalize('NFD', texto)
        texto_sin_acentos = ''.join(c for c in texto_nfd if unicodedata.category(c) != 'Mn')
        return texto_sin_acentos.casefold()
    
    def usarObjeto(self, nombre, elemento=None):
        nombre_buscar = self.normalizar(nombre)
        
        for objeto in self.objetos:
            if self.normalizar(objeto["nombre"]) != nombre_buscar:
                continue
            
            if elemento is not None:
                obj_elem = objeto.get("elemento")
                if obj_elem is None or self.normalizar(obj_elem) != self.normalizar(elemento):
                    continue
            
            if objeto["usos"] >= 1:
                objeto["usos"] -= 1
            if objeto["usos"] == 0:
                self.objetos.remove(objeto)
            return True

    def consultarUsos(self, nombre=None, categoria=None, elemento=None):
        match = []
        for objeto in self.objetos:
            #Para encapsular condiciones usamos if((condicion multiple1)and(condicion multiple2))
            if (
                (nombre is None or (objeto.get("nombre") and nombre.casefold() == objeto["nombre"].casefold()))
                and (categoria is None or (objeto.get("categoria") and categoria.casefold() == objeto["categoria"].casefold()))
                and (elemento is None or (objeto.get("elemento") and elemento.casefold() == objeto["elemento"].casefold()))
            ):
                match.append(objeto)
        if len(match) > 0:
            for objeto in match:
                print(f"{objeto['nombre']} usos: {objeto['usos']}")
        else:
            print("No hay coincidencias")
    def estrategiaSobrecarga(self):
        #usamos diccionarios (key-value) para almacenar las categorias con su energia total 
        # y otro que almacene los objetos por categoria 
        energia_por_categoria = {}
        objetos_por_categoria = {}
        #por cada objeto en inventario
        for objeto in self.objetos:
            #almacenamos la categoria del objeto actual
            cat = objeto["categoria"] 
            #calculamos cuanta energia total nos da con todos sus usos
            energia_objeto = objeto["usos"] * objeto["energia"] 
            #Si no existe la categoria del objeto la creamos en cada diccionario(una solo 
            # almacena el total de energia por categoria y
            #  otra almacena una lista de objetos por categoria)
            if cat not in energia_por_categoria:
                energia_por_categoria[cat] = 0
                objetos_por_categoria[cat] = []
            #Sumamos la energia del objeto a su categoria y lo añadimos a su lista de categoria
            energia_por_categoria[cat] += energia_objeto
            objetos_por_categoria[cat].append(objeto.get("nombre"))
        #Si no hay info se devuelve una lista vacia
        if not energia_por_categoria:
            return []

        # Buscamos la categoría con el total de energía más alto
        categoria_ganadora = max(energia_por_categoria, key=energia_por_categoria.get)
        print(categoria_ganadora)
        # Devolvemos la lista de diccionarios de esa categoría
        return objetos_por_categoria[categoria_ganadora]



                
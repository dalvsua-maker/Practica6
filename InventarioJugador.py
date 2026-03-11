import os
import json
import unicodedata  
from ObjetoInventario import ObjetoInventario

class InventarioJugador:
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase InventarioJugador.
        
        Abre el archivo en la ruta especificada y carga los datos en un
        objeto de tipo ObjetoInventario.
        
        Parameters:
            nombre_archivo (str): Nombre del archivo a cargar.
        """
        
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_completa = os.path.join(dir_actual, nombre_archivo)
        
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            datos_json = json.load(archivo)
        
        # Convertir cada diccionario en un objeto ObjetoInventario
        self.objetos = [
            ObjetoInventario(
                nombre=item["nombre"],
                categoria=item["categoria"],
                contenedor=item["contenedor"],
                usos=item["usos"],
                energia=item["energia"],
                elemento=item.get("elemento")  # Usa get() por si es None
            )
            for item in datos_json
        ]

    def buscarPorEnergia(self, max_energia):
        """
        Busca objetos en el inventario cuya energia sea menor o igual a una
        cantidad dada.

        Parameters:
            max_energia (int): Energ a maxima a buscar.

        Returns:
            list(str): Lista de nombres de objetos que cumplen con la condicion.
        """
        return [
            objeto.nombre
            for objeto in self.objetos
            if objeto.energia <= max_energia
        ]

    def mostrar(self):
        """
        Muestra en pantalla todos los objetos del inventario.
        
        La salida se mostrar  con una linea de igualdad en la parte
        superior y una en la parte inferior, y mostrar  los objetos con
        la siguiente estructura:
        
        NOMBRE         | CATEGOR I | ELEM.      | ENERGIA   | USOS     
        ------------------------------------------------------------
        <nombre>      | <categoria> | <elemento> | <energia> | <usos>
        ------------------------------------------------------------
        
        Donde <nombre> es el nombre del objeto, <categoria> es la
        categor a a la que pertenece, <elemento> es el elemento del objeto
        (si es que tiene), <energia> es la energia del objeto y <usos> son
        los usos del objeto.
        """
        print("\n" + "=" * 80)
        print(
            f"{'NOMBRE':<25} | {'CATEGORÍA':<15} | {'ELEM.':<15} | {'ENERGÍA':>7} | {'USOS':>4}"
        )
        print("-" * 80)

        for item in self.objetos:
            elem = item.elemento if item.elemento else "N/A"
            print(f"{item.nombre:<25} | {item.categoria:<15} | {elem:<15} | {item.energia:>7} | {item.usos:>4}")

        print("=" * 80 + "\n")

 

    @staticmethod
    def normalizar(texto):
        """
        Normaliza un texto quitandole los acentos y convirtiendo
        a mayusculas.
        
        Parameters:
            texto (str): Texto a normalizar.
        
        Returns:
            str: Texto normalizado.
        """
        if texto is None:
            return None
        texto_nfd = unicodedata.normalize('NFD', texto)
        texto_sin_acentos = ''.join(c for c in texto_nfd if unicodedata.category(c) != 'Mn')
        return texto_sin_acentos.casefold()

    def usarObjeto(self, nombre, elemento=None):
        """
        Busca un objeto en la lista de objetos y lo utiliza si coincide
        con el nombre y elemento dados. Si el objeto tiene usos
        disponibles, se reduce en uno el numero de usos y si se
        llega a 0, se elimina del inventario.
        
        Parameters:
            nombre (str): Nombre del objeto a buscar.
            elemento (str, optional): Elemento del objeto a buscar.
                Defaults to None.
        
        Returns:
            bool: True si se encuentra y se utiliza el objeto, False
                en caso contrario.
        """
        nombre_buscar = self.normalizar(nombre)
        
        for objeto in self.objetos:
            if self.normalizar(objeto.nombre) != nombre_buscar:
                continue
            
            if elemento is not None:
                if objeto.elemento is None or self.normalizar(objeto.elemento) != self.normalizar(elemento):
                    continue
            
            if objeto.usos >= 1:
                objeto.usos -= 1
            if objeto.usos == 0:
                self.objetos.remove(objeto)
            return True
        
        return False

    def consultarUsos(self, nombre=None, categoria=None, elemento=None):
        """
        Busca objetos en el inventario que coinciden con el nombre,
        categoria y elemento dados. Si se encuentra al menos un objeto,
        se imprimen por pantalla el nombre del objeto y su numero de
        usos. Si no se encuentra ningun objeto, se imprime por pantalla
        un mensaje indicando que no hay coincidencias.
        
        Parameters:
            nombre (str, optional): Nombre del objeto a buscar.
                Defaults to None.
            categoria (str, optional): Categoria del objeto a buscar.
                Defaults to None.
            elemento (str, optional): Elemento del objeto a buscar.
                Defaults to None.
        """
        match = []
        for objeto in self.objetos:
            if (
                (nombre is None or self.normalizar(nombre) == self.normalizar(objeto.nombre))
                and (categoria is None or self.normalizar(categoria) == self.normalizar(objeto.categoria))
                and (elemento is None or (objeto.elemento and self.normalizar(elemento) == self.normalizar(objeto.elemento)))
            ):
                match.append(objeto)
        
        if len(match) > 0:
            for objeto in match:
                print(f"{objeto.nombre} usos: {objeto.usos}")
        else:
            print("No hay coincidencias")
    def estrategiaSobrecarga(self):
        """
        Calcula la categoría que más energía sobrará y devuelve una tupla con
        la categoría y una lista de objetos que la componen.
        
        Returns:
            tuple: Una tupla con la categoría ganadora y una lista de objetos
                que la componen. Si no hay objetos en el inventario, devuelve
                (None, []).
        """
        
        energia_por_categoria = {}
        objetos_por_categoria = {}
        
        for objeto in self.objetos:
            cat = objeto.categoria
            energia_objeto = objeto.usos * objeto.energia
            
            if cat not in energia_por_categoria:
                energia_por_categoria[cat] = 0
                objetos_por_categoria[cat] = []
            
            energia_por_categoria[cat] += energia_objeto
            objetos_por_categoria[cat].append(objeto.nombre)
        
        if not energia_por_categoria:
            return None, []
        
        categoria_ganadora = max(energia_por_categoria, key=energia_por_categoria.get)
        
        return categoria_ganadora, objetos_por_categoria[categoria_ganadora]


                
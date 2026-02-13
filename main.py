from InventarioJugador import InventarioJugador
inv = InventarioJugador("inventario.json")
inv.mostrar()
inv.usarObjeto(nombre="Botiquin")
inv.usarObjeto(nombre="Botiquin")
inv.mostrar()
print(inv.estrategiaSobrecarga())



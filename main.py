from InventarioJugador import InventarioJugador
inv = InventarioJugador("inventario.json")
inv.mostrar()
print(inv.buscarPorEnergia(max_energia=50))
print(inv.usarObjeto(nombre="antidoto"))
inv.mostrar()
inv.consultarUsos(elemento="fuego")
inv.consultarUsos(categoria="cura")
inv.consultarUsos(nombre="Lava de flabalaba")
inv.mostrar()
print(inv.estrategiaSobrecarga())






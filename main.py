from InventarioJugador import InventarioJugador
mi_inv = InventarioJugador("inventario.json")
print(mi_inv.buscarPorEnergia(12))
print(mi_inv.usarObjeto("Poción de energía"))
print(mi_inv.buscarPorEnergia(12))

class VentaInmueble:
    def __init__(self):
        self.ventas_realizadas = 0

    def gestiona_venta(self):
        self.ventas_realizadas += 1
        print(f"Venta de inmueble gestionada con éxito. Total de ventas: {self.ventas_realizadas}")
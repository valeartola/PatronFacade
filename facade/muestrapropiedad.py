class MuestraPropiedad:
    def __init__(self):
        self.propiedades = {
            1: "Casa de 3 habitaciones y 2 baños",
            2: "Departamento de 2 habitaciones, 1 baño",
            3: "Local comercial de 100 m2 en el centro"
        }

    def mostrar_propiedad(self, numero_propiedad: int):
        if numero_propiedad in self.propiedades:
            print(f"Propiedad #{numero_propiedad}: {self.propiedades[numero_propiedad]}")
        else:
            print(f"Propiedad #{numero_propiedad} no encontrada.")
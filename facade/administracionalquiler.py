class AdministracionAlquiler:
    def __init__(self):
        self.total_cobrado = 0

    def cobro(self, monto: float):
        self.total_cobrado += monto
        print(f"Alquiler cobrado: ${monto}")

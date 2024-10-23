class CuentasAPagar:
    def __init__(self):
        self.total_pagado = 0

    def pago_propietario(self, monto: float):
        self.total_pagado += monto
        print(f"Pago realizado al propietario: ${monto}")

from inmobiliaria import *

if __name__ == "__main__":
    cliente = Cliente()
    interesado = Interesado()

    inmobiliaria = Inmobiliaria()
    inmobiliaria.atencion_cliente(cliente)
    inmobiliaria.atencion_interesado(interesado)

    muestra_propiedad = MuestraPropiedad()
    muestra_propiedad.mostrar_propiedad(3)

    venta = VentaInmueble()
    venta.gestiona_venta()

    alquiler = AdministracionAlquiler()
    alquiler.cobro(1200)

    cuentas_a_pagar = CuentasAPagar()
    cuentas_a_pagar.pago_propietario(1100)

    inmobiliaria2 = Inmobiliaria()
    inmobiliaria2.atencion_interesado(interesado)
    inmobiliaria2.atencion_cliente(cliente)
    inmobiliaria2.muestraPropiedad.mostrar_propiedad(1)
    inmobiliaria2.ventaInmueble.gestiona_venta()
    inmobiliaria2.administracionAlquiler.cobro(1500)
    inmobiliaria2.cuentaAPagar.pago_propietario(2100)

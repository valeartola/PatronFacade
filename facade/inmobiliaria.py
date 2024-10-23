from administracionalquiler import AdministracionAlquiler
from muestrapropiedad import MuestraPropiedad
from ventainmuebles import VentaInmueble
from cuentasapagar import CuentasAPagar
from persona import Persona
from cliente import Cliente
from propietario import Propietario
from interesado import Interesado

class Inmobiliaria:
    def __init__(self):
        self.muestraPropiedad = MuestraPropiedad()
        self.ventaInmueble = VentaInmueble()
        self.cuentaAPagar = CuentasAPagar()
        self.administracionAlquiler = AdministracionAlquiler()

    def atencion_cliente(self, cliente: Cliente):
        print ("Atendiendo un cliente")

    def atencion_propietario(self, propietario: Propietario):
        print("Atendiendo a un propietario")

    def atencion_interesado(self, interesado: Interesado):
        print("Atención a un interesado en una propiedad")

    def atencion(self, persona: Persona):
        if isinstance(persona, Cliente):
            self.atencion_cliente(persona)
        elif isinstance(persona, Propietario):
            self.atencion_propietario(persona)
        elif isinstance(persona, Interesado):
            self.atencion_interesado(persona)
        else:
            print("Tipo de persona no reconocido")

    
class Configuracion:
    __instancia = None  # Variable privada para almacenar la instancia única

    def __init__(self):
        if Configuracion.__instancia is not None:
            raise Exception("Esta clase es un Singleton, ya existe una instancia creada. Utilice obtener_instancia() para obtenerla.")
        else:
            Configuracion.__instancia = self
            self.__opcion = None

    @staticmethod
    def obtener_instancia():
        if Configuracion.__instancia is None:
            Configuracion()
        return Configuracion.__instancia

    def obtener_opcion(self):
        return self.__opcion

    def establecer_opcion(self, opcion):
        self.__opcion = opcion


# Uso del Singleton en diferentes partes del programa
configuracion1 = Configuracion.obtener_instancia()
configuracion1.establecer_opcion("Opción 1")

configuracion2 = Configuracion.obtener_instancia()
print("Opción obtenida desde configuracion2:", configuracion2.obtener_opcion())

# Intentar crear una nueva instancia generará una excepción
try:
    configuracion3 = Configuracion()
except Exception as e:
    print("Excepción:", e)

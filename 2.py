class Vehiculo:
    def __init__(self, modelo, año, color):
        self.__modelo = modelo
        self.__año = año
        self.__color = color

    # Getter para el atributo modelo
    def obtener_modelo(self):
        return self.__modelo

    # Setter para el atributo modelo
    def establecer_modelo(self, modelo):
        self.__modelo = modelo

    # Getter para el atributo año
    def obtener_año(self):
        return self.__año

    # Setter para el atributo año
    def establecer_año(self, año):
        self.__año = año

    # Getter para el atributo color
    def obtener_color(self):
        return self.__color

    # Setter para el atributo color
    def establecer_color(self, color):
        self.__color = color

    def mostrar_informacion(self):
        print(f"Modelo: {self.__modelo}")
        print(f"Año: {self.__año}")
        print(f"Color: {self.__color}")

# Instanciación de dos objetos de la clase Vehiculo
vehiculo1 = Vehiculo("Toyota Corolla", 2022, "Azul")
vehiculo2 = Vehiculo("Honda Civic", 2020, "Rojo")

# Mostrar información de los vehículos
print("Información del vehículo 1:")
vehiculo1.mostrar_informacion()
print()

print("Información del vehículo 2:")
vehiculo2.mostrar_informacion()
print()

# Modificar atributos de un vehículo utilizando setters
vehiculo1.establecer_color("Blanco")
vehiculo2.establecer_año(2021)

# Mostrar información actualizada de los vehículos
print("Información actualizada del vehículo 1:")
vehiculo1.mostrar_informacion()
print()

print("Información actualizada del vehículo 2:")
vehiculo2.mostrar_informacion()

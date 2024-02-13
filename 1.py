import datetime

class Tarea:
    def __init__(self, nombre, descripcion, fecha_vencimiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas_pendientes(self):
        print("Tareas pendientes:")
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for idx, tarea in enumerate(self.tareas, start=1):
                print(f"Tarea {idx}:")
                print(f"Nombre: {tarea.nombre}")
                print(f"Descripción: {tarea.descripcion}")
                print(f"Fecha de vencimiento: {tarea.fecha_vencimiento}")
                print()


sistema = SistemaGestionTareas()

# Ejemplo de ingreso de tareas
tarea1 = Tarea("Completar informe", "Redactar el informe mensual de ventas", datetime.datetime(2024, 2, 20))
tarea2 = Tarea("Enviar correo electrónico", "Enviar recordatorio de reunión a todos los miembros del equipo", datetime.datetime(2024, 2, 15))
tarea3 = Tarea("Preparar presentación", "Preparar la presentación para el cliente", datetime.datetime(2024, 2, 25))

sistema.agregar_tarea(tarea1)
sistema.agregar_tarea(tarea2)
sistema.agregar_tarea(tarea3)

# Mostrar tareas pendientes
sistema.mostrar_tareas_pendientes()

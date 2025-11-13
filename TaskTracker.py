from datetime import date
import os
import json
# today = date.today()
# print(today)


class Task():
    def __init__(self):
        self.almacen_tareas = {}
        self.lista = []
        self.id = 1
        self.fecha_de_creacion = date.today()
        self.fecha_de_ultima_actualización = date.today()


    def crear_archivo(self):
        if not os.path.exists("data.json"):
            with open("data.json", "w") as f:
                json.dump({"tareas": []}, f, indent=4)  # o [] si querés una lista


    def leer_archivo(self):
        with open("data.json", "r") as f:
            try:
                self.almacen_tareas = json.load(f)
                print("Contenido del archivo:", self.almacen_tareas)
                for valor in self.almacen_tareas.values():
                    print(len(valor))
                    for tarea in valor:
                        if self.id == tarea["id"]:
                            for clave, dato in tarea.items():
                                print(f"{clave}: {dato}")
                print(type(self.almacen_tareas))
                return self.almacen_tareas
            except json.JSONDecodeError:
                self.almacen_tareas = {}  # o [] si esperás una lista


    def escribir_archivo(self):
        with open("data.json", "w") as f:
            json.dump(self.almacen_tareas, f, indent=4)
            return "Tarea guardada en el archivo data.json"


    def agregar(self, descripcion, estado):
        # Leer archivo existente
        with open("data.json", "r") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                datos = {"tareas": []}
        # Obtener la lista de tareas existentes
        if "tareas" not in datos:
            datos["tareas"] = []
        # Calcular el nuevo ID
        if datos["tareas"]:
            nuevo_id = max([tarea["id"] for tarea in datos["tareas"]]) + 1
        else:
            nuevo_id = 1
        # Crear nueva tarea
        nueva_tarea = {
            "id": nuevo_id,
            "descripcion": descripcion,
            "estado": estado,
            "fecha de creacion": str(self.fecha_de_creacion),
            "fecha de actualizacion": str(self.fecha_de_ultima_actualización)
        }
        # Agregar la nueva tarea a la lista
        datos["tareas"].append(nueva_tarea)
        # Escribir todo de vuelta al archivo
        with open("data.json", "w") as f:
            json.dump(datos, f, indent=4)
        self.id = nuevo_id + 1
        return f"Tarea '{descripcion}' agregada con exito."


    def actualizar_estado(self, id, estado):
        # Leer archivo existente
        with open("data.json", "r") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                return "Error al leer el archivo"
        # Buscar y actualizar la tarea
        if "tareas" in datos:
            for tarea in datos["tareas"]:
                if tarea["id"] == int(id):
                    tarea["estado"] = estado
                    tarea["fecha de actualizacion"] = str(date.today())
                    # Escribir de vuelta
                    with open("data.json", "w") as f:
                        json.dump(datos, f, indent=4)
                    return "Tarea actualizada con exito"
        return "No existe tarea con ese id.!!"


    def eliminar(self, id):
        # Leer archivo existente
        with open("data.json", "r") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                return "Error al leer el archivo"
        # Buscar y eliminar la tarea
        if "tareas" in datos:
            for i, tarea in enumerate(datos["tareas"]):
                if tarea["id"] == int(id):
                    del datos["tareas"][i]
                    # Escribir de vuelta
                    with open("data.json", "w") as f:
                        json.dump(datos, f, indent=4)
                    return "Tarea eliminada con exito"
        return "La tarea con el id ingresado no existe"


    def listar_todas_las_tareas(self):
        with open("data.json", "r") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                print("No hay tareas disponibles")
                return
        if "tareas" in datos and len(datos["tareas"]) > 0:
            for diccionario in datos["tareas"]:
                for clave, valor in diccionario.items():
                    print(f"{clave}: {valor}")
                print("-" * 10)
        else:
            print("No hay tareas disponibles")


    def Listar_todas_las_tareas_completadas(self):
        with open("data.json", "r") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                print("No hay tareas completadas")
                return
        encontrado = False
        if "tareas" in datos:
            for diccionario in datos["tareas"]:
                if diccionario["estado"].lower() == "completada":
                    for clave, valor in diccionario.items():
                        print(f"{clave}: {valor}")
                    print("-" * 10)
                    encontrado = True
        if not encontrado:
            print("No hay tareas completadas")


    def Listar_todas_las_tareas_pendientes(self):
        with open("data.json", "r") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                print("No hay tareas pendientes")
                return
        encontrado = False
        if "tareas" in datos:
            for diccionario in datos["tareas"]:
                if diccionario["estado"].lower() == "pendiente":
                    for clave, valor in diccionario.items():
                        print(f"{clave}: {valor}")
                    print("-" * 10)
                    encontrado = True
        if not encontrado:
            print("No hay tareas pendientes")


    def Listar_todas_las_tareas_en_progreso(self):
        with open("data.json", "r") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                print("No hay tareas en progreso")
                return
        encontrado = False
        if "tareas" in datos:
            for diccionario in datos["tareas"]:
                if diccionario["estado"].lower() == "en progreso":
                    for clave, valor in diccionario.items():
                        print(f"{clave}: {valor}")
                    print("-" * 10)
                    encontrado = True
        if not encontrado:
            print("No hay tareas en progreso")

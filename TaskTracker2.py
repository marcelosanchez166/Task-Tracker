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
                json.dump({}, f, indent=4)  # o [] si querés una lista

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

    def leer_archivo2(self):
        with open("data.json", "r") as f:
            try:
                self.almacen_tareas = json.load(f)
                print("Contenido del archivo:", self.almacen_tareas)
                for valor in self.almacen_tareas.values():
                    print(len(valor))
                    for tarea in valor:
                        return tarea
            except json.JSONDecodeError:
                self.almacen_tareas = {}  # o [] si esperás una lista

    def escribir_archivo(self):
        with open("data.json", "w") as f:
            json.dump(self.almacen_tareas, f, indent=4)
            return "Tarea guardada en el archivo data.json"

    def agregar(self, descripcion, estado):
        self.contenido = self.leer_archivo2()
        print(self.contenido, "type de contenido")
        print(type(self.contenido))
        if self.id not in self.contenido:
            # self.lista.append({"id": self.id, "descripcion": descripcion, "estado": estado,"fecha de creacion": self.fecha_de_creacion, "fecha de actualizacion": self.fecha_de_ultima_actualización})
            self.almacen_tareas = {"id": self.id, "descripcion": descripcion, "estado": estado,
                                   "fecha de creacion": str(self.fecha_de_creacion), "fecha de actualizacion": str(self.fecha_de_ultima_actualización)}
            self.lista.append(self.almacen_tareas)
            self.almacen_tareas = {'tareas': self.lista}
            self.escribir_archivo()
            self.id += 1
            # print(self.lista)
            return f"Tarea {descripcion} agregada con exito."
        else:
            # self.lista.append({"id": self.id, "descripcion": descripcion, "estado": estado,"fecha de creacion": self.fecha_de_creacion, "fecha de actualizacion": self.fecha_de_ultima_actualización})
            self.almacen_tareas = {"id": self.id, "descripcion": descripcion, "estado": estado,
                                   "fecha de creacion": self.fecha_de_creacion, "fecha de actualizacion": self.fecha_de_ultima_actualización}
            self.lista.append(self.almacen_tareas)
            self.almacen_tareas = {'tareas': self.lista}
            self.escribir_archivo()
            self.id += 1
            # print(self.lista)
            return f"Tarea {descripcion} agregada con exito."

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
        for i in range(len(self.lista)):
            if int(id) == self.lista[i]["id"]:
                del self.lista[i]
                return "Tarea eliminada con exito"
            else:
                return "La tarea con el id ingresado no existe"

    def listar_todas_las_tareas_old(self, id):
        pass

    def Listar_todas_las_tareas_completadas_old(self):
        pass

    def Listar_todas_las_tareas_pendientes_old(self):
        pass

    def Listar_todas_las_tareas_en_progreso_old(self):
        pass

import os
import json


class JsonManager:
    def __init__(self):
        self.almacen_tareas = {}
        # Crear archivo si no existe

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
                        print(tarea)
                print(type(self.almacen_tareas))
                return self.almacen_tareas
            except json.JSONDecodeError:
                self.almacen_tareas = {}  # o [] si esperás una lista

    def escribir_archivo(self):
        with open("data.json", "w") as f:
            json.dump(self.almacen_tareas, f, indent=4)
            return "Tarea guardada en el archivo data.json"


if __name__ == '__main__':
    gestor = JsonManager()
    gestor.crear_archivo()

    # Escribir datos de prueba
    gestor.almacen_tareas = {
        "tareas": [
            {"id": 1, "titulo": "Aprender Python", "completada": False},
            {"id": 2, "titulo": "Crear proyecto", "completada": True}
        ]
    }
    gestor.escribir_archivo()

    # Ahora leer
    #gestor.leer_archivo()
    gestor.leer_archivo2()

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
        self.data_file = "data.json"
        # Aseguramos que el archivo exista al crear la instancia
        self.crear_archivo()


    def crear_archivo(self):
        # valida si el archivo data.json no existe, si no existe entra al if y crea el archivo
        if not os.path.exists(self.data_file):
            # crea el archivo data.json si no existe al cual llamamos f
            with open(self.data_file, "w", encoding="utf-8") as f:
                # crea un diccionario con la clave tareas y una lista vacia como valor, la f es el archivo abierto en modo escritura y se le escribe el diccionario el indent=4 es para que el json se vea ordenado y ensure_ascii=False es para que los caracteres especiales se guarden correctamente
                json.dump({"tareas": []}, f, indent=4, ensure_ascii=False)


    def leer_archivo(self):
        # Devuelve siempre un dict con la clave "tareas"
        if not os.path.exists(self.data_file):  # valida si el archivo data.json no existe
            # esto devuelve un diccionario con la clave tareas y una lista vacia como valor
            return {"tareas": []}
        with open(self.data_file, "r", encoding="utf-8") as f:  # si el archivo existe lo abre en modo lectura
            try:
                # el load es para cargar el contenido del archivo json en una variable de python
                datos = json.load(f)
                if "tareas" not in datos:  # valida si la clave tareas no existe en el diccionario datos
                    # si no existe la clave tareas en el diccionario datos, la crea y le asigna una lista vacia como valor
                    datos["tareas"] = []
                return datos  # si la clave tareas existe en el diccionario datos, devuelve el diccionario datos
            except json.JSONDecodeError:
                # Si el JSON está corrupto, devolvemos estructura vacía
                return {"tareas": []}


    def escribir_archivo(self):  # este metodo escribe en el archivo data.json el contenido de self.almacen_tareas
        # Método legacy: escribe `self.almacen_tareas` si quieres usarlo.
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.almacen_tareas, f, indent=4, ensure_ascii=False)
        return "Tarea guardada en el archivo data.json"


    # este metodo escribe en el archivo data.json los datos que se le pasan como parametro
    def escribir_archivo_datos(self, datos):
        # Helper preferido: escribe el dict `datos` directamente
        with open(self.data_file, "w", encoding="utf-8") as f:#abre el archivo data.json en modo escritura, que en codigo se llama self.data_file
            json.dump(datos, f, indent=4, ensure_ascii=False)#escribe el diccionario datos en el archivo data.json, el indent=4 es para que el json se vea ordenado y ensure_ascii=False es para que los caracteres especiales se guarden correctamente, dump sirve para escribir en un archivo json
        return "Datos guardados en data.json"


    def agregar(self, descripcion, estado):
        # Usamos los helpers centralizados
        datos = self.leer_archivo()  # datos es un diccionario con la clave tareas y una lista de tareas como valor, obtenidos del archivo data.json, llamando al metodo leer_archivo
        if "tareas" not in datos:  # valida si la clave tareas no existe en el diccionario datos
            datos["tareas"] = []# si no existe la clave tareas, la crea y le asigna una lista vacia como valor
        nuevo_id = max([tarea.get("id", 0) for tarea in datos["tareas"]], default=0) + 1# si no entra al if entonces Calcula el nuevo ID (soporta lista vacía), lo que quiere decir que si la lista de tareas esta vacia el nuevo id sera 1, si no esta vacia entonces busca el id mas grande y le suma 1 para obtener el nuevo id
        ahora = date.today()
        nueva_tarea = {
            "id": nuevo_id,
            "descripcion": descripcion,
            "estado": estado,
            "fecha de creacion": str(ahora),
            "fecha de actualizacion": str(ahora)
        }
        datos["tareas"].append(nueva_tarea)# agrega la nueva tarea al diccionario datos en la clave tareas que es una lista
        self.escribir_archivo_datos(datos)#envia el diccionario datos al metodo escribir_archivo_datos para que lo escriba en el archivo data.json, dicho metodo espera un diccionario como parametro
        self.id = nuevo_id + 1# Incrementa el id para la siguiente tarea
        # Guardamos el último id para compatibilidad
        self.ultimo_id = nuevo_id# Guardamos el último id para compatibilidad
        return f"Tarea '{descripcion}' agregada con exito. (ID: {nuevo_id})"


    def actualizar_estado(self, id, estado):
        datos = self.leer_archivo()# datos es un diccionario con la clave tareas y una lista de tareas como valor, obtenidos del archivo data.json, llamando del metodo leer_archivo
        if "tareas" in datos:#si la clave tareas existe en el diccionario datos 
            for tarea in datos["tareas"]:# recorre la lista de tareas que esta en la clave tareas del diccionario datos
                if tarea["id"] == int(id):# si el id en el diccionario es igual al id que envia el usuario
                    tarea["estado"] = estado # actualiza el estado de la tarea del id indicado 
                    tarea["fecha de actualizacion"] = str(date.today()) # actualiza la fecha del diccionario para la tarea del id indicada 
                    self.escribir_archivo_datos(datos) # se le envia datos al metodo escribir_archivo_datos para que lo escriba en el archivo data.json, datos ya lleva los datos actualizados
                    return "Tarea actualizada con exito"
        return "No existe tarea con ese id.!!"


    def eliminar(self, id):
        datos = self.leer_archivo()
        if "tareas" in datos:
            for i, tarea in enumerate(datos["tareas"]):
                if tarea["id"] == int(id):
                    del datos["tareas"][i]# elimina la tarea con el id indicado por el usuario
                    self.escribir_archivo_datos(datos)# escribe el data.json sin la tarea eliminada
                    return "Tarea eliminada con exito"
        return "La tarea con el id ingresado no existe"


    def listar_todas_las_tareas(self):
        datos = self.leer_archivo()
        if "tareas" in datos and len(datos["tareas"]) > 0:#valida si la clave tareas existe y valida si el tamaño de la lista dentro del diccionario es mayor a cero
            for diccionario in datos["tareas"]:# si entra en el if, recorre la lista del diccionario, por lo que cada diccionario dentro de la lista es una posicion
                for clave, valor in diccionario.items():#recorre los items de cada diccionario dentro de la lista e imprime su clave valor
                    print(f"{clave}: {valor}")
                print("-" * 10)
        else:
            print("No hay tareas disponibles")


    def Listar_todas_las_tareas_completadas(self):
        datos = self.leer_archivo()
        encontrado = False
        if "tareas" in datos:
            for diccionario in datos["tareas"]:# recorre la lista del diccionario, por lo que cada diccionario dentro de la lista es una posicion
                if diccionario.get("estado", "").lower() == "completada":# obtiene el valor de la clave estado del diccionario y lo compara en minusculas con la palabra completada
                    for clave, valor in diccionario.items():#recorre los items de cada diccionario dentro de la lista e imprime su clave valor
                        print(f"{clave}: {valor}")
                    print("-" * 10)
                    encontrado = True
        if not encontrado:
            print("No hay tareas completadas")


    def Listar_todas_las_tareas_pendientes(self):
        datos = self.leer_archivo()
        encontrado = False
        if "tareas" in datos:
            for diccionario in datos["tareas"]:# recorre la lista del diccionario, por lo que cada diccionario dentro de la lista es una posicion
                if diccionario.get("estado", "").lower() == "pendiente":# obtiene el valor de la clave estado del diccionario y lo compara en minusculas con la palabra pendiente
                    for clave, valor in diccionario.items():#recorre los items de cada diccionario dentro de la lista e imprime su clave valor
                        print(f"{clave}: {valor}")
                    print("-" * 10)
                    encontrado = True
        if not encontrado:
            print("No hay tareas pendientes")


    def Listar_todas_las_tareas_en_progreso(self):
        datos = self.leer_archivo()
        encontrado = False# se define la variable encontrado como False, para luego cambiar su valor a True si se encuentra al menos una tarea en progreso
        if "tareas" in datos:
            for diccionario in datos["tareas"]:# recorre la lista del diccionario, por lo que cada diccionario dentro de la lista es una posicion
                if diccionario.get("estado", "").lower() == "en progreso":# obtiene el valor de la clave estado del diccionario y lo compara en minusculas con la palabra en progreso
                    for clave, valor in diccionario.items():#recorre los items de cada diccionario dentro de la lista e imprime su clave valor
                        print(f"{clave}: {valor}")
                    print("-" * 10)
                    encontrado = True#cambia el valor de encontrado a True si encuentra al menos una tarea en progreso
        if not encontrado:
            print("No hay tareas en progreso")

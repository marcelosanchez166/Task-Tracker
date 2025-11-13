from TaskTracker import Task


class Menu:
    def __init__(self):
        self.tareas = Task()

    def main(self):
        while True:
            print('¡¡¡Bienvenido al menu de Task Tracker')
            print("Seleccione una opcion: ")
            print("1. Agregar tarea")
            print("2. Actualizar tarea")
            print("3. Eliminar tarea")
            print("4. Listar todas las tareas")
            print("5. Listar todas las tareas completadas")
            print("6. Listar todas las tareas pendientes")
            print("7. Listar todas las tareas en progreso")
            print("8. Salir")
            opcion = input("Ingrese el numero de la opcion deseada: ")
            if opcion == '1':
                print("\n")
                self.descripcion = input("Ingrese Una breve descripción de la tarea: ").lower()
                self.estado = input(
                    "El estado de la tarea (pendiente, en progreso, completada): ").lower()
                tarea_agregada = self.tareas.agregar(self.descripcion, self.estado)
                print(tarea_agregada)
            elif opcion == '2':
                self.id = input("Ingrese el id de la tarea a actualizar: ")
                self.estado = input(
                    "Ingrese el estado de la tarea (pendiente, en progreso, completada): ").lower()
                tarea_actualizada = self.tareas.actualizar_estado(self.id, self.estado)
                print(tarea_actualizada)
            elif opcion == '3':
                self.id = input("Ingrese el id de la tarea a eliminar: ")
                tarea_eliminada = self.tareas.eliminar(self.id)
                print(tarea_eliminada)
            elif opcion == '4':
                print("\n")
                tarea_actualizada = self.tareas.listar_todas_las_tareas()
                print("\n")
            elif opcion == '5':
                print("\n")
                tarea_completada = self.tareas.Listar_todas_las_tareas_completadas()
            elif opcion == '6':
                print("\n")
                tarea_pendiente = self.tareas.Listar_todas_las_tareas_pendientes()
            elif opcion == '7':
                print("\n")
                tarea_en_progreso = self.tareas.Listar_todas_las_tareas_en_progreso()
            elif opcion == '8':
                print("\n")
                print("Adios, Vuelve pronto.!!! ")
                break


if __name__ == '__main__':
    menu = Menu()
    menu.main()

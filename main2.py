from TaskTracker import Task
import sys


class Menu:
    def __init__(self):
        self.tareas = Task()

    def main(self):
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

        print("Comandos disponibles: \n"
              "n1 <descripcion> <estado> - Agregar tarea [pendiente, en progreso, completada] \n"
              "n2 <id> <estado> - Actualizar tarea\n"
              "n3 <id> - Eliminar tarea\n"
              "n4 - Listar todas las tareas\n"
              "n5 - Listar todas las tareas completadas\n"
              "n6 - Listar todas las tareas pendientes\n"
              "n7 - Listar todas las tareas en progreso\n"
              "n8 - Salir\n"
              "Ejemplo de uso: python tareas.py 1 'Comprar leche' pendiente")

        print("Ingrese el numero de la opcion deseada: ")
        # Validar que se haya pasado al menos una opción
        if len(sys.argv) < 2:
            sys.exit()
        opcion = sys.argv[1]

        if opcion == '1':
            if len(sys.argv) < 4:
                print("Error: Para agregar una tarea se necesita descripción y estado.")
                print("Ejemplo: python tareas.py 1 'Comprar leche' pendiente")
            else:
                self.descripcion = sys.argv[2]
                self.estado = sys.argv[3]
                tarea_agregada = self.tareas.agregar(self.descripcion, self.estado)
                print(tarea_agregada)

        elif opcion == '2':
            if len(sys.argv) < 4:
                print("Error: Para actualizar una tarea se necesita id y estado.")
                print("Ejemplo: python tareas.py 2 1 completada")
            else:
                self.id = sys.argv[2]
                self.estado = sys.argv[3]
                tarea_actualizada = self.tareas.actualizar_estado(self.id, self.estado)
                print(tarea_actualizada)

        elif opcion == '3':
            if len(sys.argv) < 3:
                print("Error: Para eliminar una tarea se necesita el id.")
                print("Ejemplo: python tareas.py 3 1")
            else:
                self.id = sys.argv[2]
                tarea_eliminada = self.tareas.eliminar(self.id)
                print(tarea_eliminada)

        elif opcion == '4':
            tarea_actualizada = self.tareas.listar_todas_las_tareas()

        elif opcion == '5':
            tarea_completada = self.tareas.Listar_todas_las_tareas_completadas()

        elif opcion == '6':
            tarea_pendiente = self.tareas.Listar_todas_las_tareas_pendientes()

        elif opcion == '7':
            tarea_en_progreso = self.tareas.Listar_todas_las_tareas_en_progreso()

        elif opcion == '8':
            print("Adios, Vuelve pronto.!!! ")
            sys.exit()


if __name__ == '__main__':
    menu = Menu()
    menu.main()

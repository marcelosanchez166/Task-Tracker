#!/usr/bin/env python
"""
CLI wrapper for TaskTracker.Task
Usage examples:
  python task_cli.py add "Buy groceries"
  python task_cli.py update 1 "New description"
  python task_cli.py delete 1
  python task_cli.py mark-in-progress 1
  python task_cli.py mark-done 1
  python task_cli.py list [status]
"""
import argparse
import json
import sys
from TaskTracker import Task

# Normalize status user input to stored strings
STATUS_MAP = {
    'done': 'completada',
    'completed': 'completada',
    'completada': 'completada',
    'todo': 'pendiente',
    'pending': 'pendiente',
    'pendiente': 'pendiente',
    'in-progress': 'en progreso',
    'in_progress': 'en progreso',
    'en-progreso': 'en progreso',
    'en progreso': 'en progreso',
    'en progreso': 'en progreso'
}

DATA_FILE = 'data.json'


def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8-sig') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'tareas': []}


def save_data(datos):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def cmd_add(args):
    t = Task()
    t.crear_archivo()
    # default estado 'pendiente'
    estado = args.status if args.status else 'pendiente'
    # use Task.agregar to add
    msg = t.agregar(args.description, estado)
    # read last task to get ID
    datos = load_data()
    if datos.get('tareas'):
        last = max(datos['tareas'], key=lambda x: x['id'])
        print(f"Task added successfully (ID: {last['id']})")
    else:
        print(msg)


def cmd_update(args):
    datos = load_data()
    for tarea in datos.get('tareas', []):
        if tarea['id'] == int(args.id):
            tarea['descripcion'] = args.description
            tarea['fecha de actualizacion'] = str(Task().fecha_de_ultima_actualización)
            save_data(datos)
            print('Task updated successfully')
            return
    print('Task id not found')


def cmd_delete(args):
    t = Task()
    res = t.eliminar(args.id)
    print(res)


def cmd_mark_in_progress(args):
    t = Task()
    res = t.actualizar_estado(args.id, 'en progreso')
    print(res)


def cmd_mark_done(args):
    t = Task()
    res = t.actualizar_estado(args.id, 'completada')
    print(res)


def cmd_list(args):
    datos = load_data()
    tasks = datos.get('tareas', [])
    if args.status:
        key = args.status.lower()
        mapped = STATUS_MAP.get(key, None)
        if not mapped:
            print('Status desconocido. Usa: done, todo, in-progress')
            return
        tasks = [t for t in tasks if t.get('estado', '').lower() == mapped]

    if not tasks:
        print('No hay tareas para mostrar')
        return

    for t in tasks:
        print(f"ID: {t.get('id')}")
        print(f"Descripcion: {t.get('descripcion')}")
        print(f"Estado: {t.get('estado')}")
        print(f"Creada: {t.get('fecha de creacion')}")
        print(f"Actualizada: {t.get('fecha de actualizacion')}")
        print('-' * 20)


def main():
    parser = argparse.ArgumentParser(prog='task-cli', description='Task tracker CLI')
    sub = parser.add_subparsers(dest='cmd')

    p_add = sub.add_parser('add', help='Add a new task')
    p_add.add_argument('description', help='Task description')
    p_add.add_argument('--status', '-s', help='Initial status (optional)')
    p_add.set_defaults(func=cmd_add)

    p_update = sub.add_parser('update', help='Update task description')
    p_update.add_argument('id', help='Task id')
    p_update.add_argument('description', help='New description')
    p_update.set_defaults(func=cmd_update)

    p_delete = sub.add_parser('delete', help='Delete a task')
    p_delete.add_argument('id', help='Task id')
    p_delete.set_defaults(func=cmd_delete)

    p_mip = sub.add_parser('mark-in-progress', help='Mark task as in progress')
    p_mip.add_argument('id', help='Task id')
    p_mip.set_defaults(func=cmd_mark_in_progress)

    p_done = sub.add_parser('mark-done', help='Mark task as done')
    p_done.add_argument('id', help='Task id')
    p_done.set_defaults(func=cmd_mark_done)

    p_list = sub.add_parser('list', help='List tasks (optionally by status)')
    p_list.add_argument('status', nargs='?', help='Optional status: done, todo, in-progress')
    p_list.set_defaults(func=cmd_list)

    args = parser.parse_args()
    if not getattr(args, 'func', None):
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == '__main__':
    main()

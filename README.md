# Task Tracker - Gestor de Tareas

Un gestor de tareas simple pero potente que te permite crear, actualizar, eliminar y gestionar tus tareas desde la línea de comandos.

## 📋 Descripción

Task Tracker es una aplicación CLI (Command Line Interface) que almacena tus tareas en un archivo JSON (`data.json`). Proporciona dos formas de interactuar con tus tareas:

1. **Menú tradicional** (`main2.py`) - Menú interactivo numérico (recomendado)

## 🚀 Instalación

### Requisitos
- Python 3.6 o superior
- No hay dependencias externas

### Configuración
1. Descarga o clona el proyecto
2. Navega a la carpeta del proyecto:
   ```bash
   cd tu_ruta_al_proyecto
   ```
3. El archivo `data.json` se creará automáticamente al ejecutar por primera vez

## 📖 Uso

### Opción 1: Menú Tradicional (main2.py) - Recomendado

Usa `main2.py` para un menú interactivo numérico:

#### Agregar una tarea
```bash
python main2.py 1 "Descripción de la tarea" "pendiente"
# Estados válidos: pendiente, en progreso, completada
```

#### Actualizar estado de una tarea
```bash
python main2.py 2 1 "en progreso"
# Formato: python main2.py 2 <id_tarea> <nuevo_estado>
```

#### Eliminar una tarea
```bash
python main2.py 3 1
# Formato: python main2.py 3 <id_tarea>
```

#### Listar todas las tareas
```bash
python main2.py 4
```

#### Listar tareas completadas
```bash
python main2.py 5
```

#### Listar tareas pendientes
```bash
python main2.py 6
```

#### Listar tareas en progreso
```bash
python main2.py 7
```

#### Salir
```bash
python main2.py 8
```


## 📁 Estructura de Archivos

```
Project_Task_tracker/
├── TaskTracker.py        # Clase principal que gestiona las tareas
├── main2.py             # Interfaz menú tradicional
├── data.json            # Almacenamiento de tareas (se crea automáticamente)
└── README.md            # Este archivo
```

## 🔧 Estructura de Datos

Las tareas se almacenan en formato JSON en `data.json`:

```json
{
    "tareas": [
        {
            "id": 1,
            "descripcion": "Comprar groceries",
            "estado": "pendiente",
            "fecha de creacion": "2025-11-13",
            "fecha de actualizacion": "2025-11-13"
        },
        {
            "id": 2,
            "descripcion": "Aprender Python",
            "estado": "en progreso",
            "fecha de creacion": "2025-11-13",
            "fecha de actualizacion": "2025-11-13"
        }
    ]
}
```

### Estados disponibles:
- **pendiente** - Tarea no iniciada
- **en progreso** - Tarea siendo realizada
- **completada** - Tarea finalizada

## 📚 Clases y Métodos

### Clase `Task` (TaskTracker.py)

#### `__init__()`
Inicializa una instancia de Task con variables de control.

#### `crear_archivo()`
Crea el archivo `data.json` si no existe.

#### `agregar(descripcion, estado)`
Agrega una nueva tarea con ID automático.
- **Parámetros:** `descripcion` (str), `estado` (str)
- **Retorna:** Mensaje de confirmación con el ID

#### `actualizar_estado(id, estado)`
Actualiza el estado de una tarea existente.
- **Parámetros:** `id` (int), `estado` (str)
- **Retorna:** Mensaje de confirmación o error

#### `eliminar(id)`
Elimina una tarea por su ID.
- **Parámetros:** `id` (int)
- **Retorna:** Mensaje de confirmación o error

#### `listar_todas_las_tareas()`
Muestra todas las tareas sin filtros.

#### `Listar_todas_las_tareas_completadas()`
Muestra solo las tareas con estado "completada".

#### `Listar_todas_las_tareas_pendientes()`
Muestra solo las tareas con estado "pendiente".

#### `Listar_todas_las_tareas_en_progreso()`
Muestra solo las tareas con estado "en progreso".

## 💡 Ejemplos Prácticos

### Flujo completo con main2.py:

```bash
# 1. Agregar dos tareas
python main2.py 1 "Estudiar Python" "pendiente"
python main2.py 1 "Hacer ejercicio" "pendiente"

# 2. Actualizar estado a en progreso
python main2.py 2 1 "en progreso"

# 3. Listar todas las tareas
python main2.py 4

# 4. Listar solo tareas pendientes
python main2.py 6

# 5. Marcar como completada
python main2.py 2 1 "completada"

# 6. Listar tareas completadas
python main2.py 5

# 7. Eliminar tarea
python main2.py 3 1
```



## 🎯 Características

✅ **Gestión completa de tareas** - Crear, leer, actualizar y eliminar  
✅ **Almacenamiento persistente** - Datos guardados en JSON  
✅ **Filtrado por estado** - Listar tareas por su estado  
✅ **IDs automáticos** - No es necesario especificar IDs manualmente  
✅ **Registro de fechas** - Seguimiento de cuándo se crean y actualizan  
✅ **Interfaz moderna y tradicional** - Elige tu forma preferida  
✅ **Sin dependencias externas** - Solo Python estándar  

## ⚙️ Notas Técnicas

- Los IDs se generan automáticamente basándose en el ID máximo actual + 1
- Las fechas se registran automáticamente en formato ISO (YYYY-MM-DD)
- El archivo `data.json` se crea automáticamente al ejecutar por primera vez
- Los cambios se guardan inmediatamente en `data.json`
- La comparación de estados es insensible a mayúsculas (case-insensitive)


## 📝 Licencia

Libre para usar y modificar.

## 🤝 Contribuciones

¿Ideas para mejorar? ¡Siéntete libre de modificar y adaptar el código!

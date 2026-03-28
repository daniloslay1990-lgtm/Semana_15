class Tarea:
    # Modelo de datos de una tarea
    # Representa la estructura de cada tarea en el sistema

    def __init__(self, id: int, descripcion: str):
        self.id = id
        self.descripcion = descripcion  # usa setter
        self.completada = False  # estado inicial

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        # Validación: no permitir tareas vacías
        if not value or not value.strip():
            raise ValueError("La tarea no puede estar vacía")
        self._descripcion = value.strip()

    def marcar_completada(self):
        
        # Cambia el estado de la tarea a completada
        
        self.completada = True
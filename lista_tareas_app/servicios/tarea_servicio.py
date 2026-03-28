from modelos.tarea import Tarea


class TareaServicio:
    """
    Capa de lógica de negocio (CRUD de tareas)
    """

    def __init__(self):
        self._tareas = []  # lista en memoria
        self._contador = 1  # id automático

    def agregar_tarea(self, descripcion):
        """
        Crea una nueva tarea
        """
        tarea = Tarea(self._contador, descripcion)
        self._tareas.append(tarea)
        self._contador += 1

    def obtener_todas(self):
        """
        Retorna todas las tareas
        """
        return self._tareas

    def completar_tarea(self, id):
        """
        Marca una tarea como completada
        """
        tarea = self._buscar(id)
        if tarea:
            tarea.marcar_completada()
        else:
            raise ValueError("Tarea no encontrada")

    def eliminar_tarea(self, id):
        """
        Elimina una tarea por ID
        """
        tarea = self._buscar(id)
        if tarea:
            self._tareas.remove(tarea)
        else:
            raise ValueError("Tarea no encontrada")

    def _buscar(self, id):
        """
        Método privado para buscar tarea
        """
        for t in self._tareas:
            if t.id == id:
                return t
        return None
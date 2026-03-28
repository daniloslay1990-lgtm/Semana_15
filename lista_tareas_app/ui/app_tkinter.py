import tkinter as tk
from tkinter import ttk, messagebox


class AppTareas(tk.Tk):
    """
    Interfaz principal (UI)
    Maneja eventos de usuario y visualización
    """

    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio

        self.title("Lista de Tareas")
        self.geometry("820x520")
        self.configure(bg="#f4f4f9")

        self._estilos()
        self._ui()
        self._eventos()

    # ================= ESTILOS =================
    def _estilos(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        # Estilo de tabla
        style.configure("Treeview", background="#ffffff", rowheight=25)
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        # Estilo de botones
        style.configure("Agregar.TButton", background="#4CAF50", foreground="white")
        style.configure("Completar.TButton", background="#2196F3", foreground="white")
        style.configure("Eliminar.TButton", background="#f44336", foreground="white")

    # ================= UI =================
    def _ui(self):

        # Campo de entrada
        frame = tk.Frame(self, bg="#f4f4f9")
        frame.pack(pady=10)

        tk.Label(frame, text="Nueva tarea:", bg="#f4f4f9").grid(row=0, column=0)

        self.entry = ttk.Entry(frame, width=50)
        self.entry.grid(row=0, column=1, padx=10)

        # Mensaje de estado
        self.lbl_estado = tk.Label(
            self,
            text="Enter=Agregar | Doble clic=Completar | Delete=Eliminar",
            bg="#f4f4f9",
            fg="#1d3b6b"
        )
        self.lbl_estado.pack(fill="x", padx=20)

        # Botones
        frame_btn = tk.Frame(self, bg="#f4f4f9")
        frame_btn.pack(pady=5)

        ttk.Button(frame_btn, text="Añadir Tarea",
                   style="Agregar.TButton",
                   command=self._agregar).pack(side="left", padx=5)

        ttk.Button(frame_btn, text="Marcar Completada",
                   style="Completar.TButton",
                   command=self._completar).pack(side="left", padx=5)

        ttk.Button(frame_btn, text="Eliminar",
                   style="Eliminar.TButton",
                   command=self._eliminar).pack(side="left", padx=5)

        # Tabla
        self.tabla = ttk.Treeview(self, columns=("id", "desc"), show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("desc", text="Descripción")
        self.tabla.pack(fill="both", expand=True)

    # ================= EVENTOS =================
    def _eventos(self):
        # Evento teclado ENTER
        self.entry.bind("<Return>", self._evento_enter)

        # Evento doble clic en tabla
        self.tabla.bind("<Double-1>", self._evento_doble_click)

        # Evento tecla DELETE
        self.tabla.bind("<Delete>", self._evento_delete)

        # Evento cerrar ventana
        self.protocol("WM_DELETE_WINDOW", self._cerrar)

    def _evento_enter(self, e):
        """Agregar tarea con ENTER"""
        self.lbl_estado.config(text="Enter → tarea agregada")
        self._agregar()

    def _evento_doble_click(self, e):
        """Completar tarea con doble clic"""
        self.lbl_estado.config(text="Doble clic → tarea completada")
        self._completar()

    def _evento_delete(self, e):
        """Eliminar tarea con tecla DELETE"""
        self.lbl_estado.config(text="Delete → tarea eliminada")
        self._eliminar()

    # ================= FUNCIONES =================

    def _agregar(self):
        try:
            self.servicio.agregar_tarea(self.entry.get())
            self._actualizar()
            self.entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _completar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            return

        id_tarea = self.tabla.item(seleccion[0])["values"][0]
        self.servicio.completar_tarea(id_tarea)
        self._actualizar()

    def _eliminar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            return

        id_tarea = self.tabla.item(seleccion[0])["values"][0]

        # Confirmación antes de eliminar
        confirmar = messagebox.askyesno(
            "Confirmar",
            "¿Seguro que desea eliminar la tarea?"
        )

        if confirmar:
            self.servicio.eliminar_tarea(id_tarea)
            self._actualizar()

    def _actualizar(self):
        # Limpiar tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Insertar tareas actualizadas
        for t in self.servicio.obtener_todas():

            texto = t.descripcion

            # Feedback visual
            if t.completada:
                texto = "[✔] " + texto

            self.tabla.insert("", tk.END, values=(t.id, texto))

    def _cerrar(self):
        """
        Confirmación al cerrar la app
        """
        if messagebox.askyesno("Salir", "¿Está seguro de cerrar?"):
            self.destroy()
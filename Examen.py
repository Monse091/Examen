import tkinter as tk
from tkinter import simpledialog

class Paciente:
    def __init__(self, nombre, edad, genero, telefono, diagnostico):
        self.id = None
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.telefono = telefono
        self.diagnostico = diagnostico

class RegistroDPacientes:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, paciente):
        paciente.id = len(self.pacientes) + 1
        self.pacientes.append(paciente)

    def buscar_pacienteNombre(self, nombre_busqueda):
        for paciente in self.pacientes:
            if paciente.nombre == nombre_busqueda:
                return paciente
        return None
    
    def buscar_pacienteDiagnostico(self, diagnostico_busqueda):
        for paciente in self.pacientes:
            if paciente.diagnostico == diagnostico_busqueda:
                return paciente
        return None

    def eliminar_paciente(self, id_eliminar):
        for paciente in self.pacientes:
            if paciente.id == id_eliminar:
                self.pacientes.remove(paciente)
                return True
        return False

    def editar_paciente(self, id_editar, nueva_edad, nuevo_telefono, nuevo_diagnostico):
        paciente = self.buscar_paciente(id_editar)
        if paciente:
            paciente.edad = nueva_edad
            paciente.telefono = nuevo_telefono
            paciente.diagnostico = nuevo_diagnostico
            return True
        return False

class InterfazTkinter:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registro de Pacientes")

        self.registro = RegistroDPacientes()

        self.crear_botones()
        self.crear_resultados()

    def crear_botones(self):
        btn_crear = tk.Button(self.ventana, text="Crear Paciente", command=self.crear_paciente)
        btn_buscarNombre = tk.Button(self.ventana, text="Buscar Paciente por nombre", command=self.buscar_pacientenombre)
        btn_buscarDiagnostico = tk.Button(self.ventana, text="Buscar Paciente por diagnostico", command=self.buscar_pacientediagnostico)
        btn_administrar = tk.Button(self.ventana, text="Administrar Pacientes", command=self.administrar_pacientes)

        btn_crear.pack()
        btn_buscarNombre.pack()
        btn_buscarDiagnostico.pack()
        btn_administrar.pack()

    def crear_resultados(self):
        self.resultados = tk.Text(self.ventana, height=10, width=40)
        self.resultados.pack()

    def crear_paciente(self):
        nombre = simpledialog.askstring("Crear Paciente", "Nombre:")
        edad = simpledialog.askinteger("Crear Paciente", "Edad:")
        genero = simpledialog.askstring("Crear Paciente", "Género:")
        telefono = simpledialog.askstring("Crear Paciente", "Teléfono:")
        diagnostico = simpledialog.askstring("Crear Paciente", "Diagnóstico:")

        paciente = Paciente(nombre, edad, genero, telefono, diagnostico)
        self.registro.agregar_paciente(paciente)
        self.resultados.insert(tk.END, f"Paciente registrado con ID: {paciente.id}\n")

    def buscar_pacientenombre(self):
        Nombre_busqueda = simpledialog.askstring("Buscar Paciente", "Nombre del Paciente:")
        paciente = self.registro.buscar_pacienteNombre(Nombre_busqueda)
        if paciente:
            self.mostrar_info_paciente(paciente)
        else:
            self.resultados.insert(tk.END, "Paciente no encontrado\n")

    def buscar_pacientediagnostico(self):
        diagnostico_busqueda = simpledialog.askstring("Buscar Paciente", "diagnostico del Paciente:")
        paciente = self.registro.buscar_pacienteDiagnostico(diagnostico_busqueda)
        if paciente:
            self.mostrar_info_paciente(paciente)
        else:
            self.resultados.insert(tk.END, "Paciente no encontrado\n")

    def administrar_pacientes(self):
        id_opcion = simpledialog.askinteger("Administrar Pacientes", "1. Eliminar Paciente\n2. Editar Paciente\nOpción:")
        if id_opcion == 1:
            id_eliminar = simpledialog.askinteger("Eliminar Paciente", "ID del Paciente a eliminar:")
            if self.registro.eliminar_paciente(id_eliminar):
                self.resultados.insert(tk.END, "Paciente eliminado con éxito\n")
            else:
                self.resultados.insert(tk.END, "El Paciente no fue encontrado\n")
        elif id_opcion == 2:
            id_editar = simpledialog.askinteger("Editar Paciente", "ID del Paciente a editar:")
            paciente = self.registro.buscar_paciente(id_editar)
            if paciente:
                nueva_edad = simpledialog.askinteger("Editar Paciente", f"Edad actual: {paciente.edad}\nNueva Edad:")
                nuevo_telefono = simpledialog.askstring("Editar Paciente", f"Teléfono actual: {paciente.telefono}\nNuevo Teléfono:")
                nuevo_diagnostico = simpledialog.askstring("Editar Paciente", f"Diagnóstico actual: {paciente.diagnostico}\nNuevo Diagnóstico:")
                if self.registro.editar_paciente(id_editar, nueva_edad, nuevo_telefono, nuevo_diagnostico):
                    self.resultados.insert(tk.END, "Cambios guardados con éxito\n")
                else:
                    self.resultados.insert(tk.END, "Error al editar el paciente\n")
            else:
                self.resultados.insert(tk.END, "Paciente no encontrado\n")

    def mostrar_info_paciente(self, paciente):
        info = f"ID: {paciente.id}\nNombre: {paciente.nombre}\nEdad: {paciente.edad}\nGénero: {paciente.genero}\nTeléfono: {paciente.telefono}\nDiagnóstico: {paciente.diagnostico}\n"
        self.resultados.insert(tk.END, info)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazTkinter(ventana)
    ventana.mainloop()
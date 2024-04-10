import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import win32event
import win32api
import winerror
import sys
from GraficasTk.CrearAlumnoTk import CrearAlumnoTk
from GraficasTk.ModAlumnoTk import ModAlumnoTk
from GraficasTk.Materia_AlumnoTk import Materia_AlumnoTk
from GraficasTk.MateriaTk import MateriaTk
from GraficasTk.CrearProfesorTk import CrearProfesorTk
from GraficasTk.ModProfesorTk import ModProfesorTk
from GraficasTk.Materia_ProfesorTk import Materia_ProfesorTk
from db.DataBase import DataBase

class Aplicacion(CrearAlumnoTk,ModAlumnoTk,Materia_AlumnoTk,CrearProfesorTk,ModProfesorTk,Materia_ProfesorTk,MateriaTk):

    def __init__(self):
        if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
            print("Ya hay una instancia de la aplicación en ejecución.")
            sys.exit()
        try:
            # Intenta conectar con el servidor usando las credenciales del usuario EtecUser
            database = DataBase("localhost", "root", "tkinterdatabase", "1234")
        except ConnectionError as e:
    # Si ocurre algún error durante la conexión o la creación de la base de datos y el usuario, muestra un mensaje de error
            messagebox.showerror("Error de conexión con el servidor", str(e))
            return
        self.event_name = "ETEC"
        self.event_handle = win32event.CreateEvent(None, 0, 0, self.event_name)
        
        # Verifica si ya existe una instancia en ejecución
        
        self.ventana1 = tk.Tk()
        self.__initialize_custom_style()
        self.ventana1.title("ETEC")
        self.ventana1.config(bg="#FFFFFF")
        self.ventana1.geometry('925x500+300+200')
        self.ventana1.resizable(0,0)
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self.ventana1)
        self.notebook.config(height=500,width=925)
        self.notebook["style"] = "CustomNotebook"
        self.notebook.bind("<ButtonPress-1>", self.on_close_press, True)
        self.notebook.bind("<ButtonRelease-1>", self.on_close_release)
        self.frameInicio = tk.Frame(self.notebook,bg="#FFF")
        self.VentanaInicio(self.frameInicio)
        self.frameCargarAlumno = tk.Frame(self.notebook,bg="#FFF")
        self.MasterCargarAlumno(self.frameCargarAlumno)
        self.frameBMAlumno = tk.Frame(self.notebook,bg="#FFF")
        self.MasterBMAlumno(self.frameBMAlumno)
        self.frameMateria_Alumno = tk.Frame(self.notebook,bg="#FFF")
        self.MasterMateria_Alumno(self.frameMateria_Alumno)
        self.frameCargarProfesor = tk.Frame(self.notebook,bg="#FFF")
        self.MasterCargarProfesor(self.frameCargarProfesor)
        self.frameBMProfesor = tk.Frame(self.notebook,bg="#FFF")
        self.MasterBMProfesor(self.frameBMProfesor)
        self.frameMateria_Profesor = tk.Frame(self.notebook,bg="#FFF")
        self.MasterMateria_Profesor(self.frameMateria_Profesor)
        self.frameCargarMateria = tk.Frame(self.notebook,bg="#FFF")
        self.MasterCargarMateria(self.frameCargarMateria)
        self.frameBMMateria = tk.Frame(self.notebook,bg="#FFF")
        self.MasterBMMateria(self.frameBMMateria)
        # Añadirlas al panel con su respectivo texto.

        self.notebook.add(self.frameInicio,text="Inicio",padding=20)
        self.notebook.add(self.frameCargarAlumno, text="Cargar Alumno", padding=20)
        self.notebook.add(self.frameBMAlumno, text="Guardar Alumno", padding=20)
        self.notebook.add(self.frameMateria_Alumno,text="Agregar Materia a Alumno",padding=20)
        self.notebook.add(self.frameCargarProfesor, text="Cargar Profesor", padding=20)
        self.notebook.add(self.frameBMProfesor, text="Guardar Profesor", padding=20)
        self.notebook.add(self.frameMateria_Profesor,text="Agregar Materia a Profesor",padding=20)
        self.notebook.add(self.frameCargarMateria, text="Cargar Materia",padding=20)
        self.notebook.add(self.frameBMMateria, text="Guardar Materia",padding=20)

        # Ocultar las ventanas.
        self.notebook.hide(self.frameCargarAlumno)
        self.notebook.hide(self.frameBMAlumno)
        self.notebook.hide(self.frameMateria_Alumno)
        self.notebook.hide(self.frameCargarProfesor)
        self.notebook.hide(self.frameBMProfesor)
        self.notebook.hide(self.frameMateria_Profesor)
        self.notebook.hide(self.frameCargarMateria)
        self.notebook.hide(self.frameBMMateria)
        self.notebook.pack(padx=10, pady=10)
        
        self.ventana1.mainloop()
   
    
#<-------------------------------------Estilos de la App------------------------------------------------------> 
    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            #cruz blanca
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            #cruz amarilla
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            #cruz roja
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                })
            ]
        })
    ])  

    def on_close_release(self, event):
        """Called when the button is released"""
        if not self.notebook.instate(['pressed']):
            return

        element =  self.notebook.identify(event.x, event.y)
        print(element)
        if "close" not in element:
            # si el usuario mueve el mouse fuera de la cruz
            return

        index = self.notebook.index("@%d,%d" % (event.x, event.y))

        if self.notebook._active == index:
            if index == 0:
                return
            else:
                self.notebook.hide(index)
                print(index)
                self.notebook.event_generate("<<NotebookTabClosed>>")
                self.notebook.state(["!pressed"])
                self.notebook._active = None
        
    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.notebook.identify(event.x, event.y)
        print(element)

        if "close" in element:
            index = self.notebook.index("@%d,%d" % (event.x, event.y))
            self.notebook.state(['pressed'])
            self.notebook._active = index
            return "break"


#<---------------------------------------VENTANA DE INICIO------------------------------------------------------->
    #Abre las otras ventanas
    def VentanaInicio(self,masterCarga):
        def abrirVentana(frame):
            self.notebook.hide(frame)
            self.notebook.add(frame)
            self.notebook.select(frame)
            self.cargar_listaprofesores()
            self.cargar_comboxmateriasProfesores()
            self.cargar_listboxprofesores()
            self.cargar_listalumnos()
            self.cargar_comboxmaterias()
            self.cargar_listboxalumnos()
            self.cargar_listamaterias()

        self.tituloVentanaInicio=tk.Label(masterCarga,text="Inicio")
        self.tituloVentanaInicio.config(bg="#FFF", font=("Arial", 20))
        self.tituloVentanaInicio.place(x=400,y=10)
        self.imagenAlumno = tk.PhotoImage(file="imagenesApp/user-graduateprueba3.png")
        self.menuAlumno = tk.Menubutton(masterCarga,image=self.imagenAlumno, bg='#FFF', fg='white', border=0, cursor='hand2',direction="right")
        self.menuAlumno.menu=tk.Menu(self.menuAlumno,tearoff=0)
        self.menuAlumno['menu']=self.menuAlumno.menu
        self.menuAlumno.menu.add_command(label="Crear Alumno",command=lambda:abrirVentana(self.frameCargarAlumno))
        self.menuAlumno.menu.add_command(label="Modificar Alumno",command=lambda:abrirVentana(self.frameBMAlumno))
        self.menuAlumno.menu.add_command(label="Agregar Materia",command=lambda:abrirVentana(self.frameMateria_Alumno))
        self.menuAlumno.place(x=30,y=150)
        self.alumnoLabel = tk.Label(masterCarga,text="Alumno")
        self.alumnoLabel.config(bg="#FFF", font=("Arial", 15))
        self.alumnoLabel.place(x=90,y=90)
        tk.Frame(masterCarga, width=200, height=1.5, bg='#8CD0F7').place(x=32, y=120)
        self.imagenProfesor = tk.PhotoImage(file="imagenesApp/user-tie2.png")
        self.menuProfesor = tk.Menubutton(masterCarga,image=self.imagenProfesor, bg='#FFF', fg='white', border=0, cursor='hand2',direction="right")
        self.menuProfesor.menu=tk.Menu(self.menuProfesor,tearoff=0)
        self.menuProfesor['menu']=self.menuProfesor.menu
        self.menuProfesor.menu.add_command(label="Crear Docente",command=lambda:abrirVentana(self.frameCargarProfesor))
        self.menuProfesor.menu.add_command(label="Modificar Docente",command=lambda:abrirVentana(self.frameBMProfesor))
        self.menuProfesor.menu.add_command(label="Agregar Materia",command=lambda:abrirVentana(self.frameMateria_Profesor))
        self.menuProfesor.place(x=310,y=150)
        self.profesorLabel = tk.Label(masterCarga,text="Profesor")
        self.profesorLabel.config(bg="#FFF", font=("Arial", 15))
        self.profesorLabel.place(x=367,y=90)
        tk.Frame(masterCarga, width=200, height=1.5, bg='#8CD0F7').place(x=314, y=120)
        self.imagenMateria = tk.PhotoImage(file="imagenesApp/bookprueba.png")
        self.menuMateria = tk.Menubutton(masterCarga,image=self.imagenMateria, bg='#FFF', fg='white', border=0, cursor='hand2',direction="right")
        self.menuMateria.menu=tk.Menu(self.menuMateria,tearoff=0)
        self.menuMateria['menu']=self.menuMateria.menu
        self.menuMateria.menu.add_command(label="Crear Materia",command=lambda:abrirVentana(self.frameCargarMateria))
        self.menuMateria.menu.add_command(label="Modificar Materia",command=lambda:abrirVentana(self.frameBMMateria))
        self.menuMateria.place(x=590,y=150)
        self.materiaLabel = tk.Label(masterCarga,text="Materia")
        self.materiaLabel.config(bg="#FFF", font=("Arial", 15))
        self.materiaLabel.place(x=652,y=90)
        tk.Frame(masterCarga, width=200, height=1.5, bg='#8CD0F7').place(x=594, y=120)


if __name__ == '__main__':
    aplicacion1 = Aplicacion()
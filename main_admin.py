import tkinter as tk
from tkinter import ttk
from GraficasTk.AlumnoTk import AlumnoTk
from GraficasTk.MateriaTk import MateriaTk
from GraficasTk.ProfesorTk import ProfesorTk

class ConsultaAlumnos(AlumnoTk,ProfesorTk,MateriaTk):
    #Ejemplos de nombres para los alumnos 
    lista = []
    # lista.append( Alumno("0", "Luciano González", "tarde") )
    # lista.append( Alumno("1", "Juan Jose", "manana") )
    # lista.append( Alumno("2", "Samantha Delgado", "tarde") )
    # lista.append( Alumno("3", "Alex Granado", "manana") )
    # lista.append( Alumno("4", "Michelle Ramirez", "tarde") )
    # lista.append( Alumno("5", "Natalia Alonso", "manana") )
    # lista.append( Alumno("6", "Anthony Soto", "tarde") )
    # lista.append( Alumno("7", "Fernando Domínquez", "manana") )
    # lista.append( Alumno("8", "María Paula Jasso", "tarde") )
    # lista.append( Alumno("9", "Paz Gómez", "manana") )
    # lista.append( Alumno("10", "Magdalena Garrido", "tarde") )
    # lista.append( Alumno("11", "Maximiliano Crespo", "manana") )

    def __init__(self):
        
        self.ventana1 = tk.Tk()
        self.estilos()
        self.ventana1.title("Colegio Atid")
        self.ventana1.config(bg="#FFFFFF")
        self.ventana1.geometry('925x500+300+200')
        # self.ventana1.iconphoto(True, tk.PhotoImage(file='C:/Users/SEVN/Desktop/Aplicacion Edutec/logo.png'))
        self.ventana1.resizable(0,0)
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self.ventana1)
        self.notebook.config(height=500,width=925)
        self.frameInicio = tk.Frame(self.notebook,bg="#FFF")
        self.VentanaInicio(self.frameInicio)
        self.frameCargarAlumno = tk.Frame(self.notebook,bg="#FFF")
        self.MasterCargarAlumno(self.frameCargarAlumno)
        self.frameBMAlumno = tk.Frame(self.notebook,bg="#FFF")
        self.MasterBMAlumno(self.frameBMAlumno)
        self.frameCargarProfesor = tk.Frame(self.notebook,bg="#FFF")
        self.MasterCargarProfesor(self.frameCargarProfesor)
        self.frameBMProfesor = tk.Frame(self.notebook,bg="#FFF")
        self.MasterBMProfesor(self.frameBMProfesor)
        self.frameCargarMateria = tk.Frame(self.notebook,bg="#FFF")
        self.MasterCargarMateria(self.frameCargarMateria)
        self.frameBMMateria = tk.Frame(self.notebook,bg="#FFF")
        self.MasterBMMateria(self.frameBMMateria)
        # Añadirlas al panel con su respectivo texto.

        self.notebook.add(self.frameInicio,text="Inicio",padding=20)
        self.notebook.add(self.frameCargarAlumno, text="Cargar Alumno", padding=20)
        self.notebook.add(self.frameBMAlumno, text="Guardar Alumno", padding=20)
        self.notebook.add(self.frameCargarProfesor, text="Cargar Profesor", padding=20)
        self.notebook.add(self.frameBMProfesor, text="Guardar Profesor", padding=20)
        self.notebook.add(self.frameCargarMateria, text="Cargar Materia",padding=20)
        self.notebook.add(self.frameBMMateria, text="Guardar Materia",padding=20)

        # Ocultar las ventanas.
        self.notebook.hide(self.frameCargarAlumno)
        self.notebook.hide(self.frameBMAlumno)
        self.notebook.hide(self.frameCargarProfesor)
        self.notebook.hide(self.frameBMProfesor)
        self.notebook.hide(self.frameCargarMateria)
        self.notebook.hide(self.frameBMMateria)
        self.notebook.pack(padx=10, pady=10)
        
        self.ventana1.mainloop()
   
    
#<-------------------------------------Estilos de la App------------------------------------------------------> 
    def estilos(self):   
        self.style = ttk.Style()
        self.style.theme_create ("estilo_tb",parent="clam",settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0],"background": "#FFFFFF"} },
            "TNotebook.Tab": {
                "configure": {"padding": [5, 1], "background": "#FFFFFF" },
                "map":       {"background": [("selected", "#8CD0F7"),("active","#8CD0F7")],#A7E1F1
                            "expand": [("selected", [2, 2, 2, 0])] } }, 
            "TButton": {
                "map":       {"background": [("active", "#8CD0F7"),("pressed","#8CD0F7")]}}})
                

        self.style.theme_use("estilo_tb")
      


#<---------------------------------------VENTANA DE INICIO------------------------------------------------------->
    def VentanaInicio(self,masterCarga):
        #Funcion para que aparesca la ventana cargar profesor 
        def abrirVentanaProfesor():
            self.notebook.hide(self.frameCargarProfesor)
            self.notebook.add(self.frameCargarProfesor)
            self.notebook.select(self.frameCargarProfesor)

        def abrirVentanaBMProfesor():
            self.notebook.hide(self.frameBMProfesor)
            self.notebook.add(self.frameBMProfesor)
            self.notebook.select(self.frameBMProfesor)
            self.cargar_listaprofesores()
        #Funcion para que aparesca la ventana cargar alumno 
        def abrirVentanaAlumno():
            self.notebook.hide(self.frameCargarAlumno)
            self.notebook.add(self.frameCargarAlumno)
            self.notebook.select(self.frameCargarAlumno)
        
        def abrirVentanaBMAlumno():
            self.notebook.hide(self.frameBMAlumno)
            self.notebook.add(self.frameBMAlumno)
            self.notebook.select(self.frameBMAlumno)
            self.cargar_listalumnos()
        #Funcion para que aparesca la ventana cargar materia 
        def abrirVentanaMateria():
            self.notebook.hide(self.frameCargarMateria)
            self.notebook.add(self.frameCargarMateria)
            self.notebook.select(self.frameCargarMateria)

        def abrirVentanaBMMateria():
            self.notebook.hide(self.frameBMMateria)
            self.notebook.add(self.frameBMMateria)
            self.notebook.select(self.frameBMMateria) 
            self.cargar_listamaterias()


        self.tituloVentanaInicio=tk.Label(masterCarga,text="Incio")
        self.tituloVentanaInicio.config(bg="#FFF", font=("Arial", 20))
        self.tituloVentanaInicio.place(x=400,y=10)
        self.imagenAlumno = tk.PhotoImage(file="imagenesApp/user-graduateprueba3.png")
        self.menuAlumno = tk.Menubutton(masterCarga,image=self.imagenAlumno, bg='#FFF', fg='white', border=0, cursor='hand2',direction="right")
        self.menuAlumno.menu=tk.Menu(self.menuAlumno,tearoff=0)
        self.menuAlumno['menu']=self.menuAlumno.menu
        self.menuAlumno.menu.add_command(label="Crear Alumno",command=abrirVentanaAlumno)
        self.menuAlumno.menu.add_command(label="Modificar Alumno",command=abrirVentanaBMAlumno)
        self.menuAlumno.place(x=30,y=150)
        self.alumnoLabel = tk.Label(masterCarga,text="Cargar Alumno")
        self.alumnoLabel.config(bg="#FFF", font=("Arial", 15))
        self.alumnoLabel.place(x=30,y=90)
        tk.Frame(masterCarga, width=200, height=1.5, bg='#8CD0F7').place(x=32, y=120)
        self.imagenProfesor = tk.PhotoImage(file="imagenesApp/user-tie2.png")
        self.menuProfesor = tk.Menubutton(masterCarga,image=self.imagenProfesor, bg='#FFF', fg='white', border=0, cursor='hand2',direction="right")
        self.menuProfesor.menu=tk.Menu(self.menuProfesor,tearoff=0)
        self.menuProfesor['menu']=self.menuProfesor.menu
        self.menuProfesor.menu.add_command(label="Crear Docente",command=abrirVentanaProfesor)
        self.menuProfesor.menu.add_command(label="Modificar Docente",command=abrirVentanaBMProfesor)
        self.menuProfesor.place(x=310,y=150)
        self.profesorLabel = tk.Label(masterCarga,text="Cargar Profesor")
        self.profesorLabel.config(bg="#FFF", font=("Arial", 15))
        self.profesorLabel.place(x=312,y=90)
        tk.Frame(masterCarga, width=200, height=1.5, bg='#8CD0F7').place(x=314, y=120)
        self.imagenMateria = tk.PhotoImage(file="imagenesApp/bookprueba.png")
        self.menuMateria = tk.Menubutton(masterCarga,image=self.imagenMateria, bg='#FFF', fg='white', border=0, cursor='hand2',direction="right")
        self.menuMateria.menu=tk.Menu(self.menuMateria,tearoff=0)
        self.menuMateria['menu']=self.menuMateria.menu
        self.menuMateria.menu.add_command(label="Crear Materia",command=abrirVentanaMateria)
        self.menuMateria.menu.add_command(label="Modificar Materia",command=abrirVentanaBMMateria)
        self.menuMateria.place(x=590,y=150)
        self.materiaLabel = tk.Label(masterCarga,text="Cargar Materia")
        self.materiaLabel.config(bg="#FFF", font=("Arial", 15))
        self.materiaLabel.place(x=592,y=90)
        tk.Frame(masterCarga, width=200, height=1.5, bg='#8CD0F7').place(x=594, y=120)


if __name__ == '__main__':
    aplicacion1 = ConsultaAlumnos()
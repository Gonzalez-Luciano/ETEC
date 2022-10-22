import tkinter as tk
from tkinter import Label, ttk, END
from tkinter import messagebox,Menubutton
from Alumno import *
import re
from dbAlumnos import dbAlumnos
from dbProfesores import dbPrfesores
from dbMaterias import dbMaterias

class ConsultaAlumnos():
    #Ejemplos de nombres para los alumnos 
    lista = []
    lista.append( Alumno("0", "Luciano González", "tarde") )
    lista.append( Alumno("1", "Juan Jose", "manana") )
    lista.append( Alumno("2", "Samantha Delgado", "tarde") )
    lista.append( Alumno("3", "Alex Granado", "manana") )
    lista.append( Alumno("4", "Michelle Ramirez", "tarde") )
    lista.append( Alumno("5", "Natalia Alonso", "manana") )
    lista.append( Alumno("6", "Anthony Soto", "tarde") )
    lista.append( Alumno("7", "Fernando Domínquez", "manana") )
    lista.append( Alumno("8", "María Paula Jasso", "tarde") )
    lista.append( Alumno("9", "Paz Gómez", "manana") )
    lista.append( Alumno("10", "Magdalena Garrido", "tarde") )
    lista.append( Alumno("11", "Maximiliano Crespo", "manana") )

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
        self.frameCargarProfesor = tk.Frame(self.notebook,bg="#FFF")
        self.MasterCargarProfesor(self.frameCargarProfesor)
        self.frameCargarMateria = tk.Frame(self.notebook,bg="#FFF")
        self.MasterCargarMateria(self.frameCargarMateria)
        # Añadirlas al panel con su respectivo texto.

        self.notebook.add(self.frameInicio,text="Inicio",padding=20)
        self.notebook.add(self.frameCargarAlumno, text="Cargar Alumno", padding=20)
        self.notebook.add(self.frameCargarProfesor, text="Cargar Profesor", padding=20)
        self.notebook.add(self.frameCargarMateria, text="Cargar Materia",padding=20)

        # Ocultar las ventanas.
        self.notebook.hide(self.frameCargarAlumno)
        self.notebook.hide(self.frameCargarProfesor)
        self.notebook.hide(self.frameCargarMateria)
        self.notebook.pack(padx=10, pady=10)
        
        self.ventana1.mainloop()
    

    def estilos(self):#Estilos de la App   
        self.style = ttk.Style()
        self.style.theme_create ("estilo_tb",parent="clam",settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0],"background": "#FFFFFF"} },
            "TNotebook.Tab": {
                "configure": {"padding": [5, 1], "background": "#FFFFFF" },
                "map":       {"background": [("selected", "#8CD0F7"),("active","#A7E1F1")],
                            "expand": [("selected", [2, 2, 2, 0])] } }, 
            "TButton": {
                "map":       {"background": [("!active","#FFF"),("active", "#FFFFFF"),("pressed","#8CD0F7")] }}})
                

        self.style.theme_use("estilo_tb")
    
    #Función para buscar alumnos en la listbox
    # def buscar(self):
    #     alumno=self.entryBuscador.get()
    #     for x in range(self.listbox1.size()):
    #         alumnoBuscado = self.listbox1.get(x)
    #         if alumno == alumnoBuscado:
    #             self.listbox1.selection_set(x)
    # #Messagebox final con todos los datos    
    # def recuperar(self):
    #     combo1 = self.comboboxMateria.get()
    #     nota = self.notAlumno.get().strip()
    #     selector = self.listbox1.curselection()
    #     if selector != ():
    #         alumn = self.listbox1.get(selector)
    #         try:
    #             int(nota)
    #             messagebox.askyesno("Pregunta", f"¿Quiere Guardar Los Datos?\n\nAlumno: {alumn}\nMateria: {combo1}\nNota: {nota}")
    #         except ValueError:
    #             messagebox.showerror("Error de entrada de nota","Ingrese un número")
    #     else:
    #         messagebox.showerror("Error de entrada de nota","Seleccione un alumno")
            
    # #Función de filtrado de lista 
    # def filtro(self):
    #     listaLocal = self.__class__.lista
    #     self.listbox1.delete(0, tk.END)
    #     if self.checkMananaValue.get() == True and self.checkTardeValue.get() == True:
    #         for x in range(len(listaLocal)):
    #             self.listbox1.insert(x,listaLocal[x].GetNombre())
    #     elif self.checkMananaValue.get() == True:
    #         for x in range(len(listaLocal)):
    #             if (listaLocal[x].GetTurno() == "manana"):
    #                 self.listbox1.insert(x, listaLocal[x].GetNombre())
    #     elif self.checkTardeValue.get() == True:
    #         for x in range(len(listaLocal)):
    #             if (listaLocal[x].GetTurno() == "tarde"):
    #                 self.listbox1.insert(x,listaLocal[x].GetNombre())
    #     elif self.checkTodosValue.get() == True:
    #        for x in range(len(listaLocal)):
    #             self.listbox1.insert(x,listaLocal[x].GetNombre())
    #     else:
    #         messagebox.showerror("Error", "Por favor, seleccione un turno")  

    
    def MasterCargarAlumno(self, masterCarga):#Funcion para crear interfaz grafica de la pestaña Cargar
        self.tituloCargarAlumno=tk.Label(masterCarga,text="Cargar Alumno")
        self.tituloCargarAlumno.config(bg="#FFF", font=("Arial", 20))
        self.tituloCargarAlumno.place(x=360,y=10)
        tk.Frame(masterCarga, width=800, height=1, bg='#8CD0F7').place(x=30, y=70)
       
        def on_enter(e):
            name=self.nombreEntryAlumno.get()
            if name == 'Nombre':
                self.nombreEntryAlumno.delete(0, 'end')
    
        def on_leave(e):
            name=self.nombreEntryAlumno.get()
            if name=='':
                self.nombreEntryAlumno.insert(0, 'Nombre')
        self.nombreEntryAlumno=tk.Entry(masterCarga)
        self.nombreEntryAlumno.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
        self.nombreEntryAlumno.insert(0, 'Nombre')
        self.nombreEntryAlumno.bind('<FocusIn>', on_enter)
        self.nombreEntryAlumno.bind('<FocusOut>', on_leave)
        self.nombreEntryAlumno.place(x=320,y=106)
        tk.Frame(masterCarga, width=300, height=3, bg='#8CD0F7').place(x=315, y=136)
        def on_enter(e):
            name=self.apellidoEntryAlumno.get()
            if name == 'Apellido':
                self.apellidoEntryAlumno.delete(0, 'end')
    
        def on_leave(e):
            name=self.apellidoEntryAlumno.get()
            if name=='':
                self.apellidoEntryAlumno.insert(0, 'Apellido')
        self.apellidoEntryAlumno=tk.Entry(masterCarga)
        self.apellidoEntryAlumno.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
        self.apellidoEntryAlumno.insert(0, 'Apellido')
        self.apellidoEntryAlumno.bind('<FocusIn>', on_enter)
        self.apellidoEntryAlumno.bind('<FocusOut>', on_leave)
        self.apellidoEntryAlumno.place(x=320,y=196)
        tk.Frame(masterCarga, width=300, height=3, bg='#8CD0F7').place(x=315, y=226)
        # self.horarioLabel=tk.Label(masterCarga,text="Turno:")
        # self.horarioLabel.config(bg="#8CD0F7",padx=15,font=("Arial", 15))
        # self.horarioLabel.place(x=50,y=300)
        # self.opcionHorario=tk.StringVar()
        # horarios=("Mañana","Tarde")
        # self.comboboxHorario=ttk.Combobox(masterCarga, 
        #                           width=20, 
        #                           textvariable=self.opcionHorario, 
        #                           values=horarios)
        # self.comboboxHorario.place(x=150,y=306)
        # self.comboboxHorario.current(0)
        def on_enter(e):
            name=self.cuilEntryAlumno.get()
            if name == 'Cuil':
                self.cuilEntryAlumno.delete(0, 'end')

        def on_leave(e):
            name=self.cuilEntryAlumno.get()
            if name=='':
                self.cuilEntryAlumno.insert(0, 'Cuil')
        self.cuilEntryAlumno=tk.Entry(masterCarga)
        self.cuilEntryAlumno.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
        self.cuilEntryAlumno.insert(0, 'Cuil')
        self.cuilEntryAlumno.bind('<FocusIn>', on_enter)
        self.cuilEntryAlumno.bind('<FocusOut>', on_leave)
        self.cuilEntryAlumno.place(x=320,y=286)
        tk.Frame(masterCarga, width=300, height=3, bg='#8CD0F7').place(x=315, y=316)
        self.botonGuardarNuevoAlumno=tk.Button(masterCarga,command=self.GuardarNuevoAlumno,width=20, pady=7, text='Cargar Alumno', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.botonGuardarNuevoAlumno.place(x=680,y=370)

    def MasterCargarProfesor(self, masterCarga):#Funcion para crear interfaz grafica de la pestaña Cargar
        self.tituloCargarDatos=tk.Label(masterCarga,text="Cargar Profesor")
        self.tituloCargarDatos.config(bg="#FFF", font=("Arial", 20))
        self.tituloCargarDatos.place(x=360,y=10)
        tk.Frame(masterCarga, width=800, height=1, bg='#8CD0F7').place(x=30, y=70)
        
        def on_enter(e):
            name=self.nombreEntryProfesor.get()
            if name == 'Nombre':
                self.nombreEntryProfesor.delete(0, 'end')
    
        def on_leave(e):
            name=self.nombreEntryProfesor.get()
            if name=='':
                self.nombreEntryProfesor.insert(0, 'Nombre')
        self.nombreEntryProfesor=tk.Entry(masterCarga)
        self.nombreEntryProfesor.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 12))
        self.nombreEntryProfesor.insert(0, 'Nombre')
        self.nombreEntryProfesor.bind('<FocusIn>', on_enter)
        self.nombreEntryProfesor.bind('<FocusOut>', on_leave)
        self.nombreEntryProfesor.place(x=320,y=106)
        tk.Frame(masterCarga, width=298, height=3, bg='#8CD0F7').place(x=317, y=133)
        def on_enter(e):
            name=self.apellidoEntryProfesor.get()
            if name == 'Apellido':
                self.apellidoEntryProfesor.delete(0, 'end')
    
        def on_leave(e):
            name=self.apellidoEntryProfesor.get()
            if name=='':
                self.apellidoEntryProfesor.insert(0, 'Apellido')
        self.apellidoEntryProfesor=tk.Entry(masterCarga)
        self.apellidoEntryProfesor.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 12))
        self.apellidoEntryProfesor.insert(0, 'Apellido')
        self.apellidoEntryProfesor.bind('<FocusIn>', on_enter)
        self.apellidoEntryProfesor.bind('<FocusOut>', on_leave)
        self.apellidoEntryProfesor.place(x=320,y=176)
        tk.Frame(masterCarga, width=298, height=3, bg='#8CD0F7').place(x=317, y=206)
        
        def on_enter(e):
            name=self.gmailEntryProfesor.get()
            if name == 'Correo':
                self.gmailEntryProfesor.delete(0, 'end')
    
        def on_leave(e):
            name=self.gmailEntryProfesor.get()
            if name=='':
                self.gmailEntryProfesor.insert(0, 'Correo')
        self.gmailEntryProfesor=tk.Entry(masterCarga)
        self.gmailEntryProfesor.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 12))
        self.gmailEntryProfesor.insert(0, 'Correo')
        self.gmailEntryProfesor.bind('<FocusIn>', on_enter)
        self.gmailEntryProfesor.bind('<FocusOut>', on_leave)
        self.gmailEntryProfesor.place(x=320,y=246)
        tk.Frame(masterCarga, width=298, height=3, bg='#8CD0F7').place(x=317, y=276)
        
        def on_enter(e):
            name=self.cuilEntryProfesor.get()
            if name == 'Cuil':
                self.cuilEntryProfesor.delete(0, 'end')
    
        def on_leave(e):
            name=self.cuilEntryProfesor.get()
            if name=='':
                self.cuilEntryProfesor.insert(0, 'Cuil')
        self.cuilEntryProfesor=tk.Entry(masterCarga)
        self.cuilEntryProfesor.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 12))
        self.cuilEntryProfesor.insert(0, 'Cuil')
        self.cuilEntryProfesor.bind('<FocusIn>', on_enter)
        self.cuilEntryProfesor.bind('<FocusOut>', on_leave)
        self.cuilEntryProfesor.place(x=320,y=316)
        tk.Frame(masterCarga, width=298, height=3, bg='#8CD0F7').place(x=317, y=346)
        # self.horarioLabel=tk.Label(masterCarga,text="Turno:")
        # self.horarioLabel.config(bg="#8CD0F7",padx=15,font=("Arial", 15))
        # self.horarioLabel.place(x=50,y=300)
        # self.opcionHorario=tk.StringVar()
        # horarios=("Mañana","Tarde")
        # self.comboboxHorario=ttk.Combobox(masterCarga, 
        #                           width=20, 
        #                           textvariable=self.opcionHorario, 
        #                           values=horarios)        
        # self.comboboxHorario.place(x=150,y=306)
        # self.comboboxHorario.current(0)
        
        self.botonNuevoProfesor=tk.Button(masterCarga,command=self.GuardarNuevoProfesor,width=20, pady=7, text='Cargar Profesor', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.botonNuevoProfesor.config()
        self.botonNuevoProfesor.place(x=680,y=370)
    
    def MasterCargarMateria(self,masterCarga):
        self.tituloCargarMateria=tk.Label(masterCarga,text="Cargar Materia")
        self.tituloCargarMateria.config(bg="#FFF", font=("Arial", 20))
        self.tituloCargarMateria.place(x=360,y=10)
        tk.Frame(masterCarga, width=800, height=1, bg='#8CD0F7').place(x=30, y=70)
       
        def on_enter(e):
            name=self.nombreEntryMateria.get()
            if name == 'Nombre':
                self.nombreEntryMateria.delete(0, 'end')
    
        def on_leave(e):
            name=self.nombreEntryMateria.get()
            if name=='':
                self.nombreEntryMateria.insert(0, 'Nombre')
        self.nombreEntryMateria=tk.Entry(masterCarga)
        self.nombreEntryMateria.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
        self.nombreEntryMateria.insert(0, 'Nombre')
        self.nombreEntryMateria.bind('<FocusIn>', on_enter)
        self.nombreEntryMateria.bind('<FocusOut>', on_leave)
        self.nombreEntryMateria.place(x=320,y=106)
        tk.Frame(masterCarga, width=300, height=3, bg='#8CD0F7').place(x=315, y=136)
        def on_enter(e):
            name=self.descripEntrymateria.get()
            if name == 'Descripción':
                self.descripEntrymateria.delete(0, 'end')

        def on_leave(e):
            name=self.descripEntrymateria.get()
            if name=='':
                self.descripEntrymateria.insert(0, 'Descripción')
        self.descripEntrymateria=tk.Entry(masterCarga)
        self.descripEntrymateria.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
        self.descripEntrymateria.insert(0, 'Descripción')
        self.descripEntrymateria.bind('<FocusIn>', on_enter)
        self.descripEntrymateria.bind('<FocusOut>', on_leave)
        self.descripEntrymateria.place(x=320,y=196)
        tk.Frame(masterCarga, width=300, height=3, bg='#8CD0F7').place(x=315, y=226)
        self.botonNuevaMateria=tk.Button(masterCarga,command=self.GuardarNuevaMateria,width=20, pady=7, text='Cargar Materia', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.botonNuevaMateria.place(x=680,y=370)

#<---------------------------------------VENTANA DE INICIO------------------------------------------------------->
    def VentanaInicio(self,masterCarga):
        #Funcion para que aparesca la ventana cargar profesor 
        def abrirVentanaProfesor():
            self.notebook.hide(self.frameCargarProfesor)
            self.notebook.add(self.frameCargarProfesor)
            self.notebook.select(self.frameCargarProfesor)

        #Funcion para que aparesca la ventana cargar alumno 
        def abrirVentanaAlumno():
            self.notebook.hide(self.frameCargarAlumno)
            self.notebook.add(self.frameCargarAlumno)
            self.notebook.select(self.frameCargarAlumno)
        
        #Funcion para que aparesca la ventana cargar materia 
        def abrirVentanaMateria():
            self.notebook.hide(self.frameCargarMateria)
            self.notebook.add(self.frameCargarMateria)
            self.notebook.select(self.frameCargarMateria)

        self.tituloVentanaInicio=tk.Label(masterCarga,text="Incio")
        self.tituloVentanaInicio.config(bg="#FFF", font=("Arial", 20))
        self.tituloVentanaInicio.place(x=400,y=10)
        self.imagenAlumno = tk.PhotoImage(file="imagenesApp/user-graduateprueba3.png")
        self.menuAlumno = tk.Menubutton(masterCarga,image=self.imagenAlumno, bg='#FFF', fg='white', border=0, cursor='hand2',direction="right")
        self.menuAlumno.menu=tk.Menu(self.menuAlumno,tearoff=0)
        self.menuAlumno['menu']=self.menuAlumno.menu
        self.menuAlumno.menu.add_command(label="Crear Alumno",command=abrirVentanaAlumno)
        self.menuAlumno.menu.add_command(label="Modificar Alumno",command=abrirVentanaAlumno,state='disabled')
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
        self.menuProfesor.menu.add_command(label="Modificar Docente",command=abrirVentanaAlumno,state='disabled')
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
        self.menuMateria.menu.add_command(label="Modificar Materia",command=abrirVentanaAlumno,state='disabled')
        self.menuMateria.place(x=590,y=150)
        self.materiaLabel = tk.Label(masterCarga,text="Cargar Materia")
        self.materiaLabel.config(bg="#FFF", font=("Arial", 15))
        self.materiaLabel.place(x=592,y=90)
        tk.Frame(masterCarga, width=200, height=1.5, bg='#8CD0F7').place(x=594, y=120)

    #<-----------------------Función para guardar a los nuevos alumnos en base de datos (más info en dbAlumnos.py)----------------------->
    def GuardarNuevoAlumno(self):
        nombreAlumn= self.nombreEntryAlumno.get().strip()
        apellidoAlumn=self.apellidoEntryAlumno.get().strip()
        cuilAlumn=self.cuilEntryAlumno.get().strip()
        alumnCompleto=nombreAlumn+" "+ apellidoAlumn
        print(alumnCompleto)
        # if self.comboboxHorario.get()=="Mañana":
        #     comboboxSeleccion="manana"
        # elif self.comboboxHorario.get()=="Tarde":
        #     comboboxSeleccion="tarde"
        # else:pass
        database= dbAlumnos("localhost","root","test")
        try:
            if nombreAlumn != "Nombre" and apellidoAlumn != "Apellido":
                if nombreAlumn != "" and apellidoAlumn != "":
                    int(cuilAlumn)
                    database.crear_alumno(cuilAlumn,nombreAlumn,apellidoAlumn)
                    messagebox.showinfo("","Alumno Cargado con Exito")
            else:
                messagebox.showerror("Error de entrada de Alumno","Falta un Nombre o Apellido")
        except ValueError:
            messagebox.showerror("Error de Entrada","CUIL invalido")

#<-----------------------Función para guardar a los nuevos profesores en base de datos (más info en dbProfesores.py)----------------------->
    def GuardarNuevoProfesor(self):
        nombreProfesor= self.nombreEntryProfesor.get().strip()
        apellidoProfesor=self.apellidoEntryProfesor.get().strip()
        cuilProfesor=self.cuilEntryProfesor.get().strip()
        correoProfesor=self.gmailEntryProfesor.get().strip()
        profesorCompleto=nombreProfesor+" "+ apellidoProfesor
        def es_correo_valido(correo):
            expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
            return re.match(expresion_regular, correo) is not None
        print(profesorCompleto)
        # if self.comboboxHorario.get()=="Mañana":
        #     comboboxSeleccion="manana"
        # elif self.comboboxHorario.get()=="Tarde":
        #     comboboxSeleccion="tarde"
        # else:pass
        # if self.comboboxHorario.get()=="Mañana":
        #     comboboxSeleccion="manana"
        # elif self.comboboxHorario.get()=="Tarde":
        #     comboboxSeleccion="tarde"
        # else:pass
        print(correoProfesor)
        print(es_correo_valido(correoProfesor))
        database= dbPrfesores("localhost","root","test")
        try:
            int(cuilProfesor)
            if nombreProfesor != "Nombre" and apellidoProfesor != "Apellido" and cuilProfesor != "Cuil" and correoProfesor != "Correo" and es_correo_valido(correoProfesor) == True:
                database.crear_profesor(cuilProfesor,nombreProfesor,apellidoProfesor,correoProfesor)
            elif nombreProfesor != "" and apellidoProfesor != "" and cuilProfesor != "" and correoProfesor != "" and es_correo_valido(correoProfesor) == True:
                database.crear_profesor(cuilProfesor,nombreProfesor,apellidoProfesor,correoProfesor)
            else:
                messagebox.showerror("Error de entrada de Alumno","Falta un Dato o es Incorrecto")
        except ValueError:
            messagebox.showerror("Error de Entrada","CUIL invalido")
        # if nombreProfesor != "Nombre" or "" and apellidoProfesor != "Apellido" or "":
        #     ultimoId = len(self.__class__.lista)
        #     self.__class__.lista.append( Alumno(str(ultimoId), profesorCompleto))
        # else:
        #     messagebox.showerror("Error de entrada de Profesor","Falta un Nombre o Apellido")
    def GuardarNuevaMateria(self):
        nombreMateria=self.nombreEntryMateria.get().strip()
        descripMateria=self.descripEntrymateria.get().strip()
        database= dbMaterias("localhost","root","test")
        if nombreMateria != "Nombre" and descripMateria != "Descripción":
            if nombreMateria != "" and descripMateria != "":
                database.crear_materia(nombreMateria,descripMateria)
        else:
            messagebox.showerror("Error de entrada de Materia","Falta un Nombre o Descripción")
aplicacion1 = ConsultaAlumnos()
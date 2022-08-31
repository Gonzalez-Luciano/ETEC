#https://es.stackoverflow.com/questions/280768/c%C3%B3mo-cambiar-din%C3%A1micamente-el-contenido-de-un-listbox-en-base-a-la-opci%C3%B3n-elegi
#Message box, entry(con nota del alumno) y label indicandole al profesor
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Alumno import *


class ConsultaAlumnos():
    #Ejemplos de nombres para los alumnos 
    '''alumno = Alumno()
    alumno.SetIdAlumno("1")
    alumno.SetNombre("nombre")
    alumno.SetTurno("tarde")
    alumno2 = Alumno()
    alumno2.SetIdAlumno("2")
    alumno2.SetNombre("nombre2")
    alumno2.SetTurno("manana")

    

    listaAlumno = [Alumno()]
    listaAlumno.append(alumno)
    listaAlumno.append(alumno2)

    for alumno in listaAlumno: 
        if(alumno.GetTurno() == "manana"):
            print(alumno.GetNombre())'''


    '''lista = {
        0: {"nombre" : "Luciano González", "turno" : "tarde"},
        1: {"nombre" : "Juan Jose", "turno" : "manana"},
        2: {"nombre" : "Ana Sofía Granado", "turno" : "manana"},
        3: {"nombre" : "Cristóbal Leon", "turno" : "manana"},
        4: {"nombre" : "Antonia Leon", "turno" : "manana"},
        5: {"nombre" : "Maximiliano Crespo", "turno" : "manana"},
        6: {"nombre" : "Magdalena Garrido", "turno" : "manana"},
        7: {"nombre" : "Paz Gómez", "turno" : "tarde"},
        8: {"nombre" : "María Paula Jasso", "turno" : "tarde"},
        9: {"nombre" : "Fernando Domínquez", "turno" : "tarde"},
        10: {"nombre" : "Anthony Soto", "turno" : "tarde"},
        11: {"nombre" : "Natalia Alonso", "turno" : "tarde"},
        12: {"nombre" : "Michelle Ramirez", "turno" : "tarde"},
        13: {"nombre" : "Alex Granado", "turno" : "tarde"},
        14: {"nombre" : "Samantha Delgado", "turno" : "tarde"},
    }'''
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
        # self.ventana1.iconphoto(True, tk.PhotoImage(file='C:/Users/SEVN/Desktop/Aplicacion Edutec/logo.png'))
        self.ventana1.resizable(0,0)
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self.ventana1)
        self.frameGuargarDatos = tk.Frame(self.notebook)
        self.frameGuargarDatos.config(bg="#8CD0F7")
        self.frameCargarDatos = tk.Frame(self.notebook)
        self.frameCargarDatos.config(bg="#8CD0F7")
        self.MasterGuardarDatos(self.frameGuargarDatos)
        self.MasterCargarDatos (self.frameCargarDatos)
        
        # Añadirlas al panel con su respectivo texto.
        self.notebook.add(self.frameGuargarDatos, text="Guardar", padding=20)

        self.notebook.add(self.frameCargarDatos, text="Cargar", padding=20)
        
        self.notebook.pack(padx=10, pady=10)
        
        self.ventana1.mainloop()
    

    def estilos(self):#Estilos de la App   
        self.style = ttk.Style()
        self.style.theme_create ("estilo_tb",parent="default",settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0],"background": "#FFFFFF"} },
            "TNotebook.Tab": {
                "configure": {"padding": [5, 1], "background": "#FFFFFF" },
                "map":       {"background": [("selected", "#8CD0F7"),("active","#A7E1F1")],
                            "expand": [("selected", [2, 2, 2, 0])] } }, 
            "TButton": {
                "map":       {"background": [("active", "#FFFFFF"),("pressed","#8CD0F7")] }}})
                

        self.style.theme_use("estilo_tb")


    def MasterGuardarDatos(self, masterGuarda):#Funcion para crear interfaz grafica de la pestaña Guardar
        self.buscarImagen=tk.PhotoImage(file="C:/Users/TuKK/Desktop/programaEscuela/imagenesApp/boton-busqueda2.png")
        self.titulo=tk.Label(masterGuarda,text="Información General")
        self.titulo.config(bg="#8CD0F7", font=("Arial", 20))
        self.titulo.grid(row=0, column=3,columnspan=6,pady=10)
        # self.textoEjemplo= tk.StringVar()
        # self.textoEjemplo.set("Nombre de Alumno")
        self.entryBuscador=tk.Entry(masterGuarda)
        self.entryBuscador.insert(0," Nombre del Alumno")
        self.entryBuscador.grid(row=1,column=0,pady=5)
        self.buttonBuscador=ttk.Button(masterGuarda,image=self.buscarImagen,command=self.buscar, cursor="hand2")
        self.buttonBuscador.grid(row=1,column=1,pady=5)
        self.notAlumno=tk.Entry(masterGuarda)
        self.notAlumno.grid(row=5, column=9,columnspan=4,padx=10,pady=10)
        self.label2=tk.Label(masterGuarda,text="Nota del alumno:")
        self.label2.grid(row=5, column=8,pady=10)
        self.label2.config(bg="#8CD0F7")
        #<-----------------------------Boton para filtrar entre las opciones de la listbox-------------------------------------------->
        self.boton_filtrar=ttk.Button(masterGuarda, text="Filtrar",command=self.filtro, cursor="hand2")
        self.boton_filtrar.grid(row=2,column=10,columnspan=4)
        #<------------------------------Botones de filtro mañana, tarde y todos--------------------------------------------------------> 
        self.turnos=tk.Label(masterGuarda,text="Seleccione un turno/s:")
        self.turnos.config(bg="#8CD0F7")
        self.turnos.grid(row=2, column=3, padx=15)
        self.checkMananaValue = tk.BooleanVar()
        self.checkManana=tk.Checkbutton(masterGuarda,text="Mañana", variable=self.checkMananaValue)
        self.checkManana.grid(column=6, row=2,sticky="w")
        self.checkManana.config(bg="#8CD0F7", activebackground="#8CD0F7")
        self.checkTardeValue = tk.BooleanVar()
        self.checkTarde=tk.Checkbutton(masterGuarda,text="Tarde", variable=self.checkTardeValue)
        self.checkTarde.grid(column=7, row=2,sticky="w")
        self.checkTarde.config(bg="#8CD0F7", activebackground="#8CD0F7")
        self.checkTodosValue = tk.BooleanVar()
        self.checkTodos=tk.Checkbutton(masterGuarda,text="Todos", variable=self.checkTodosValue)
        self.checkTodos.grid(column=8, row=2,sticky="w")
        self.checkTodos.config(bg="#8CD0F7", activebackground="#8CD0F7")
        #<----------------------------------------------Scrollbar , Listbox y Combobox------------------------------------------------------------------------------------>
        self.scroll1 = tk.Scrollbar(masterGuarda, orient=tk.VERTICAL)
        self.listbox1=tk.Listbox(masterGuarda, selectmode=tk.SINGLE, yscrollcommand=self.scroll1.set,bg="#ADD7EF",exportselection=False)
        self.listbox1.grid(column=0,row=2)
        self.scroll1.configure(command=self.listbox1.yview)        
        self.scroll1.grid(column=1, row=2, sticky='NS')     
        self.listbox1.grid(column=0,row=2)
        self.labelAsignatura=ttk.Label(masterGuarda, text="Seleccione la asignatura:")
        self.labelAsignatura.grid(column=0, row=5)
        self.labelAsignatura.config(background="#8CD0F7")
        self.opcionMateria=tk.StringVar()
        asignatura=("Matemática","Lengua","Ciencias Sociales","Ciencias Naturales","Inglés","Informática","Artística", "Educación Física")
        self.comboboxMateria=ttk.Combobox(masterGuarda, 
                                  width=20, 
                                  textvariable=self.opcionMateria, 
                                  values=asignatura)
        self.comboboxMateria.current(0)
        self.comboboxMateria.grid(column=3, row=5)
        self.boton1=ttk.Button(masterGuarda, text="Guardar", command=self.recuperar,cursor="hand2")
        self.boton1.grid(column=3, row=6,columnspan=6,pady=10)

    #Función para buscar alumnos en la listbox
    def buscar(self):
        alumno=self.entryBuscador.get()
        for x in range(self.listbox1.size()):
            alumnoBuscado = self.listbox1.get(x)
            if alumno == alumnoBuscado:
                self.listbox1.selection_set(x)
    #Messagebox final con todos los datos    
    def recuperar(self):
        combo1 = self.comboboxMateria.get()
        nota = self.notAlumno.get().strip()
        selector = self.listbox1.curselection()
        if selector != ():
            alumn = self.listbox1.get(selector)
            try:
                int(nota)
                messagebox.askyesno("Pregunta", f"¿Quiere Guardar Los Datos?\n\nAlumno: {alumn}\nMateria: {combo1}\nNota: {nota}")
            except ValueError:
                messagebox.showerror("Error de entrada de nota","Ingrese un número")
        else:
            messagebox.showerror("Error de entrada de nota","Seleccione un alumno")
            
    #Función de filtrado de lista 
    def filtro(self):
        listaLocal = self.__class__.lista
        self.listbox1.delete(0, tk.END)
        if self.checkMananaValue.get() == True and self.checkTardeValue.get() == True:
            for x in range(len(listaLocal)):
                self.listbox1.insert(x,listaLocal[x].GetNombre())
        elif self.checkMananaValue.get() == True:
            for x in range(len(listaLocal)):
                if (listaLocal[x].GetTurno() == "manana"):
                    self.listbox1.insert(x, listaLocal[x].GetNombre())
        elif self.checkTardeValue.get() == True:
            for x in range(len(listaLocal)):
                if (listaLocal[x].GetTurno() == "tarde"):
                    self.listbox1.insert(x,listaLocal[x].GetNombre())
        elif self.checkTodosValue.get() == True:
           for x in range(len(listaLocal)):
                self.listbox1.insert(x,listaLocal[x].GetNombre())
        else:
            messagebox.showerror("Error", "Por favor, seleccione un turno")  


    def MasterCargarDatos(self, masterCarga):#Funcion para crear interfaz grafica de la pestaña Cargar
        self.tituloCargarDatos=tk.Label(masterCarga,text="Alumnos")
        self.tituloCargarDatos.config(bg="#8CD0F7", font=("Arial", 20))
        self.tituloCargarDatos.grid(row=0, column=3,columnspan=6,pady=10)
        self.nombreLabel=tk.Label(masterCarga,text="Nombres:")
        self.nombreLabel.config(bg="#8CD0F7",padx=15)
        self.nombreLabel.grid(row=1,column=0,sticky="w")
        self.nombreEntry=tk.Entry(masterCarga)
        self.nombreEntry.grid(row=1,column=1,sticky="w") 
        self.apellidoLabel=tk.Label(masterCarga,text="Apellidos:")
        self.apellidoLabel.config(bg="#8CD0F7",padx=15)
        self.apellidoLabel.grid(row=2,column=0,sticky="w")
        self.apellidoEntry=tk.Entry(masterCarga)
        self.apellidoEntry.grid(row=2,column=1,sticky="w") 
        self.horarioLabel=tk.Label(masterCarga,text="Turno:")
        self.horarioLabel.config(bg="#8CD0F7",padx=15)
        self.horarioLabel.grid(row=3,column=0,sticky="w")
        self.opcionHorario=tk.StringVar()
        horarios=("Mañana","Tarde")
        self.comboboxHorario=ttk.Combobox(masterCarga, 
                                  width=20, 
                                  textvariable=self.opcionHorario, 
                                  values=horarios)
        self.comboboxHorario.grid(row=3,column=1,pady=15,sticky="w")
        self.comboboxHorario.current(0)
        self.botonGuardarNuevoAlumno=ttk.Button(masterCarga,text="Cargar Alumno",command=self.GuardarNuevoAlumno, cursor="hand2")
        self.botonGuardarNuevoAlumno.grid(row=4,column=0,padx=15,sticky="w")


    def GuardarNuevoAlumno(self):#Funcion para "guardar" a los nuevos alumnos
        nombreAlumn= self.nombreEntry.get().strip()
        apellidoAlumn=self.apellidoEntry.get().strip()
        alumnCompleto=nombreAlumn+" "+ apellidoAlumn
        print(alumnCompleto)
        if self.comboboxHorario.get()=="Mañana":
            comboboxSeleccion="manana"
        elif self.comboboxHorario.get()=="Tarde":
            comboboxSeleccion="tarde"
        else:pass
        if nombreAlumn != "" and apellidoAlumn != "":
            ultimoId = len(self.__class__.lista)
            self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto, comboboxSeleccion) )
        else:
            messagebox.showerror("Error de entrada de Alumno","Falta un Nombre o Apellido")

            
        
aplicacion1 = ConsultaAlumnos()
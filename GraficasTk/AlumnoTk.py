import tkinter as tk
from tkinter import Label, Widget, ttk, END
from tkinter import messagebox,Menubutton
from Alumno import *
from db.dbAlumnos import dbAlumnos

class AlumnoTk():

#<-----------------------------------------Funcion para crear interfaz grafica de la pestaña CargarAlumno---------------------------------->
    
    def MasterCargarAlumno(self, masterCarga):
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
 
#<-----------------------------------------Funcion para crear interfaz grafica de la pestaña GuardarAlumno---------------------------------->  
   
    def MasterBMAlumno(self, masterGuarda):
            self.buscarImagenAlumno=tk.PhotoImage(file="imagenesApp/boton-busqueda-alumno.png")
            self.titulo=tk.Label(masterGuarda,text="Información General")
            self.titulo.config(bg="#FFF",font=("Arial", 20))
            self.titulo.place(x=320,y=5)
            # self.textoEjemplo= tk.StringVar()
            # self.textoEjemplo.set("Nombre de Alumno")
            self.entryBuscadorBMAlumno=tk.Entry(masterGuarda, width=16, fg='black', border=0, font=('Microsoft Yahei UI', 12))
            self.entryBuscadorBMAlumno.insert(0," Buscar")
            self.entryBuscadorBMAlumno.place(x=50,y=76)
            #Función para crear y borrar el pre-texto de entryBuscador
            def on_enter(e):
                name=self.entryBuscadorBMAlumno.get()
                if name == ' Buscar':
                    self.entryBuscadorBMAlumno.delete(0, 'end')

            def on_leave(e):
                name=self.entryBuscadorBMAlumno.get()
                if name=='':
                    self.entryBuscadorBMAlumno.insert(0, ' Buscar')
            self.entryBuscadorBMAlumno.bind('<FocusIn>', on_enter)
            self.entryBuscadorBMAlumno.bind('<FocusOut>', on_leave)
            self.buttonBuscadorAlumno=tk.Button(masterGuarda,image=self.buscarImagenAlumno,command=self.cargar_listalumnos,width=25,height=25,bg='#57a1f9', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.buttonBuscadorAlumno.place(x=206,y=76)
            
            #Scrollbar , Listbox y Combobox
            self.scrollBMAlumno = tk.Scrollbar(masterGuarda, orient=tk.VERTICAL)
            self.listboxBMAlumno=tk.Listbox(masterGuarda, selectmode=tk.SINGLE,width=30,height=17 ,yscrollcommand=self.scrollBMAlumno.set,bg="#FFF",exportselection=False)
            self.listboxBMAlumno.place(x=50,y=100)
            self.listboxBMAlumno.bind("<<ListboxSelect>>",self.evento_clickAlumno)
            self.scrollBMAlumno.configure(command=self.listboxBMAlumno.yview)        
            self.scrollBMAlumno.place(x=176,y=100)     
            # self.labelAsignatura=ttk.Label(masterGuarda, text="Seleccione la asignatura:")
            # self.labelAsignatura.place(x=50, y=300)
            # self.labelAsignatura.config(background="#8CD0F7")
            # self.opcionMateria=tk.StringVar()
            # asignatura=("Matemática","Lengua","Ciencias Sociales","Ciencias Naturales","Inglés","Informática","Artística", "Educación Física")
            # self.comboboxMateria=ttk.Combobox(masterGuarda, 
            #                           width=20, 
            #                           textvariable=self.opcionMateria, 
            #                           values=asignatura)
            # self.comboboxMateria.current(0)
            # self.comboboxMateria.place(x=80, y=300)
            self.botonBorrarAlumno=tk.Button(masterGuarda,width=20, pady=7, command=self.baja_alumno, text='Borrar Alumno', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.botonBorrarAlumno.place(x=250,y=370)
            self.botonActualizarAlumno=tk.Button(masterGuarda,width=20, pady=7, command=self.ActualizarAlumno, text='Guardar Alumno', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.botonActualizarAlumno.place(x=680,y=370)
            def on_enter(e):
                name=self.nombreEntryBMAlumno.get()
                if name == 'Nombre':
                    self.nombreEntryBMAlumno.delete(0, 'end')
        
            def on_leave(e):
                name=self.nombreEntryBMAlumno.get()
                if name=='':
                    self.nombreEntryBMAlumno.insert(0, 'Nombre')
            self.nombreEntryBMAlumno=tk.Entry(masterGuarda)
            self.nombreEntryBMAlumno.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
            self.nombreEntryBMAlumno.insert(0, 'Nombre')
            self.nombreEntryBMAlumno.bind('<FocusIn>', on_enter)
            self.nombreEntryBMAlumno.bind('<FocusOut>', on_leave)
            self.nombreEntryBMAlumno.place(x=390,y=106)
            tk.Frame(masterGuarda, width=300, height=3, bg='#8CD0F7').place(x=385, y=136)
            def on_enter(e):
                name=self.apellidoEntryBMAlumno.get()
                if name == 'Apellido':
                    self.apellidoEntryBMAlumno.delete(0, 'end')
        
            def on_leave(e):
                name=self.apellidoEntryBMAlumno.get()
                if name=='':
                    self.apellidoEntryBMAlumno.insert(0, 'Apellido')
            self.apellidoEntryBMAlumno=tk.Entry(masterGuarda)
            self.apellidoEntryBMAlumno.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
            self.apellidoEntryBMAlumno.insert(0, 'Apellido')
            self.apellidoEntryBMAlumno.bind('<FocusIn>', on_enter)
            self.apellidoEntryBMAlumno.bind('<FocusOut>', on_leave)
            self.apellidoEntryBMAlumno.place(x=390,y=196)
            tk.Frame(masterGuarda, width=300, height=3, bg='#8CD0F7').place(x=385, y=226)
            def on_enter(e):
                name=self.cuilEntryBMAlumno.get()
                if name == 'Cuil':
                    self.cuilEntryBMAlumno.delete(0, 'end')

            def on_leave(e):
                name=self.cuilEntryBMAlumno.get()
                if name=='':
                    self.cuilEntryBMAlumno.insert(0, 'Cuil')
            self.cuilEntryBMAlumno=tk.Entry(masterGuarda)
            self.cuilEntryBMAlumno.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
            self.cuilEntryBMAlumno.insert(0, 'Cuil')
            self.cuilEntryBMAlumno.bind('<FocusIn>', on_enter)
            self.cuilEntryBMAlumno.bind('<FocusOut>', on_leave)
            self.cuilEntryBMAlumno.place(x=390,y=286)
            tk.Frame(masterGuarda, width=300, height=3, bg='#8CD0F7').place(x=385, y=316)

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
                    self.cargar_listalumnos()
                    self.nombreEntryAlumno.delete(0,'end')
                    self.apellidoEntryAlumno.delete(0,'end')
                    self.cuilEntryAlumno.delete(0,'end')
                    self.nombreEntryAlumno.insert(0, 'Nombre')
                    self.apellidoEntryAlumno.insert(0, 'Apellido')
                    self.cuilEntryAlumno.insert(0, 'Cuil')
            else:
                messagebox.showerror("Error de entrada de Alumno","Falta un Nombre o Apellido")
        except ValueError:
            messagebox.showerror("Error de Entrada","CUIL invalido")
    
#<-----------------------Función para actualizar a los nuevos alumnos en base de datos (más info en dbAlumnos.py)----------------------->

    def ActualizarAlumno(self):
        selector = self.listboxBMAlumno.curselection()
        nombreAlumn=self.nombreEntryBMAlumno.get().strip()
        apellidoAlumn=self.apellidoEntryBMAlumno.get().strip()
        cuilAlumn=self.cuilEntryBMAlumno.get().strip()
        if selector != ():
            idAlumno = self.listalumnos[selector[0]].id
        else:
            messagebox.showwarning("","Seleccione un Alumno")
            return
        try:
            database= dbAlumnos("localhost","root","test")
            if nombreAlumn != "Nombre" and apellidoAlumn != "Apellido":
                if nombreAlumn != "" and apellidoAlumn != "":
                    int(cuilAlumn)
                    database.actualizar_alumno(cuilAlumn,nombreAlumn,apellidoAlumn,idAlumno)
                    messagebox.showinfo("","Alumno actualizado con Exito")
                    self.cargar_listalumnos()
                    self.nombreEntryBMAlumno.delete(0,'end')
                    self.apellidoEntryBMAlumno.delete(0,'end')
                    self.cuilEntryBMAlumno.delete(0,'end')
                    self.nombreEntryBMAlumno.insert(0, 'Nombre')
                    self.apellidoEntryBMAlumno.insert(0, 'Apellido')
                    self.cuilEntryBMAlumno.insert(0, 'Cuil')
            else:
                messagebox.showerror("Error de entrada de Alumno","Falta un Nombre o Apellido")
        except ValueError:
            messagebox.showerror("Error de Entrada","CUIL invalido")
    
#<-----------------------Función para dar de baja a los alumnos en base de datos (más info en dbAlumnos.py)----------------------->
    def baja_alumno(self):
        selector = self.listboxBMAlumno.curselection()
        if selector != ():
            index = selector[0]
            respuesta = messagebox.askyesno(title='confirmacion',
                    message=f'¿Estas seguro de querer borrar a {self.listalumnos[index].nombre} {self.listalumnos[index].apellido}?')
            if respuesta:
                database = dbAlumnos("localhost","root","test")
                idAlumno = self.listalumnos[index].id
                database.baja_alumno(idAlumno)
                self.nombreEntryBMAlumno.delete(0,'end')
                self.apellidoEntryBMAlumno.delete(0,'end')
                self.cuilEntryBMAlumno.delete(0,'end')
                self.nombreEntryBMAlumno.insert(0, 'Nombre')
                self.apellidoEntryBMAlumno.insert(0, 'Apellido')
                self.cuilEntryBMAlumno.insert(0, 'Cuil')
                self.cargar_listalumnos()
            else:
                return
        else:
            messagebox.showerror("","Seleccione a un alumno")


    
    def evento_clickAlumno(self,event):
        selector = event.widget.curselection()
        print(selector)
        if selector != ():
            index = selector[0]
            self.nombreEntryBMAlumno.delete(0,'end')
            self.apellidoEntryBMAlumno.delete(0,'end')
            self.cuilEntryBMAlumno.delete(0,'end')
            self.nombreEntryBMAlumno.insert(0,self.listalumnos[index].nombre)
            self.apellidoEntryBMAlumno.insert(0,self.listalumnos[index].apellido)
            self.cuilEntryBMAlumno.insert(0,self.listalumnos[index].cuil)
        print(index)
            
    def cargar_listalumnos(self):
        self.listboxBMAlumno.delete(0, tk.END)
        alumnos = dbAlumnos("localhost","root","test").buscar_listalumno()
        self.listalumnos=[]
        index=0
        for alumno in alumnos:
            self.listalumnos.append(Alumno(alumno[0],alumno[1],alumno[2],alumno[3],alumno[4]))
            self.listboxBMAlumno.insert(index,alumno[2] + " " + alumno[3])
            print(self.listalumnos)
            index = index + 1
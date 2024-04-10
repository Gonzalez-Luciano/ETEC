import tkinter as tk
from tkinter import messagebox
from Alumno import *
from db.dbAlumnos import dbAlumnos

class CrearAlumnoTk():

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
 
    #<-----------------------Función para guardar a los nuevos alumnos en base de datos (más info en dbAlumnos.py)----------------------->
    def GuardarNuevoAlumno(self):
        nombreAlumn= self.nombreEntryAlumno.get().strip()
        apellidoAlumn=self.apellidoEntryAlumno.get().strip()
        cuilAlumn=self.cuilEntryAlumno.get().strip()
        database= dbAlumnos("localhost","EtecUser","tkinterdatabase","1234")
        try:
            if nombreAlumn != "Nombre" and apellidoAlumn != "Apellido":
                if nombreAlumn != "" and apellidoAlumn != "":
                    int(cuilAlumn)
                    database.crear_alumno(cuilAlumn,nombreAlumn,apellidoAlumn)
                    messagebox.showinfo("","Alumno Cargado con Exito")
                    self.cargar_listalumnos()
                    self.cargar_listboxalumnos()
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
    
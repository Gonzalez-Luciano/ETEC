from ast import Delete
import tkinter as tk
from tkinter import Label, Widget, ttk, END
from tkinter import messagebox,Menubutton
from Profesor import *
from db.dbProfesores import dbProfesores


class CrearProfesorTk():
    
#<-----------------------------------------Funcion para crear interfaz grafica de la pestaña CargarProfesor---------------------------------->

    def MasterCargarProfesor(self, masterCarga):
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
        self.botonNuevoProfesor=tk.Button(masterCarga,command=self.GuardarNuevoProfesor,width=20, pady=7, text='Cargar Profesor', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.botonNuevoProfesor.place(x=680,y=370)
      
      
#<-----------------------Función para guardar a los nuevos profesores en base de datos (más info en dbProfesores.py)----------------------->

    def GuardarNuevoProfesor(self):
        nombreProfesor= self.nombreEntryProfesor.get().strip()
        apellidoProfesor=self.apellidoEntryProfesor.get().strip()
        cuilProfesor=self.cuilEntryProfesor.get().strip()
        correoProfesor=self.gmailEntryProfesor.get().strip()
        profesorCompleto=nombreProfesor+" "+ apellidoProfesor
        def es_correo_valido(correo):
            if '@' in correo:
                return True
            else:
                return False
        print(profesorCompleto)
        print(correoProfesor)
        print(es_correo_valido(correoProfesor))
        database= dbProfesores("localhost","EtecUser","tkinterdatabase","1234")
        try:
            int(cuilProfesor)
            if nombreProfesor != "Nombre" and apellidoProfesor != "Apellido" and cuilProfesor != "Cuil" and correoProfesor != "Correo" and es_correo_valido(correoProfesor) == True:
                if nombreProfesor != "" and apellidoProfesor != "" and cuilProfesor != "" and correoProfesor != "" and es_correo_valido(correoProfesor) == True:
                    database.crear_profesor(cuilProfesor,nombreProfesor,apellidoProfesor,correoProfesor)
                    messagebox.showinfo("","Profesor Cargado con Exito")
                    self.cargar_listaprofesores()
                    self.cargar_listboxprofesores()
                    self.nombreEntryProfesor.delete(0,'end')
                    self.apellidoEntryProfesor.delete(0,'end')
                    self.gmailEntryProfesor.delete(0,'end')
                    self.cuilEntryProfesor.delete(0,'end')
                    self.nombreEntryProfesor.insert(0, 'Nombre')
                    self.apellidoEntryProfesor.insert(0, 'Apellido')
                    self.gmailEntryProfesor.insert(0, 'Correo')
                    self.cuilEntryProfesor.insert(0, 'Cuil')
            else:
                messagebox.showerror("Error de entrada de Alumno","Falta un Dato o es Incorrecto")
        except ValueError:
            messagebox.showerror("Error de Entrada","CUIL invalido")

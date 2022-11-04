from ast import Delete
import tkinter as tk
from tkinter import Label, Widget, ttk, END
from tkinter import messagebox,Menubutton
from Profesor import *
from db.dbProfesores import dbProfesores


class ProfesorTk():
    
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
        self.botonNuevoProfesor.place(x=680,y=370)
      
#<-------------------------------------------Funcion para crear interfaz grafica de la pestaña GuardarProfesor------------------------>  
    def MasterBMProfesor(self,masterGuarda):
        self.buscarImagenProfesor=tk.PhotoImage(file="imagenesApp/boton-busqueda-profesor.png")
        self.titulo=tk.Label(masterGuarda,text="Información General")
        self.titulo.config(bg="#FFF",font=("Arial", 20))
        self.titulo.place(x=320,y=5)
        # self.textoEjemplo= tk.StringVar()
        # self.textoEjemplo.set("Nombre de Alumno")
        self.entryBuscadorBMProfesor=tk.Entry(masterGuarda, width=16, fg='black', border=0, font=('Microsoft Yahei UI', 12))
        self.entryBuscadorBMProfesor.insert(0," Buscar")
        self.entryBuscadorBMProfesor.place(x=50,y=76)
        #Función para crear y borrar el pre-texto de entryBuscador
        def on_enter(e):
            name=self.entryBuscadorBMProfesor.get()
            if name == ' Buscar':
                self.entryBuscadorBMProfesor.delete(0, 'end')

        def on_leave(e):
            name=self.entryBuscadorBMProfesor.get()
            if name=='':
                self.entryBuscadorBMProfesor.insert(0, ' Buscar')
        self.entryBuscadorBMProfesor.bind('<FocusIn>', on_enter)
        self.entryBuscadorBMProfesor.bind('<FocusOut>', on_leave)
        self.buttonBuscadorProfesor=tk.Button(masterGuarda,image=self.buscarImagenProfesor,command=self.cargar_listaprofesores,width=25,height=25,bg='#57a1f9', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.buttonBuscadorProfesor.place(x=206,y=76)
        
        #Scrollbar , Listbox y Combobox
        self.scrollBMProfesor = tk.Scrollbar(masterGuarda, orient=tk.VERTICAL)
        self.listboxBMProfesor=tk.Listbox(masterGuarda, selectmode=tk.SINGLE,width=30,height=17 ,yscrollcommand=self.scrollBMProfesor.set,bg="#FFF",exportselection=False)
        self.listboxBMProfesor.place(x=50,y=100)
        self.listboxBMProfesor.bind("<<ListboxSelect>>",self.evento_clickProfesor)
        self.scrollBMProfesor.configure(command=self.listboxBMProfesor.yview)        
        self.scrollBMProfesor.place(x=176,y=100)  
        def on_enter(e):
            name=self.nombreEntryBMProfesor.get()
            if name == 'Nombre':
                self.nombreEntryBMProfesor.delete(0, 'end')
    
        def on_leave(e):
            name=self.nombreEntryBMProfesor.get()
            if name=='':
                self.nombreEntryBMProfesor.insert(0, 'Nombre')
        self.nombreEntryBMProfesor=tk.Entry(masterGuarda)
        self.nombreEntryBMProfesor.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 12))
        self.nombreEntryBMProfesor.insert(0, 'Nombre')
        self.nombreEntryBMProfesor.bind('<FocusIn>', on_enter)
        self.nombreEntryBMProfesor.bind('<FocusOut>', on_leave)
        self.nombreEntryBMProfesor.place(x=390,y=106)
        tk.Frame(masterGuarda, width=298, height=3, bg='#8CD0F7').place(x=387, y=133)
        def on_enter(e):
            name=self.apellidoEntryBMProfesor.get()
            if name == 'Apellido':
                self.apellidoEntryBMProfesor.delete(0, 'end')
    
        def on_leave(e):
            name=self.apellidoEntryBMProfesor.get()
            if name=='':
                self.apellidoEntryBMProfesor.insert(0, 'Apellido')
        self.apellidoEntryBMProfesor=tk.Entry(masterGuarda)
        self.apellidoEntryBMProfesor.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 12))
        self.apellidoEntryBMProfesor.insert(0, 'Apellido')
        self.apellidoEntryBMProfesor.bind('<FocusIn>', on_enter)
        self.apellidoEntryBMProfesor.bind('<FocusOut>', on_leave)
        self.apellidoEntryBMProfesor.place(x=390,y=176)
        tk.Frame(masterGuarda, width=298, height=3, bg='#8CD0F7').place(x=387, y=206)
        
        def on_enter(e):
            name=self.gmailEntryBMProfesor.get()
            if name == 'Correo':
                self.gmailEntryBMProfesor.delete(0, 'end')
    
        def on_leave(e):
            name=self.gmailEntryBMProfesor.get()
            if name=='':
                self.gmailEntryBMProfesor.insert(0, 'Correo')
        self.gmailEntryBMProfesor=tk.Entry(masterGuarda)
        self.gmailEntryBMProfesor.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 12))
        self.gmailEntryBMProfesor.insert(0, 'Correo')
        self.gmailEntryBMProfesor.bind('<FocusIn>', on_enter)
        self.gmailEntryBMProfesor.bind('<FocusOut>', on_leave)
        self.gmailEntryBMProfesor.place(x=390,y=246)
        tk.Frame(masterGuarda, width=298, height=3, bg='#8CD0F7').place(x=387, y=276)
        
        def on_enter(e):
            name=self.cuilEntryBMProfesor.get()
            if name == 'Cuil':
                self.cuilEntryBMProfesor.delete(0, 'end')
    
        def on_leave(e):
            name=self.cuilEntryBMProfesor.get()
            if name=='':
                self.cuilEntryBMProfesor.insert(0, 'Cuil')
        self.cuilEntryBMProfesor=tk.Entry(masterGuarda)
        self.cuilEntryBMProfesor.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 12))
        self.cuilEntryBMProfesor.insert(0, 'Cuil')
        self.cuilEntryBMProfesor.bind('<FocusIn>', on_enter)
        self.cuilEntryBMProfesor.bind('<FocusOut>', on_leave)
        self.cuilEntryBMProfesor.place(x=390,y=316)
        tk.Frame(masterGuarda, width=298, height=3, bg='#8CD0F7').place(x=387, y=346)
        # self.horarioLabel=tk.Label(masterGuarda,text="Turno:")
        # self.horarioLabel.config(bg="#8CD0F7",padx=15,font=("Arial", 15))
        # self.horarioLabel.place(x=50,y=300)
        # self.opcionHorario=tk.StringVar()
        # horarios=("Mañana","Tarde")
        # self.comboboxHorario=ttk.Combobox(masterGuarda, 
        #                           width=20, 
        #                           textvariable=self.opcionHorario, 
        #                           values=horarios)        
        # self.comboboxHorario.place(x=150,y=306)
        # self.comboboxHorario.current(0)
        self.botonBorrarProfesor=tk.Button(masterGuarda,width=20, pady=7, command=self.baja_profesor, text='Borrar Profesor', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.botonBorrarProfesor.place(x=250,y=370)
        self.botonNuevoProfesor=tk.Button(masterGuarda,command=self.ActualizarProfesor,width=20, pady=7, text='Guardar Profesor', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.botonNuevoProfesor.place(x=680,y=370)
        
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
        database= dbProfesores("localhost","root","test")
        try:
            int(cuilProfesor)
            if nombreProfesor != "Nombre" and apellidoProfesor != "Apellido" and cuilProfesor != "Cuil" and correoProfesor != "Correo" and es_correo_valido(correoProfesor) == True:
                if nombreProfesor != "" and apellidoProfesor != "" and cuilProfesor != "" and correoProfesor != "" and es_correo_valido(correoProfesor) == True:
                    database.crear_profesor(cuilProfesor,nombreProfesor,apellidoProfesor,correoProfesor)
                    messagebox.showinfo("","Profesor Cargado con Exito")
                    self.cargar_listaprofesores()
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
        # if nombreProfesor != "Nombre" or "" and apellidoProfesor != "Apellido" or "":
        #     ultimoId = len(self.__class__.lista)
        #     self.__class__.lista.append( Alumno(str(ultimoId), profesorCompleto))
        # else:
        #     messagebox.showerror("Error de entrada de Profesor","Falta un Nombre o Apellido")
    
    
    def ActualizarProfesor(self):
        selector = self.listboxBMProfesor.curselection()
        nombreProfesor= self.nombreEntryBMProfesor.get().strip()
        apellidoProfesor=self.apellidoEntryBMProfesor.get().strip()
        cuilProfesor=self.cuilEntryBMProfesor.get().strip()
        correoProfesor=self.gmailEntryBMProfesor.get().strip()
        profesorCompleto=nombreProfesor+" "+ apellidoProfesor
        def es_correo_valido(correo):
            if '@' in correo:
                return True
            else:
                return False
        print(profesorCompleto)
        print(correoProfesor)
        print(es_correo_valido(correoProfesor))
        if selector != ():
            idProfesor = self.listaprofesores[selector[0]].id
        try:
            database= dbProfesores("localhost","root","test")
            int(cuilProfesor)
            if nombreProfesor != "Nombre" and apellidoProfesor != "Apellido" and cuilProfesor != "Cuil" and correoProfesor != "Correo" and es_correo_valido(correoProfesor) == True:
                if nombreProfesor != "" and apellidoProfesor != "" and cuilProfesor != "" and correoProfesor != "" and es_correo_valido(correoProfesor) == True:
                    database.actualizar_profesor(cuilProfesor,nombreProfesor,apellidoProfesor,correoProfesor,idProfesor)
                    messagebox.showinfo("","Docente actualizado con Exito")
                    self.cargar_listaprofesores()
                    self.nombreEntryBMProfesor.delete(0,'end')
                    self.apellidoEntryBMProfesor.delete(0,'end')
                    self.gmailEntryBMProfesor.delete(0,'end')
                    self.cuilEntryBMProfesor.delete(0,'end')
                    self.nombreEntryBMProfesor.insert(0, 'Nombre')
                    self.apellidoEntryBMProfesor.insert(0, 'Apellido')
                    self.gmailEntryBMProfesor.insert(0, 'Correo')
                    self.cuilEntryBMProfesor.insert(0, 'Cuil')
            else:
                messagebox.showerror("Error de entrada de Profesor","Falta un Dato o es Incorrecto")
        except ValueError:
            messagebox.showerror("Error de Entrada","CUIL invalido")
        # if nombreProfesor != "Nombre" or "" and apellidoProfesor != "Apellido" or "":
        #     ultimoId = len(self.__class__.lista)
        #     self.__class__.lista.append( Alumno(str(ultimoId), profesorCompleto))
        # else:
        #     messagebox.showerror("Error de entrada de Profesor","Falta un Nombre o Apellido")
    
    
    def baja_profesor(self):
        selector = self.listboxBMProfesor.curselection()
        if selector != ():
            index = selector[0]
            respuesta = messagebox.askyesno(title='confirmacion',
                    message=f'¿Estas seguro de querer borrar a {self.listaprofesores[index].nombre} {self.listaprofesores[index].apellido}?')
            if respuesta:
                database = dbProfesores("localhost","root","test")
                idProfesor = self.listaprofesores[index].id
                database.baja_profesor(idProfesor)
                self.nombreEntryBMProfesor.delete(0,'end')
                self.apellidoEntryBMProfesor.delete(0,'end')
                self.gmailEntryBMProfesor.delete(0,'end')
                self.cuilEntryBMProfesor.delete(0,'end')
                self.nombreEntryBMProfesor.insert(0, 'Nombre')
                self.apellidoEntryBMProfesor.insert(0, 'Apellido')
                self.gmailEntryBMProfesor.insert(0, 'Correo')
                self.cuilEntryBMProfesor.insert(0, 'Cuil')
                self.cargar_listaprofesores()
            else:
                return
        else:
            messagebox.showerror("","Seleccione a un profesor")
    
    def evento_clickProfesor(self,event):
        selector = event.widget.curselection()
        print(selector)
        if selector != ():
            index = selector[0]
            self.nombreEntryBMProfesor.delete(0,'end')
            self.apellidoEntryBMProfesor.delete(0,'end')
            self.gmailEntryBMProfesor.delete(0,'end')
            self.cuilEntryBMProfesor.delete(0,'end')
            self.nombreEntryBMProfesor.insert(0,self.listaprofesores[index].nombre)
            self.apellidoEntryBMProfesor.insert(0,self.listaprofesores[index].apellido)
            self.gmailEntryBMProfesor.insert(0,self.listaprofesores[index].mail)
            self.cuilEntryBMProfesor.insert(0,self.listaprofesores[index].cuil)
        print(index)
    
    
    def cargar_listaprofesores(self):
        self.listboxBMProfesor.delete(0, tk.END)
        profesores = dbProfesores("localhost","root","test").buscar_listaprofesor()
        self.listaprofesores=[]
        index=0
        for profesor in profesores:
            self.listaprofesores.append(Profesor(profesor[0],profesor[1],profesor[2],profesor[3],profesor[4],profesor[5]))
            self.listboxBMProfesor.insert(index,profesor[2] + " " + profesor[3])
            print(self.listaprofesores)
            index = index + 1

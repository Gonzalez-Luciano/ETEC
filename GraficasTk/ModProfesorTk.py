from ast import Delete
import tkinter as tk
from tkinter import Label, Widget, ttk, END
from tkinter import messagebox,Menubutton
from Profesor import *
from db.dbProfesores import dbProfesores


class ModProfesorTk():
#<-------------------------------------------Funcion para crear interfaz grafica de la pestaña GuardarProfesor------------------------>  

    def MasterBMProfesor(self,masterGuarda):
        self.buscarImagenProfesor=tk.PhotoImage(file="imagenesApp/boton-busqueda-profesor.png")
        self.titulo=tk.Label(masterGuarda,text="Información General")
        self.titulo.config(bg="#FFF",font=("Arial", 20))
        self.titulo.place(x=320,y=5)
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
        self.buttonBuscadorProfesor=tk.Button(masterGuarda,image=self.buscarImagenProfesor,command=self.buscarProfesor,width=25,height=25,bg='#57a1f9', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
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
        self.botonBorrarProfesor=tk.Button(masterGuarda,width=20, pady=7, command=self.baja_profesor, text='Borrar Profesor', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.botonBorrarProfesor.place(x=250,y=370)
        self.botonNuevoProfesor=tk.Button(masterGuarda,command=self.ActualizarProfesor,width=20, pady=7, text='Guardar Profesor', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.botonNuevoProfesor.place(x=680,y=370)
        
        
        #Función para buscar al profesor por el cuil
    def buscarProfesor(self):
            cuil = self.entryBuscadorBMProfesor.get()
            print(cuil)
            try:
                int(cuil)
                for index in range(self.listboxBMProfesor.size()):
                    profesorBuscado = self.listaprofesores[index].cuil
                    self.listboxBMProfesor.selection_clear(0, tk.END)
                    if cuil == profesorBuscado:
                        self.listboxBMProfesor.selection_set(index)
                        return
                else:
                    self.entryBuscadorBMProfesor.delete(0,'end')
                    self.entryBuscadorBMProfesor.insert(0,' Buscar')
                    messagebox.showinfo("","No se encontro el profesor")
            except ValueError:
                self.entryBuscadorBMProfesor.delete(0,'end')
                self.entryBuscadorBMProfesor.insert(0,' Buscar')
                messagebox.showerror("","ingrese un cuil valido")
#<-------------------------------------------Funcion para actualizar al profesor en base de datos (más info en dbProfesores.py)------------------------>  

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
            database= dbProfesores("localhost","EtecUser","tkinterdatabase","1234")
            int(cuilProfesor)
            if nombreProfesor != "Nombre" and apellidoProfesor != "Apellido" and cuilProfesor != "Cuil" and correoProfesor != "Correo" and es_correo_valido(correoProfesor) == True:
                if nombreProfesor != "" and apellidoProfesor != "" and cuilProfesor != "" and correoProfesor != "" and es_correo_valido(correoProfesor) == True:
                    database.actualizar_profesor(cuilProfesor,nombreProfesor,apellidoProfesor,correoProfesor,idProfesor)
                    messagebox.showinfo("","Docente actualizado con Exito")
                    self.cargar_listaprofesores()
                    self.cargar_listboxprofesores()
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
            
            
#<-------------------------------------------Funcion para dar de baja al profesor en base de datos (más info en dbProfesores.py)------------------------>  

    def baja_profesor(self):
        selector = self.listboxBMProfesor.curselection()
        if selector != ():
            index = selector[0]
            respuesta = messagebox.askyesno(title='confirmacion',
                    message=f'¿Estas seguro de querer borrar a {self.listaprofesores[index].nombre} {self.listaprofesores[index].apellido}?')
            if respuesta:
                database = dbProfesores("localhost","EtecUser","tkinterdatabase","1234")
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
                self.cargar_listboxprofesores()
            else:
                return
        else:
            messagebox.showerror("","Seleccione a un profesor")
    
    
#<-------------------------------------------Funcion para autocompletar los datos en cada Entry de los profesores------------------------>  

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
        profesores = dbProfesores("localhost","EtecUser","tkinterdatabase","1234").buscar_listaprofesor()
        self.listaprofesores=[]
        index=0
        for profesor in profesores:
            self.listaprofesores.append(Profesor(profesor[0],profesor[1],profesor[2],profesor[3],profesor[4],profesor[5]))
            self.listboxBMProfesor.insert(index,profesor[2] + " " + profesor[3])
            print(self.listaprofesores)
            index = index + 1
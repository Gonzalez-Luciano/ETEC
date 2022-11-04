import tkinter as tk
from tkinter import Label, Widget, ttk, END
from tkinter import messagebox,Menubutton
from Materia import *
from db.dbMaterias import dbMaterias


class MateriaTk():
    
#<--------------------------------------------Funcion para crear interfaz grafica de la pestaña CargarMateria------------------------------->

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
            name=self.descripcionEntryMateria.get()
            if name == 'Descripción':
                self.descripcionEntryMateria.delete(0, 'end')

        def on_leave(e):
            name=self.descripcionEntryMateria.get()
            if name=='':
                self.descripcionEntryMateria.insert(0, 'Descripción')
        self.descripcionEntryMateria=tk.Entry(masterCarga)
        self.descripcionEntryMateria.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
        self.descripcionEntryMateria.insert(0, 'Descripción')
        self.descripcionEntryMateria.bind('<FocusIn>', on_enter)
        self.descripcionEntryMateria.bind('<FocusOut>', on_leave)
        self.descripcionEntryMateria.place(x=320,y=196)
        tk.Frame(masterCarga, width=300, height=3, bg='#8CD0F7').place(x=315, y=226)
        self.botonNuevaMateria=tk.Button(masterCarga,command=self.GuardarNuevaMateria,width=20, pady=7, text='Cargar Materia', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
        self.botonNuevaMateria.place(x=680,y=370)
        
#<-----------------------------------------Funcion para crear interfaz grafica de la pestaña GuardarAlumno---------------------------------->  

    def MasterBMMateria(self, masterGuarda):
            self.buscarImagenMateria=tk.PhotoImage(file="imagenesApp/boton-busqueda-materia.png")
            self.titulo=tk.Label(masterGuarda,text="Información General")
            self.titulo.config(bg="#FFF",font=("Arial", 20))
            self.titulo.place(x=320,y=5)
            # self.textoEjemplo= tk.StringVar()
            # self.textoEjemplo.set("Nombre de Alumno")
            self.entryBuscadorBMMateria=tk.Entry(masterGuarda, width=16, fg='black', border=0, font=('Microsoft Yahei UI', 12))
            self.entryBuscadorBMMateria.insert(0," Buscar")
            self.entryBuscadorBMMateria.place(x=50,y=76)
            #Función para crear y borrar el pre-texto de entryBuscador
            def on_enter(e):
                name=self.entryBuscadorBMMateria.get()
                if name == ' Buscar':
                    self.entryBuscadorBMMateria.delete(0, 'end')

            def on_leave(e):
                name=self.entryBuscadorBMMateria.get()
                if name=='':
                    self.entryBuscadorBMMateria.insert(0, ' Buscar')
            self.entryBuscadorBMMateria.bind('<FocusIn>', on_enter)
            self.entryBuscadorBMMateria.bind('<FocusOut>', on_leave)
            self.buttonBuscadorMateria=tk.Button(masterGuarda,image=self.buscarImagenMateria,width=25,height=25,bg='#57a1f9', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.buttonBuscadorMateria.place(x=206,y=76)
            
            #Scrollbar , Listbox y Combobox
            self.scrollBMMateria = tk.Scrollbar(masterGuarda, orient=tk.VERTICAL)
            self.listboxBMMateria=tk.Listbox(masterGuarda, selectmode=tk.SINGLE,width=30,height=17 ,yscrollcommand=self.scrollBMMateria.set,bg="#FFF",exportselection=False)
            self.listboxBMMateria.place(x=50,y=100)
            self.listboxBMMateria.bind("<<ListboxSelect>>",self.evento_clickMateria)
            self.scrollBMMateria.configure(command=self.listboxBMMateria.yview)        
            self.scrollBMMateria.place(x=176,y=100)  
            self.botonBorrarMateria=tk.Button(masterGuarda,width=20, pady=7, command=self.baja_materia, text='Borrar Materia', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.botonBorrarMateria.place(x=250,y=370)
            self.botonActualizarMateria=tk.Button(masterGuarda,width=20, pady=7, command=self.ActualizarMateria, text='Guardar Materia', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.botonActualizarMateria.place(x=680,y=370)
            def on_enter(e):
                name=self.nombreEntryBMMateria.get()
                if name == 'Nombre':
                    self.nombreEntryBMMateria.delete(0, 'end')
        
            def on_leave(e):
                name=self.nombreEntryBMMateria.get()
                if name=='':
                    self.nombreEntryBMMateria.insert(0, 'Nombre')
            self.nombreEntryBMMateria=tk.Entry(masterGuarda)
            self.nombreEntryBMMateria.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
            self.nombreEntryBMMateria.insert(0, 'Nombre')
            self.nombreEntryBMMateria.bind('<FocusIn>', on_enter)
            self.nombreEntryBMMateria.bind('<FocusOut>', on_leave)
            self.nombreEntryBMMateria.place(x=390,y=106)
            tk.Frame(masterGuarda, width=300, height=3, bg='#8CD0F7').place(x=385, y=136)
            def on_enter(e):
                name=self.descripcionEntryBMMateria.get()
                if name == 'Descripción':
                    self.descripcionEntryBMMateria.delete(0, 'end')
        
            def on_leave(e):
                name=self.descripcionEntryBMMateria.get()
                if name=='':
                    self.descripcionEntryBMMateria.insert(0, 'Descripción')
            self.descripcionEntryBMMateria=tk.Entry(masterGuarda)
            self.descripcionEntryBMMateria.config(width=25, fg='black', border=0, bg="#FFF", font=('Microsoft Yahei UI', 15))
            self.descripcionEntryBMMateria.insert(0, 'Descripción')
            self.descripcionEntryBMMateria.bind('<FocusIn>', on_enter)
            self.descripcionEntryBMMateria.bind('<FocusOut>', on_leave)
            self.descripcionEntryBMMateria.place(x=390,y=196)
            tk.Frame(masterGuarda, width=300, height=3, bg='#8CD0F7').place(x=385, y=226)
#<-----------------------Función para guardar nuevas materias en base de datos (más info en dbMaterias.py)----------------------->
    def GuardarNuevaMateria(self):
        nombreMateria=self.nombreEntryMateria.get().strip()
        descripMateria=self.descripcionEntryMateria.get().strip()
        database= dbMaterias("localhost","root","test")
        if nombreMateria != "Nombre" and descripMateria != "Descripción":
            if nombreMateria != "" and descripMateria != "":
                database.crear_materia(nombreMateria,descripMateria)
                messagebox.showinfo("","Materia Cargada con Exito")
                self.cargar_listamaterias()
                self.nombreEntryMateria.delete(0,'end')
                self.descripcionEntryMateria.delete(0,'end')
                self.nombreEntryMateria.insert(0, 'Nombre')
                self.descripcionEntryMateria.insert(0, 'Descripción')
        else:
            messagebox.showerror("Error de entrada de Materia","Falta un Nombre o Descripción")
   
    def ActualizarMateria(self):
        selector = self.listboxBMMateria.curselection()
        nombreMateria=self.nombreEntryBMMateria.get().strip()
        descripMateria=self.descripcionEntryBMMateria.get().strip()
        if selector != ():
            idMateria = self.listamaterias[selector[0]].id
            database= dbMaterias("localhost","root","test")
            if nombreMateria != "Nombre" and descripMateria != "Descripción":
                if nombreMateria != "" and descripMateria != "":
                    database.actualizar_materia(nombreMateria,descripMateria,idMateria)
                    messagebox.showinfo("","Materia actualizada con Exito")
                    self.nombreEntryBMMateria.delete(0,'end')
                    self.descripcionEntryBMMateria.delete(0,'end')
                    self.nombreEntryBMMateria.insert(0, 'Nombre')
                    self.descripcionEntryBMMateria.insert(0, 'Descripción')
                    self.cargar_listamaterias()
            else:
                messagebox.showerror("Error de entrada de Materia","Falta un Nombre o Descripción")
        else:
            messagebox.showwarning("","Seleccione un Alumno")
            return
           
    
    def baja_materia(self):
        selector = self.listboxBMMateria.curselection()
        if selector != ():
            index = selector[0]
            respuesta = messagebox.askyesno(title='confirmacion',
                    message=f'¿Estas seguro de querer borrar la materia: {self.listamaterias[index].nombre} ?')
            if respuesta:
                database = dbMaterias("localhost","root","test")
                idMateria = self.listamaterias[index].id
                database.baja_materia(idMateria)
                self.nombreEntryBMMateria.delete(0,'end')
                self.descripcionEntryBMMateria.delete(0,'end')
                self.nombreEntryBMMateria.insert(0, 'Nombre')
                self.descripcionEntryBMMateria.insert(0, 'Descripción')
                self.cargar_listamaterias()
            else:
                return
        else:
            messagebox.showerror("","Seleccione a un profesor")
    
    
    def evento_clickMateria(self,event):
        selector = event.widget.curselection()
        print(selector)
        if selector != ():
            index = selector[0]
            self.nombreEntryBMMateria.delete(0,'end')
            self.descripcionEntryBMMateria.delete(0,'end')
            self.nombreEntryBMMateria.insert(0,self.listamaterias[index].nombre)
            self.descripcionEntryBMMateria.insert(0,self.listamaterias[index].descripcion)
        print(index)
            
    def cargar_listamaterias(self):
        self.listboxBMMateria.delete(0, tk.END)
        materias = dbMaterias("localhost","root","test").buscar_listamateria()
        self.listamaterias=[]
        index=0
        for materia in materias:
            self.listamaterias.append(Materia(materia[0],materia[1],materia[2],materia[3]))
            self.listboxBMMateria.insert(index,materia[1])
            print(self.listamaterias)
            index = index + 1
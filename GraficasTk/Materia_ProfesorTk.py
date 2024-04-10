import tkinter as tk
from tkinter import Label, Widget, ttk, END
from tkinter import messagebox,Menubutton
from Materia import *
from Profesor import *
from db.dbProfesores import dbProfesores
from db.dbMaterias import dbMaterias
from db.dbProfesor_Materia import dbProfesor_Materia

class Materia_ProfesorTk():
    
#<-----------------------------------------Funcion para crear interfaz grafica de la pestaña Materia_Alumno---------------------------------->  
   
    def MasterMateria_Profesor(self, masterGuarda):
            self.buscarImagenMateria_Profesor=tk.PhotoImage(file="imagenesApp/boton-busqueda-alumno.png")
            self.tituloMateria_Profesor=tk.Label(masterGuarda,text="Modificar Profesor")
            self.tituloMateria_Profesor.config(bg="#FFF",font=("Arial", 20))
            self.tituloMateria_Profesor.place(x=320,y=5)
            # self.textoEjemplo= tk.StringVar()
            # self.textoEjemplo.set("Nombre de Alumno")
            self.entryBuscadorMateria_Profesor=tk.Entry(masterGuarda, width=16, fg='black', border=0, font=('Microsoft Yahei UI', 12))
            self.entryBuscadorMateria_Profesor.insert(0," Buscar")
            self.entryBuscadorMateria_Profesor.place(x=50,y=76)
            def on_enter(e):
                name=self.entryBuscadorMateria_Profesor.get()
                if name == ' Buscar':
                    self.entryBuscadorMateria_Profesor.delete(0, 'end')

            def on_leave(e):
                name=self.entryBuscadorMateria_Profesor.get()
                if name=='':
                    self.entryBuscadorMateria_Profesor.insert(0, ' Buscar')
            self.entryBuscadorMateria_Profesor.bind('<FocusIn>', on_enter)
            self.entryBuscadorMateria_Profesor.bind('<FocusOut>', on_leave)
            self.buttonBuscadorMateria_Profesor=tk.Button(masterGuarda,image=self.buscarImagenMateria_Profesor,command=self.buscarProfesor_Materia,width=25,height=25,bg='#57a1f9', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.buttonBuscadorMateria_Profesor.place(x=206,y=76)
            #Scrollbar , Listbox y Combobox
            self.scrollProfesor = tk.Scrollbar(masterGuarda, orient=tk.VERTICAL)
            self.listboxProfesores=tk.Listbox(masterGuarda, selectmode=tk.SINGLE,width=30,height=17 ,yscrollcommand=self.scrollProfesor.set,bg="#FFF",exportselection=False)
            self.listboxProfesores.place(x=50,y=100)
            self.listboxProfesores.bind("<<ListboxSelect>>",lambda e:self.evento_clickMostrarMateria_Profesor())
            self.scrollMateria = tk.Scrollbar(masterGuarda, orient=tk.VERTICAL)
            self.listboxMaterias_Profesor=tk.Listbox(masterGuarda, selectmode=tk.SINGLE,width=30,height=17 ,yscrollcommand=self.scrollMateria.set,bg="#FFF",exportselection=False)
            self.listboxMaterias_Profesor.place(x=630,y=100)
            self.labelMateria=tk.Label(masterGuarda, width=16,bg='#FFF', fg='black', border=0, font=('Microsoft Yahei UI', 12),text="Materias agregadas:")
            self.labelMateria.place(x=630,y=76)
            self.scrollProfesor.configure(command=self.listboxProfesores.yview)        
            self.scrollProfesor.place(x=176,y=100)     
            self.labelAsignatura=ttk.Label(masterGuarda, text="Seleccione la materia:")
            self.labelAsignatura.place(x=270, y=100)
            self.labelAsignatura.config(background="#FFF",font=('Microsoft Yahei UI', 10))
            self.opcionMateria=tk.StringVar()
            self.comboboxMateria_Profesor=ttk.Combobox(masterGuarda, 
                                      width=20, 
                                      textvariable=self.opcionMateria,
                                      state="readonly")
            self.comboboxMateria_Profesor.place(x=427, y=101)
            self.comboboxMateria_Profesor.configure(font=('Microsoft Yahei UI', 9))
            self.botonBorrarProfesor=tk.Button(masterGuarda,width=20, pady=7, command=self.bajaProfesor_Materia, text='Borrar Materia', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.botonBorrarProfesor.place(x=668,y=380)
            self.botonAgregarMateria_Profesor=tk.Button(masterGuarda,width=20, pady=7, command=self.cargarProfesor_Materia, text='Agregar Materia', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.botonAgregarMateria_Profesor.place(x=270,y=200)

    #Función para buscar al profesor por el cuil
    def buscarProfesor_Materia(self):
            cuil = self.entryBuscadorMateria_Profesor.get()
            print(cuil)
            try:
                int(cuil)
                for index in range(self.listboxProfesores.size()):
                    profesorBuscado = self.listaprofesores1[index].cuil
                    self.listboxProfesores.selection_clear(0, tk.END)
                    if cuil == profesorBuscado:
                        self.listboxProfesores.selection_set(index)
                        return
                else:
                    self.entryBuscadorMateria_Profesor.delete(0,'end')
                    self.entryBuscadorMateria_Profesor.insert(0,' Buscar')
                    messagebox.showinfo("","No se encontro el profesor")
            except ValueError:
                self.entryBuscadorMateria_Profesor.delete(0,'end')
                self.entryBuscadorMateria_Profesor.insert(0,' Buscar')
                messagebox.showerror("","ingrese un cuil valido")    


    def evento_clickMostrarMateria_Profesor(self):
        selector = self.listboxProfesores.curselection()
        self.listboxMaterias_Profesor.delete(0, tk.END)
        if selector != ():
            self.listaProfesor_Materia=[]
            index = 0
            indexProfesor = selector[0]
            idProfesor= self.listaprofesores1[indexProfesor].id
            database = dbProfesor_Materia("localhost","EtecUser","tkinterdatabase","1234")
            materias = database.mostrarMateria(idProfesor)
            for materia in materias:
                self.listaProfesor_Materia.append(Materia(materia[0],materia[1],materia[2],materia[3]))
                self.listboxMaterias_Profesor.insert(index,materia[1])
                index = index + 1
                
    def cargar_listboxprofesores(self):
        self.listboxProfesores.delete(0, tk.END)
        profesores = dbProfesores("localhost","EtecUser","tkinterdatabase","1234").buscar_listaprofesor()
        self.listaprofesores1=[]
        index=0
        for profesor in profesores:
            self.listaprofesores1.append(Profesor(profesor[0],profesor[1],profesor[2],profesor[3],profesor[4],profesor[5]))
            self.listboxProfesores.insert(index,profesor[2] + " " + profesor[3])
            print(self.listaprofesores1)
            index = index + 1
            
    def cargar_comboxmateriasProfesores(self):
            materias = dbMaterias("localhost","EtecUser","tkinterdatabase","1234").buscar_listamateria()
            self.values=[]
            self.listamaterias_profesor=[]
            for materia in materias:
                self.listamaterias_profesor.append(Materia(materia[0],materia[1],materia[2],materia[3]))
                self.values.append(materia[1])
                self.comboboxMateria_Profesor["values"] = self.values
                self.comboboxMateria_Profesor.current(0)
    
    def cargarProfesor_Materia(self):
        selector = self.listboxProfesores.curselection()
        if selector != ():
            database= dbProfesor_Materia("localhost","EtecUser","tkinterdatabase","1234")
            indexProfesor = selector[0]
            indexMateria = self.comboboxMateria_Profesor.current()
            idMateria = self.listamaterias_profesor[indexMateria].id
            idProfesor= self.listaprofesores1[indexProfesor].id
            messagebox.showinfo("","Materia agregada con Exito"
                                if database.agregarProfesor_Materia(idProfesor,idMateria)
                                else "El profesor ya tiene esta materia")  
            self.evento_clickMostrarMateria_Profesor()
            
        else:
            messagebox.showwarning("","Por favor, seleccione un profesor")
    
    
    def bajaProfesor_Materia(self):
        selectorProfesor = self.listboxProfesores.curselection()
        selectorMateria = self.listboxMaterias_Profesor.curselection()
        
        if selectorProfesor != () and selectorMateria != ():
            database = dbProfesor_Materia("localhost","EtecUser","tkinterdatabase","1234")
            indexProfesor = selectorProfesor[0]
            indexMateria = selectorMateria[0]
            idMateria = self.listaProfesor_Materia[indexMateria].id
            idProfesor= self.listaprofesores1[indexProfesor].id
            messagebox.showinfo("","Materia eliminada con Exito"
                                if database.bajaProfesor_Materia(idProfesor,idMateria)
                                else "error")  
            self.evento_clickMostrarMateria_Profesor()
            
        else:
            messagebox.showwarning("","Por favor, seleccione un alumno o materia")
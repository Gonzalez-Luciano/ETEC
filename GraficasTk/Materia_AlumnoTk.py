import tkinter as tk
from tkinter import Label, Widget, ttk, END
from tkinter import messagebox,Menubutton
from Materia import *
from Alumno import *
from db.dbAlumnos import dbAlumnos
from db.dbMaterias import dbMaterias
from db.dbAlumno_Materia import dbAlumno_Materia

class Materia_AlumnoTk():
    
#<-----------------------------------------Funcion para crear interfaz grafica de la pestaña Materia_Alumno---------------------------------->  
   
    def MasterMateria_Alumno(self, masterGuarda):
            self.buscarImagenMateria_Alumno=tk.PhotoImage(file="imagenesApp/boton-busqueda-alumno.png")
            self.tituloMateria_Alumno=tk.Label(masterGuarda,text="Modificar Alumno")
            self.tituloMateria_Alumno.config(bg="#FFF",font=("Arial", 20))
            self.tituloMateria_Alumno.place(x=320,y=5)
            # self.textoEjemplo= tk.StringVar()
            # self.textoEjemplo.set("Nombre de Alumno")
            self.entryBuscadorMateria_Alumno=tk.Entry(masterGuarda, width=16, fg='black', border=0, font=('Microsoft Yahei UI', 12))
            self.entryBuscadorMateria_Alumno.insert(0," Buscar")
            self.entryBuscadorMateria_Alumno.place(x=50,y=76)
            def on_enter(e):
                name=self.entryBuscadorMateria_Alumno.get()
                if name == ' Buscar':
                    self.entryBuscadorMateria_Alumno.delete(0, 'end')

            def on_leave(e):
                name=self.entryBuscadorMateria_Alumno.get()
                if name=='':
                    self.entryBuscadorMateria_Alumno.insert(0, ' Buscar')
            self.entryBuscadorMateria_Alumno.bind('<FocusIn>', on_enter)
            self.entryBuscadorMateria_Alumno.bind('<FocusOut>', on_leave)
            self.buttonBuscadorMateria_Alumno=tk.Button(masterGuarda,image=self.buscarImagenMateria_Alumno,command=self.buscarAlumno_Materia,width=25,height=25,bg='#57a1f9', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.buttonBuscadorMateria_Alumno.place(x=206,y=76)
            
            #Scrollbar , Listbox y Combobox
            self.scrollMateria = tk.Scrollbar(masterGuarda, orient=tk.VERTICAL)
            self.listboxAlumnos=tk.Listbox(masterGuarda, selectmode=tk.SINGLE,width=30,height=17 ,yscrollcommand=self.scrollMateria.set,bg="#FFF",exportselection=False)
            self.listboxAlumnos.place(x=50,y=100)
            self.listboxAlumnos.bind("<<ListboxSelect>>",lambda e:self.evento_clickMostrarMateria())
            self.listboxMaterias=tk.Listbox(masterGuarda, selectmode=tk.SINGLE,width=30,height=17 ,yscrollcommand=self.scrollMateria.set,bg="#FFF",exportselection=False)
            self.listboxMaterias.place(x=630,y=100)
            self.labelMateria=tk.Label(masterGuarda, width=16,bg='#FFF', fg='black', border=0, font=('Microsoft Yahei UI', 12),text="Materias agregadas:")
            self.labelMateria.place(x=630,y=76)
            self.scrollMateria.configure(command=self.listboxAlumnos.yview)        
            self.scrollMateria.place(x=176,y=100)     
            self.labelAsignatura=ttk.Label(masterGuarda, text="Seleccione la materia:")
            self.labelAsignatura.place(x=270, y=97)
            self.labelAsignatura.config(background="#FFF",font=('Microsoft Yahei UI', 10))
            self.opcionMateria=tk.StringVar()
            self.comboboxMateria=ttk.Combobox(masterGuarda, 
                                      width=20, 
                                      textvariable=self.opcionMateria,
                                      state="readonly")
            self.comboboxMateria.place(x=427, y=101)
            self.comboboxMateria.configure(font=('Microsoft Yahei UI', 9))
            self.botonBorrarAlumno=tk.Button(masterGuarda,width=20, pady=7, command=self.bajaAlumno_Materia, text='Borrar Materia', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.botonBorrarAlumno.place(x=668,y=380)
            self.botonAgregarMateria=tk.Button(masterGuarda,width=20, pady=7, command=self.cargarAlumno_Materia, text='Agregar Materia', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed')
            self.botonAgregarMateria.place(x=270,y=200)

    #Función para buscar al alumno por el cuil
    def buscarAlumno_Materia(self):
        cuil = self.entryBuscadorMateria_Alumno.get()
        print(cuil)
        try:
            int(cuil)
            for index in range(self.listboxAlumnos.size()):
                alumnoBuscado = self.listalumnos1[index].cuil
                self.listboxAlumnos.selection_clear(0, tk.END)
                if cuil == alumnoBuscado:
                    self.listboxAlumnos.selection_set(index)
                    return
            else:
                self.entryBuscadorMateria_Alumno.delete(0,'end')
                self.entryBuscadorMateria_Alumno.insert(0,' Buscar')
                messagebox.showinfo("","No se encontro el alumno")
        except ValueError:
            self.entryBuscadorMateria_Alumno.delete(0,'end')
            self.entryBuscadorMateria_Alumno.insert(0,' Buscar')
            messagebox.showerror("","ingrese un cuil valido")
    
    
    def evento_clickMostrarMateria(self):
        selector = self.listboxAlumnos.curselection()
        self.listboxMaterias.delete(0, tk.END)
        if selector != ():
            self.listaAlumno_materia=[]
            index = 0
            indexAlumno = selector[0]
            idAlumno= self.listalumnos1[indexAlumno].id
            database = dbAlumno_Materia("localhost","EtecUser","tkinterdatabase","1234")
            materias = database.mostrarMateria(idAlumno)
            for materia in materias:
                self.listaAlumno_materia.append(Materia(materia[0],materia[1],materia[2],materia[3]))
                self.listboxMaterias.insert(index,materia[1])
                index = index + 1
                
    def cargar_listboxalumnos(self):
        self.listboxAlumnos.delete(0, tk.END)
        alumnos = dbAlumnos("localhost","EtecUser","tkinterdatabase","1234").buscar_listalumno()
        self.listalumnos1=[]
        index=0
        for alumno in alumnos:
            self.listalumnos1.append(Alumno(alumno[0],alumno[1],alumno[2],alumno[3],alumno[4]))
            self.listboxAlumnos.insert(index,alumno[2] + " " + alumno[3])
            print(self.listalumnos1)
            index = index + 1
            
    def cargar_comboxmaterias(self):
            materias = dbMaterias("localhost","EtecUser","tkinterdatabase","1234").buscar_listamateria()
            self.values=[]
            self.listamaterias1=[]
            for materia in materias:
                self.listamaterias1.append(Materia(materia[0],materia[1],materia[2],materia[3]))
                self.values.append(materia[1])
                self.comboboxMateria["values"] = self.values
                self.comboboxMateria.current(0)
    
    def cargarAlumno_Materia(self):
        selector = self.listboxAlumnos.curselection()
        print(selector)
        if selector != ():
            database= dbAlumno_Materia("localhost","EtecUser","tkinterdatabase","1234")
            indexAlumno = selector[0]
            indexMateria = self.comboboxMateria.current()
            idMateria = self.listamaterias1[indexMateria].id
            idAlumno= self.listalumnos1[indexAlumno].id
            messagebox.showinfo("","Materia agregada con Exito"
                                if database.agregarAlumno_Materia(idAlumno,idMateria)
                                else "El alumno ya tiene esta materia")  
            self.evento_clickMostrarMateria()
            
        else:
            messagebox.showwarning("","Por favor, seleccione un alumno")
    
    
    def bajaAlumno_Materia(self):
        selectorAlumno = self.listboxAlumnos.curselection()
        selectorMateria = self.listboxMaterias.curselection()
        
        if selectorAlumno != () and selectorMateria != ():
            database = dbAlumno_Materia("localhost","EtecUser","tkinterdatabase","1234")
            indexAlumno = selectorAlumno[0]
            indexMateria = selectorMateria[0]
            idMateria = self.listaAlumno_materia[indexMateria].id
            idAlumno= self.listalumnos1[indexAlumno].id
            messagebox.showinfo("","Materia eliminada con Exito"
                                if database.bajaAlumno_Materia(idAlumno,idMateria)
                                else "error")  
            self.evento_clickMostrarMateria()
            
        else:
            messagebox.showwarning("","Por favor, seleccione un alumno o materia")
    

import tkinter as tk
from tkinter import Toplevel, messagebox
from tkinter import ttk
# from main1 import *
# from Alumno import *

root = tk.Tk()
root.title('Login')
root.geometry('925x600+400+300')
root.configure(bg="#fff")
root.resizable(False,False)

# def abriraplicacion():
#     ConsultaAlumnos()
    
def signin():
    username=user.get()
    password=code.get()
    
    if username =='admin' and password == '1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        
        tk.Label(screen, text='Hello Everyone!', bg='#fff', font=('Calibri(Body)', 50, 'bold' )).pack(expand=True)
        
        screen.mainloop()
        # abriraplicacion()
        

    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid", "Invalid username and password")
        
    elif password != '1234':
        messagebox.showerror("Invalid", "Invalid password")
     
    elif username != 'admin':
        messagebox.showerror("Invalid", "Invalid username")   
    
img = tk.PhotoImage(file='F:/Curso Programador/Aplicacion Edutec/login.png')
tk.Label(root, image=img, bg='white').place(x=50, y=50)

frame=tk.Frame(root, width=450, height=450, bg="white")
frame.place(x=480, y=70)

heading=tk.Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

#-----------------------------------
def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.inser(0, 'Username')
        
        
user = tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#---------------------------------------

def on_enter(e):
    code.config(show="•")
    code.delete(0, 'end')
    
def on_leave(e):
    name=code.get()
    if name=='':
        code.config(show="")
        code.inser(0, 'Password')
        
        
code = tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
#show="*"
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#------------------------------------

def on_enter(e):
    confirmation.config(show="•")
    confirmation.delete(0, 'end')
    
def on_leave(e):
    name=confirmation.get()
    if name=='':
        confirmation.config(show="")
        confirmation.inser(0, ' Confirm Password')

confirmation = tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))

confirmation.place(x=30, y=220)
confirmation.insert(0, 'Confirm Password')
confirmation.bind('<FocusIn>', on_enter)
confirmation.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)


#------------------------------------

def on_enter(e):
    mail.delete(0, 'end')
    
def on_leave(e):
    name=mail.get()
    if name=='':
        mail.inser(0, 'Mail')

mail = tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))

mail.place(x=30, y=290)
mail.insert(0, 'Mail')
mail.bind('<FocusIn>', on_enter)
mail.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=317)


#------------------------------------

tk.Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, cursor='hand2', activebackground='#8cb9ed', command=signin).place(x=35, y=350)
# label=tk.Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
# label.place(x=100, y=400)

# sign_up=tk.Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
# sign_up.place(x=215, y=900)
root.mainloop()
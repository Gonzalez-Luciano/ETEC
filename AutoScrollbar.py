from tkinter import *
   
class AutoScrollbar(Scrollbar): 
       
    
    
    def set(self, low, high): 
           
        if float(low) <= 0.0 and float(high) >= 1.0: 
               
            
            self.tk.call("grid", "remove", self) 
        else: 
            self.grid() 
        Scrollbar.set(self, low, high) 
       
    
    def pack(self, **kw): 
           
        
        raise (TclError,"pack cannot be used with \  this widget") 
       
    
    def place(self, **kw): 
           
        
        raise (TclError, "place cannot be used  with \  this widget") 
  
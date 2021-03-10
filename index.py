# █████╗ ██████╗ ███████╗
#██╔══██╗██╔══██╗██╔════╝
#███████║██████╔╝█████╗  
#██╔══██║██╔═══╝ ██╔══╝  
#██║  ██║██║     ███████╗
#╚═╝  ╚═╝╚═╝     ╚══════╝                     
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################


import tkinter as tk
from tkinter import Label, Menu, PhotoImage, mainloop, ttk
from src.indexview import IndexView
import webbrowser



class FrmParqueadero:

    def __init__(self):

        
        self.ventana= tk.Tk()
        self.ventana.geometry("1117x566")
        self.ventana.resizable(0,0)



        
        img = tk.PhotoImage(file=r"img\logo.png")
        img = img.subsample(2,2)
        self.lblA = ttk.Label(self.ventana,image=img,border=4)
        self.lblA.place(x=200,y=80,width=650,height=420)
        self.lblA.configure(background="#212121",foreground="white",padding=110)
        self.lblTitulo = ttk.Label(self.lblA,text="Apepixel",background="#212121",foreground="#bb255b",font=('',12,'bold'))
        self.lblTitulo.place(x=10,y=10,width=100,height=20)

        self.buttonGit = tk.Button(self.lblA,text="GitHub",background="#212121",foreground="#bb255b",font=('',12,'bold'))
        self.buttonGit.place(x=580,y=380)
        self.buttonGit.configure(command=self.launchGit)
        self.lblTitulo.place(x=10,y=10,width=100,height=20)
        self.menubar = tk.Menu(self.ventana)
        self.ventana.config(background="#0e1018")
        self.ventana.config(menu=self.menubar)
        self.menubar.config(background="black")
        
        
        opciones = tk.Menu(self.menubar,tearoff=0)
        opciones.add_command(label="C.R.U.D",command = self.configurar)
        opciones.add_separator()
        opciones.config(background="black",foreground="white")
        self.menubar.add_cascade(label="Parking", menu=opciones)
        
        self.ventana.mainloop()
        


    def configurar(self):
        self.ventana.destroy()
        IndexView()
    
    def launchGit(self):
        webbrowser.open('https://github.com/Apepixel', new=2)
        
        
        

s=FrmParqueadero()
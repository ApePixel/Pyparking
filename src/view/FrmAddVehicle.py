import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class AddVehicle:
    
    def __init__(self,ventanaGestion,parqueadero):
        self.window = tk.Toplevel(ventanaGestion)
        self.window.config(background="#252525")
        self.window.geometry("350x200")
        self.verify = False
        self.controller = parqueadero
        self.labelFrame = ttk.LabelFrame(self.window,text="Data from vehicle (6 characters):")
        self.window.focus()
        self.labelFrame.grid(column=0,row=0,padx=(50,0),pady=30)
        self.login()
        self.window.protocol("WM_DELETE_WINDOW",self.confirm)
        self.window.resizable(0,0)
        self.window.grab_set()

    def login(self):
        
        
        self.styles = ttk.Style(self.window)
        self.styles.configure("TLabelframe",background="black",foreground="white")
        self.styles.configure("TLabelframe.Label",background="black",foreground="white")
        self.Plate_value = tk.StringVar()

        self.lblPlate = ttk.Label(self.labelFrame,text="Plate:"
        ,background="black"
        ,foreground="white")
        self.lblPlate.grid(column=0,row=0,padx=8,pady=8)
        self.txtPlate = ttk.Entry(self.labelFrame,textvariable=self.Plate_value)
        self.txtPlate.grid(column=1,row=0,padx=8,pady=8)
        self.btn_save_plate = tk.Button(self.labelFrame,background="#7dbf2f"
        ,text="Add",command=self.save_plate)
        self.btn_save_plate.grid(column=0, row=2, padx=8, pady=(30,20))
        self.btn_save_plate.config(font=('',9,'bold'))
        

    def save_plate(self):  
        if len(self.Plate_value.get()) == 6 and self.controller.verify_plate(self.Plate_value.get()):
            self.verify = True
            self.window.destroy()
            
        else:
            self.verify=False
            mb.showinfo("ERROR","The Plate is repetead or doesn't have 6 characters")
        

    def show(self):
        self.window.wait_window()
    
    def confirm(self):
        
        self.window.destroy()
        
    def catchParam(self):
        if self.verify:
            return self.Plate_value.get()
        return None
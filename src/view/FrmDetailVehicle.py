import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox as mb


class FrmDetailVehicle:

    def __init__(self, CRUD_window, vehicle,parking):
        self.window = tk.Toplevel(CRUD_window)
        self.window.config(background="#252525")
        self.window.geometry("350x200")
        self.opi = ""
        self.window.focus()

        self.controller = parking
        self.vehicle = vehicle
        
        self.labelframe = ttk.LabelFrame(self.window, text="Datos vehiculos")
        
        self.labelframe.grid(column=0,row=0,padx=(70,0),pady=30)
        self.initC()
        self.window.protocol("WM_DELETE_WINDOW", self.confirm)
        self.window.resizable(0, 0)
        self.window.grab_set()

    def initC(self):
        
        self.styles = ttk.Style(self.window)
        self.styles.configure("TLabelframe",background="black",foreground="white")
        self.styles.configure("TLabelframe.Label",background="black",foreground="white")


        self.plate_value = tk.StringVar()
        self.plate_value.set(self.vehicle.getPlate())
        self.lblPlate = ttk.Label(
            self.labelframe, text="Marca:", background="black", foreground="white")
        self.lblPlate.grid(column=0, row=0, padx=8, pady=8)
        self.txtPlate = ttk.Entry(
            self.labelframe, textvariable=self.plate_value)

        self.txtPlate.grid(column=1, row=0, padx=8, pady=8)
        #creating add button
        self.btn_save_plate = tk.Button(
            self.labelframe, text="Edit",background="#7dbf2f")
        self.btn_save_plate.grid(column=0, row=2, padx=8, pady=(30,20))
        #creating lambda to catch operation
        self.btn_save_plate.bind('<1>',lambda event, op="save": self.operation(op))
        #to close window
        self.btn_save_plate.config(command=self.confirm,font=('',9,'bold'))

        self.btn_delete_plate = tk.Button(
            self.labelframe, text="Allow exit",background="#b73838")
        self.btn_delete_plate.bind('<1>',lambda event, op="delete": self.operation(op))
        self.btn_delete_plate.grid(column=1, row=2, padx=8, pady=(30,20))
        self.btn_delete_plate.config(command=self.confirm,font=('',9,'bold'))
        
    def delete_plate(self):
        
        return self.vehicle

    def save_plate(self):
        
        return self.plate_value.get()

    def show(self):
        self.window.wait_window()

    def confirm(self):
        self.window.destroy()

    def operation(self,op):
        if self.vehicle.getPlate() != self.plate_value.get():
            
            if len(self.plate_value.get()) == 6 and self.controller.verify_plate(self.plate_value.get()):
                self.verify = True
                self.opi=op
                self.window.destroy()
                
            else:
                self.verify=False
                mb.showinfo("ERROR","The Plate is repeated or does not have 6 characters")
            
        else:
            self.opi=op
            self.window.destroy()
    
    def catchOperacion(self):
        return self.opi



import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox as mb


class FrmStateVehicle:

    def __init__(self, CRUD_window, vehicle,parking):
        self.window = tk.Toplevel(CRUD_window)
        self.window.config(background="#252525")
        self.window.geometry("480x240")
        self.opi = ""
        self.window.focus()

        self.controller = parking
        self.vehicle = vehicle
        
        self.labelframe = ttk.LabelFrame(self.window, text="Datos vehiculos")
        
        self.labelframe.grid(column=0,row=0,padx=(70,0),pady=30)
        self.initC()
        self.window.protocol("WM_DELETE_WINDOW", self.confirmar)
        self.window.resizable(0, 0)
        self.window.grab_set()

    def initC(self):
        
        self.styles = ttk.Style(self.window)
        self.styles.configure("TLabelframe",background="black",foreground="white")
        self.styles.configure("TLabelframe.Label",background="black",foreground="white")

        self.lbl_state = ttk.Label(self.window,text="State:"
        ,background="#252525"
        ,foreground="white")
        
        self.lbl_state.grid(column=0, row=0, padx=0, pady=(30,20))


        self.lbl_state.configure(font=('',9,'bold'))


        self.lblHours = ttk.Label(self.window,text="Actual hours:"
        ,background="#252525"
        ,foreground="white")
        
        self.lblHours.grid(column=0, row=1, padx=0, pady=(30,20))

        self.lblHours.configure(font=('',9,'bold'))


        self.lbl_driver = ttk.Label(self.window,text="Driver:"
        ,background="#252525"
        ,foreground="white")
        
        self.lbl_driver.grid(column=0, row=2, padx=0, pady=(30,20))

        self.lbl_driver.configure(font=('',9,'bold'))

        self.total_hours = tk.StringVar()
        self.total_hours.set(self.controller.get_actual_time(self.vehicle))

        self.driver = tk.StringVar()
        self.driver.set(self.vehicle.driver.get_name())

        self.lbl_hours_result = ttk.Entry(self.window,text="Hours:"
        ,background="white"
        ,foreground="black"
        ,textvariable=self.total_hours
        ,state="disabled")
        
        self.lbl_hours_result.grid(column=1, row=1, padx=0, pady=(30,20))
        

        self.entry_driver = ttk.Entry(self.window
        ,background="white"
        ,foreground="black"
        ,textvariable=self.driver
        ,state="disabled")
        
        self.entry_driver.grid(column=1, row=2, padx=0, pady=(30,20))


        states = ("Is parking","Is not parking")
        
        self.optionsC = tk.StringVar()

        self.combo = ttk.Combobox(self.window,
        width=40
        ,textvariable=self.optionsC
        ,values=states
        ,state='disabled')

        self.combo.current(0)
        

        self.combo.grid(column=1, row=0, padx=0, pady=(30,20))
        

    def mostrar(self):
        self.window.wait_window()

    def confirmar(self):
        self.window.destroy()



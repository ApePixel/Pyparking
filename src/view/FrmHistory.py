import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style


class FrmHistory:
    
    def __init__(self,CRUD_window,array):
        self.window = tk.Toplevel(CRUD_window)
        self.window.geometry("1117x466")
        self.window.focus()
        self.window.config(background="#0e1018")
        self.array=array
        self.styles = ttk.Style(self.window)
        self.styles.theme_use("clam")
        self.initTable()
        self.window.protocol("WM_DELETE_WINDOW",self.confirm)
        self.window.resizable(0,0)
        self.window.grab_set()

    
    def initTable(self):

        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=20)

        self.scroll = ttk.Scrollbar(self.frame)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)

        
        self.styles.configure("Treeview",fieldbackground="#0e1018",background="#0e1018",fieldforeground="white")
        
        
        self.table = ttk.Treeview(self.frame,yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.table.yview)
        self.table['columns'] = ("Plate","Driver","State","Out hour","Total")

        self.table.column("#0",width=50,minwidth=25)
        self.table.column("Plate",anchor=tk.CENTER,width=90,minwidth=25)
        self.table.column("Driver",anchor=tk.W,width=120,minwidth=25)
        self.table.column("State",anchor=tk.W,width=150,minwidth=25)
        self.table.column("Out hour",anchor=tk.W,width=120,minwidth=25)
        self.table.column("Driver",anchor=tk.W,width=120,minwidth=25)

        self.table.heading("#0",text="Label",anchor=tk.W)
        self.table.heading("Plate",text="Plate",anchor=tk.CENTER)
        self.table.heading("Driver",text="Driver",anchor=tk.W)
        self.table.heading("State",text="State",anchor=tk.W)
        self.table.heading("Out hour",text="Out hour",anchor=tk.W)
        self.table.heading("Total",text="Total",anchor=tk.W)

        for i in range(len(self.array)):

            self.table.insert("",tk.END,text=f"{i+1}",values=(f"{self.array[i].getPlate()}",
            f"{self.array[i].driver.get_name()}",f"{self.array[i].get_state()}",f"{self.array[i].get_out_hour()}",f"{self.array[i].getTotal()}"))
        self.table.pack(pady=20)
    
    def show(self):
        self.window.wait_window()

    def confirm(self):
        self.window.destroy()
        

from random import randint
import tkinter as tk
from tkinter import ttk
from src.parking.parking import Parking
from src.vehicles.vehicle import Vehicle
from src.clients.client import Client
from src.view.FrmAddVehicle import AddVehicle
from src.view.FrmDetailVehicle import FrmDetailVehicle
from src.view.FrmHistory import FrmHistory
from src.view.FrmStateVehicle import FrmStateVehicle
import random
from tkinter import messagebox as mb


class IndexView:

    def __init__(self):
        self.listC = list()
        self.parking = Parking()
        self.window = tk.Tk()
        self.window.geometry("1297x466")
        self.window.focus()
        self.window.config(background="#252525")
        self.window.resizable(0, 0)
        self.listCliente = list()

        # panel body definition
        self.panel = tk.PanedWindow(
            self.window, background="#252525", orient=tk.VERTICAL)
        self.panel.pack(fill=tk.BOTH, expand=1)
        # adding first panel
        self.panelB = tk.PanedWindow(self.panel, background="#0e1816")
        self.btnSave = tk.Button(self.panelB, text="Save (Hour value = $3000)", background="black",
                                    activebackground="#252525", activeforeground="white", fg="white", command=self.configurar)

        self.btnSave.pack(side=tk.LEFT)
        # find section
        self.findedvalue = tk.StringVar()
        self.historyList = list()
        self.input_to_search = ttk.Entry(
            self.panelB, textvariable=self.findedvalue)
        self.input_to_search.pack(side=tk.LEFT, padx=(400, 0))

        self.btn_search = tk.Button(self.panelB, text="Search (plate)", background="#252525",
                                activebackground="#252525", activeforeground="white", fg="white", command=self.find)
        self.btn_search.pack(side=tk.LEFT)

        self.btn_history = tk.Button(self.panelB, text="History", background="black",
                                    activebackground="#252525", activeforeground="white", fg="white", command=self.getHistory)
        self.btn_history.pack(side=tk.RIGHT)

        self.panel.add(self.panelB, minsize=50)
        
        self.panelD = tk.PanedWindow(self.panel,orient=tk.VERTICAL)
        
        self.panel.add(self.panelD)

        self.getScrollBar()
        
        self.window.mainloop()
    

    def getScrollBar(self):
        self.panelC = tk.PanedWindow(self.panelD)
        
        
        self.frame = ttk.Frame(self.panelC)
        self.frame.pack(fill=tk.BOTH,expand=1)
        
        self.canva =tk.Canvas(self.frame, background="#151515")
        
        
        self.scroll= ttk.Scrollbar(self.frame,orient=tk.VERTICAL,command=self.canva.yview)
        self.scroll.pack(side=tk.RIGHT,fill=tk.BOTH)

        self.canva.config(yscrollcommand=self.scroll.set, background="#0e1018")
        self.canva.bind('<Configure>',lambda e: self.canva.configure(scrollregion=self.canva.bbox("all")))
        self.canva.pack(fill=tk.BOTH,expand=True)
        
        self.frame2=tk.Frame(self.canva,background="#0e1018")
        self.canva.create_window((0,0),window=self.frame2,anchor="nw")

        self.button = list()
        self.button_client = list()
        self.button_state = list()
        self.button_time_in = list()
        self.buttonIndex = list()

        ranColor = ("#7dbf2f", "#38b7ab", "#9259ff", "#b73838", "#cc9428")
        
        
        if self.getSize() != 0:

            labelTitleA = ttk.Label(self.frame2,background="#0e1018",foreground="white",text="ID")
            labelTitleA.grid(column=0, row=0,padx=(10,0), pady=10,ipadx=10)

            labelTitle = ttk.Label(self.frame2,background="#0e1018",foreground="white",text="Plates (Click)")
            labelTitle.grid(column=1,row=0,padx=(130,0),ipadx=10, pady=2)

            labelTitleB = ttk.Label(self.frame2,background="#0e1018",foreground="white",text="Drivers")
            labelTitleB.grid(column=2,row=0,padx=(130,0),ipadx=10, pady=2)

            labelTitleC = ttk.Label(self.frame2,background="#0e1018",foreground="white",text="State (Click)")
            labelTitleC.grid(column=3,row=0,padx=(130,0),ipadx=10, pady=2)

            labelTitleD = ttk.Label(self.frame2,background="#0e1018",foreground="white",text="Entry time")
            labelTitleD.grid(column=4,row=0,padx=(130,0),ipadx=10, pady=2)

            for i in range(len(self.listC)):
                self.button.append(tk.Label(
                    self.frame2,
                    background="#1ef08c",
                    foreground="black",
                    activebackground="black",
                    activeforeground="#ff00ff",
                    font=('',11,'bold'),
                    text=self.listC[i].getPlate()
                ))
                self.button[i].bind('<1>', lambda event,
                                    i=i: self.getVehicleSelected(i))
                
                self.button[i].grid(column=1, row=i+1,padx=(120,0),ipadx=10, pady=2)

                #CLIENTS#########################
                self.button_client.append(tk.Label(
                    self.frame2,
                    background=ranColor[randint(0, len(ranColor)-1)],
                    foreground="black",
                    activebackground="black",
                    activeforeground="white",
                    font=('',11,'bold'),
                    text=self.listC[i].driver.get_name()
                ))
                self.button_client[i].grid(column=2, row=i+1,padx=(150,0), pady=10,ipadx=10)
                ##########################

                #STATE#########################
                self.button_state.append(tk.Label(
                    self.frame2,
                    background=ranColor[randint(0, len(ranColor)-1)],
                    foreground="black",
                    activebackground="black",
                    activeforeground="white",
                    font=('',11,'bold'),
                    text=self.listC[i].get_state()
                ))
                self.button_state[i].bind('<1>', lambda event,
                                    i=i: self.getStateSelected(i))
                self.button_state[i].grid(column=3, row=i+1,padx=(150,0), pady=10,ipadx=10)
                ##########################

                #HOURS#########################
                self.button_time_in.append(tk.Label(
                    self.frame2,
                    background=ranColor[randint(0, len(ranColor)-1)],
                    foreground="black",
                    activebackground="black",
                    activeforeground="white",
                    font=('',11,'bold'),
                    text=self.listC[i].get_in_hour()
                ))
                
                self.button_time_in[i].grid(column=4, row=i+1,padx=(150,0), pady=10,ipadx=10)
                ##########################

                #INDEX#########################
                self.buttonIndex.append(tk.Label(
                    self.frame2,
                    background=ranColor[randint(0, len(ranColor)-1)],
                    foreground="black",
                    activebackground="black",
                    activeforeground="white",
                    font=('',11,'bold'),
                    text=i+1
                ))
            
                self.buttonIndex[i].grid(column=0, row=i+1,padx=(10,0), pady=10,ipadx=10)
        self.panelC.pack(fill=tk.X,expand=True)
        self.panelD.add(self.panelC)
        

    def getSize(self):
        return len(self.listC)

    def find(self):
        if self.findedvalue.get() == "":
            mb.showinfo("ERROR","You have not written any value")

        elif self.getSize() <= 0:
            mb.showinfo("ERROR","Theres not vehicles parking")
            self.findedvalue.set('')
        else:
            self.i = self.parking.find_car(self.findedvalue.get())
            if self.i == -1:
                mb.showinfo("ERROR","Plate is not founded")
                self.findedvalue.set('')
            else:

                self.findedvalue.set('')
                self.getVehicleSelected(self.i)

    # Adding one vehicle from another frame
    def configurar(self):
        dialog = AddVehicle(self.window,self.parking)
        dialog.show()

        if dialog.catchParam() != None:
    
            ranNames = ("Felipe", "Diana", "Angie", "Laura", "Andres", "Karen",
                        "Lucia", "Sandra", "Marcela", "Daniela", "Nicole", "Cristina", "Adriana", "Pablo", "Camilo", "Camila", "Antonio", "Nicolas")
            self.listC = self.parking.add_Car(
                Vehicle(dialog.catchParam(), Client(ranNames[randint(0, len(ranNames)-1)])))
            self.panelD.remove(self.panelC)
            self.getScrollBar()

    

    def getVehicleSelected(self, i):
        vehicle = self.listC[i]
        little_window = FrmDetailVehicle(self.window, vehicle,self.parking)
        little_window.show()
        

        if little_window.catchOperacion() == "save":
            self.listC[i].setPlate(little_window.save_plate())
            self.panelD.remove(self.panelC)
            self.getScrollBar()
            
            
        elif little_window.catchOperacion() == "delete":
            self.listC[i].setTotal(self.parking.make_calc(i))
            self.listC[i].set_state(f"Left the parking")
            self.historyList.append(self.listC[i])
            del self.listC[i]
            self.panelD.remove(self.panelC)
            self.getScrollBar()
            
    def getStateSelected(self,i):
        vehicle = self.listC[i]
        little_window= FrmStateVehicle(self.window, vehicle,self.parking)
        little_window.mostrar()
    def getHistory(self):
        little_window =FrmHistory(self.window,self.historyList)
        little_window.show()
    
    
            



from datetime import datetime

class Vehicle:

    def __init__(self,Plate,driver):
        self.Plate = Plate
        self.state = "Is parking"
        self.in_hour = datetime.now()
        self.out_hour = datetime.now()
        self.total=0
        
        self.driver=driver
        
        
    def getTotal(self):
        return self.total

    def setTotal(self,valor):
        self.total=valor

    def getPlate(self):
        return self.Plate

    def setPlate(self, Plate):
        self.Plate = Plate

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_in_hour(self):
        return self.in_hour

    def set_in_hour(self, horaEntrada):
        self.horaEntrada = horaEntrada

    def set_out_hour(self):
        self.out_hour=datetime.now()

    def get_out_hour(self):
        return self.out_hour

    

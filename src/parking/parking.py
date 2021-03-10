from datetime import datetime

class Parking:

    def __init__(self):
        self.cars = list()
        self.drivers=list()

    def add_Car(self, car):
        
        self.cars.append(car)
        car.set_state("Is in the parking")
        return self.cars
        
    def verify_plate(self,Plate):
        for i in range(len(self.cars)):
            if Plate == self.cars[i].getPlate():
                return False
        return True

    
    def find_car(self,Plate):

        for i in range(len(self.cars)):
            if self.cars[i].getPlate() == Plate:
                print(f"This vehicle was founded {self.cars[i].getPlate()} ")
                return i
        return -1

    def delete_ar(self,i):
        print(f"This vehicle was deleted {self.cars[i].getPlate()} ")
        del self.carros[i]
        return self.cars
    
    def edit_car(self,vehiculo,i):
        print(f"The Plate is: {self.carros[i].getPlate}")
        self.cars[i].setPlate(vehiculo.getPlate())
        print(f"The Plate got updated to: {self.carros[i].getPlate}")
        return self.cars

    def make_calc(self,i):
        self.cars[i].set_out_hour()
        total_hours = self.cars[i].get_out_hour()-self.cars[i].get_in_hour()
        horitas = round((total_hours.days*24)+(total_hours.seconds/3600))
        if horitas < 1:
            horitas = 1
        total = horitas*3000
        return total

    def get_actual_time(self,vehiculo):
        actual_hour = datetime.now()
        total_hour = actual_hour-vehiculo.get_in_hour()
        return total_hour







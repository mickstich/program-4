from datetime import datetime


class car:
    def __init__(self,weight,max_speed,no_of_wheels,service_dates):
        self.weight=weight
        self.max_speed=max_speed
        self.no_of_wheels=no_of_wheels
        self.service_dates=service_dates
    def get_weight(self):
        return self.weight
    def get_max_speed(self):
        return self.max_speed
    def get_wheels(self):
        return self.no_of_wheels
    def get_serv_date(self):
        return self.service_dates
    def update_weight(self,value):
        self.weight = value
    def update_max_speed(self,value):
        self.max_speed = value
    def update_wheels(self,value):
        self.no_of_wheels = value
    def add_service_date(self,value):
        self.service_dates = value
    def car_parts(self):
        print ("weight: {0}kg  , speed: {1}km/h ,  wheels: {2} ,  date: {3}".format (self.weight,self.max_speed,self.no_of_wheels,self.service_dates))
obj1 = car(1400, 200, 4, datetime(2000, 3, 20))
obj2 = car(1500, 300, 4, datetime(2000, 8, 30))
obj3 = car(1600, 350, 4, datetime(2001, 9, 28))

obj1.car_parts()
obj2.car_parts()
obj3.car_parts()





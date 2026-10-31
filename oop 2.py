class Car:
    def __init__(self,colour,model,company):
        self.colour=colour
        self.model=model
        self.company=company

    def define(self):
        print(f"company : {self.company}  model : {self.model}    colour : {self.colour}")

car1=Car('yellow','90s','bmw')
car1.define()

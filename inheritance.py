class car:
    def __init__(self,name,brand):
        self.model_name=name
        self.model_brand=brand

    def launch(self):
        print(f"{self.model_name} by {self.model_brand} launched !")
# creating an object of car class
car1=car("ghost","rolsroys ")
print(car1.launch())
# class benz inherited launch method from car class
class benz(car):
    pass
h1=benz("Maclaren","Benz")
h1.launch()

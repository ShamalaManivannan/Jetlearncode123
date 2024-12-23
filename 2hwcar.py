class Car():
    def __init__(self,colour,horsepower,name,type):
        self.colour = colour
        self.horsepower = horsepower
        self.name = name
        self.type = type
        
    
    def get_colour(self): #this get function, if you want to get any hidden values, etc. bank details(cant access from common people, it is private/personal)
        return self.colour
    def set_shape(self,new_colour): #it can update a name
        self.colour = new_colour
    def increase_horsepower(self): #increasing the preference
        self.horsepower= self.horsepower+20
    def show_car(self):
        print("Here are your car details {},{},{},{}".format(self.colour,self.horsepower,self.name,self.type))

volkswagen = Car("red",241,"Volkswagen Golf GTI","SMALL")
volkswagen.show_car()
volkswagen.increase_horsepower()
print(volkswagen.get_colour())
volkswagen.set_shape("McLaren")
volkswagen.show_car()

question = input("What brand is your car,for your car details")
if question == "volkswagen":
    volkswagen.show_car()





        
    




        
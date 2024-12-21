class Fruit():
    def __init__(self,colour,taste,shape,preference):
        self.colour = colour
        self.taste = taste
        self.shape = shape
        self.preference = preference
        
    
    def get_shape(self): #this get function, if you want to get any hidden values, etc. bank details(cant access from common people, it is private/personal)
        return self.shape  
    def set_shape(self,new_shape): #it can update a name
        self.shape = new_shape
    def increase_preference(self): #increasing the preference
        self.preference = self.preference+1
    def show_fruit(self):
        print("Im a fruit with{},{},{},{}".format(self.colour,self.taste,self.shape,self.preference))

apple = Fruit("red","sour","round",1)
apple.show_fruit()
apple.increase_preference()
print(apple.get_shape())
apple.set_shape("pear")
apple.show_fruit()

banana = Fruit("yellow","sweet","cyclinder",2)
banana.show_fruit()
banana.increase_preference()
banana.show_fruit()


        
    




        
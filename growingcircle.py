import pygame
pygame.init()

screen=pygame.display.set_mode([500,500])

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)

screen.fill(white)

class Circle:
    def __init__(self,colour,pos,radius,width=0):
        self.colour = colour
        self.pos = pos
        self.radius = radius
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius)

    def grow(self,x):        
        self.radius += x
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius)

pos = (300,300)
radius = 50
width = 2
pygame.draw.circle(screen,red,pos,radius,width)        

pygame.display.update()

blue_circle = Circle(blue,pos,radius+60)
red_circle = Circle(red,pos,radius+40)
yellow_circle = Circle(yellow,pos,radius,5)
green_circle = Circle(green,pos,20)

while True:
    for event in pygame.event.get():  #iterate through each of the events through the for loop
        if  (event.type == pygame.MOUSEBUTTONDOWN): 
            blue_circle.draw()
            red_circle.draw()
            yellow_circle.draw()
            green_circle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            blue_circle.grow(2)
            red_circle.grow(2)
            yellow_circle.grow(2)
            green_circle.grow(2)
            pygame.display.update()
        elif  (event.type == pygame.MOUSEMOTION): 
            pos= pygame.mouse.get_pos()
            black_circle = Circle(black,pos,5)  
            black_circle.draw()
            pygame.display.update() 


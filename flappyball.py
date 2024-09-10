import pgzrun
from random import randint
WIDTH = 800
HEIGHT = 600

TITLE = "Flappy Ball"
R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = R,G,B
gravity = 2000 #2000 means pixels per second(Motion)
 
class Ball:
    def __init__ (self,initial_x,intial_y): #only need self when inside a class
        self.x = initial_x
        self.y = intial_y
        self.vx = 200  #the balls horizontal velocity is set to 200 pixels per second
        self.vy = 0     # balls vertical velocity is set to 0
        self.radius = 40  
    
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,CLR)   #draw filled circle with the specified radius and colour

ball = Ball(50,100) #initial position of the ball

def draw():
    screen.clear()
    ball.draw()

def update(dt):  #updating the position and the velocity of the ball at each frame based on dt(time)
    uy=ball.vy #ball.vy is vertical velocity of the ball 
    ball.vy+=gravity*dt #applying gravity to the vertical velocity, formula is gravity times the time
    ball.y+=(uy+ball.vy)*0.5*dt #calculating balls new vertical position using the average of the iunitial and the final time, how much the ball should move
    if ball.y > HEIGHT-ball.radius:#calculating the bounce
        ball.y=HEIGHT-ball.radius
        ball.vy = -ball.vy*0.9 #balls vertical velocity is reversed simulating a bounce balls velocity is also reduced 10 percent, inelastic 
    ball.x += ball.vx*dt #UPDATING HORizontal position, calculates how far the ball should move based on the elapsed time
    if ball.x > WIDTH-ball.radius or ball.x<ball.radius: #CHECKING IF THE BALL HITS THE RIGHT EDGE OF THE SCREEN AND THE LEFT EDGE SCREEN simulating a bounce of the wall,inelastic colision
        ball.vx = -ball.vx
def on_key_down(key): #if space button is clicked the ball jumps upwards
    if key == keys.SPACE:
        ball.vy=-500

pgzrun.go()         
            

    


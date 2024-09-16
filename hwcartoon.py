import pgzrun
from random import randint
TITLE="Catch Spongebob"
WIDTH=800 
HEIGHT=448
message=""
score=0
gameover=False
spongebob=Actor("spongebob")  #
def draw(): 
  screen.clear() 
  screen.blit("background",(0,0))
  spongebob.draw() 
  screen.draw.text(message,center=(400,10),fontsize=30) 
  if gameover:
        screen.fill("blue")
        screen.draw.text("time up,your final score:" +str(score),midtop=(WIDTH/2,10),fontsize=40,color="yellow")

def timeup():
    global gameover
    gameover=True

def place_spongebob(): 
  spongebob.x=randint(50,WIDTH-200) 
  spongebob.y=randint(50,WIDTH-400)  
def on_mouse_down(pos): 
  global message,score
  if spongebob.collidepoint(pos): 
    message="you catched spongebob!"
    place_spongebob()
    score=score+10
  else:
    message="you missed!"
    score=score-10
place_spongebob()
clock.schedule(timeup,20)
pgzrun.go()
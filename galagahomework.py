import pgzrun
import random

WIDTH = 1200
HEIGHT = 600
white = (255,255,255)
blue = (0,0,255)
ship = Actor("shooter")  
insect = Actor("insect")

ship.pos=(WIDTH//2,HEIGHT-60)
speed = 5
bullets = []
enemies = []
enemies.append(Actor("insect"))
enemies[-1].x=10
enemies[-1].y=-100
score = 0

def display_score():
    screen.draw.text(str(score),50,30)

def on_keys_down(key):  
    if key == keys.SPACE:
        arrows.append(Actor("arrow"))
        arrows[-1].x=ship.x
        arrows[-1].y=ship.y-50
        
def update():
    global score    
    if keyboard.left:
        ship.x-=speed
        if ship.x <= 0:
            ship.x = 0
    elif keyboard.right:
        ship.x+=speed
        if ship.x >= WIDTH:
            ship.x= WIDTH
    for  arrow in arrows:
        if arrow.y <= 0:
            arrows.remove(arrow)       
        else:
            arrow.y-=10
    for enemy in enemies:
        enemy.y += 5
        if enemy.y >= HEIGHT:
            enemy.y=-100
            enemy.x = random.randint(50,WIDTH-50)
        for arrow in arrows:
            if enemy.colliderect(arrow):
                score+=100
                arrows.remove(arrow)
                enemies.remove(enemy)
def draw():
    screen.clear()
    screen.fill(blue)
    for arrow in arrows:
        arrow.draw()
    for enemy in enemies:
        enemy.draw()
    ship.draw()
    display_score()

pgzrun.go          

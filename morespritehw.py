import pygame
from pygame.locals import *
import random


pygame.init()

WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

class PacMan():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/35262/Downloads/images/pacman.png")   
        self.image = pygame.transform.scale(self.image[60,70])
        self.rect  = self.image.get_rect()

    def update(self,pressed_keys):
        if pressed_keys[K._UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K._DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K._LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K._RIGHT]:
            self.rect.move_ip[5,0]
        if self.rect.left > 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.left = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


class Bots():
    def __init__(self):
        super().__init__(self)
        bots = [red_bot = pygame.image.load("C:/Users/35262/Downloads/images/red_bot.png"),
        yellow_bot = pygame.image.load("C:/Users/35262/Downloads/images/yellow_bot.png")]

sprites = pygame.sprite.Group()


def start_game():
    PacMan = PacMan()
    Bots = Bots()
    sprites.add(PacMan,Bots)




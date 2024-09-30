import pygame
from random import randint

pygame.init()
screen=pygame.display.set_mode([600,600])

white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 192, 203)
red = (255, 0, 0)

pygame.display.set_caption("Bee and Flower Game")

bee = pygame.image.load("C:/Users/35262/Downloads/images/bee.png")
flower= pygame.image.load("C:/Users/35262/Downloads/images/flower.png")

bee_rect = bee_img.get_rect(center=(200, 200))
flower_rect = flower_img.get_rect(center=(200, 200))

score = 0
gameover = False
clock = pygame.time.Clock()

font = pygame.font.Font(ariel, 40)

GAME_OVER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GAME_OVER_EVENT, 60000)

def place_flower():
    flower_rect.x = randint(70, WIDTH - 70)
    flower_rect.y = randint(70, HEIGHT - 70)

def draw_text(text, color, pos, size=40):
    font = pygame.font.Font(ariel, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

running = True

while running:
    screen.fill(pink if gameover else white)
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == GAME_OVER_EVENT:
            gameover = True

    if not gameover:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bee_rect.x -= 2
        if keys[pygame.K_RIGHT]:
            bee_rect.x += 2
        if keys[pygame.K_UP]:
            bee_rect.y -= 2
        if keys[pygame.K_DOWN]:
            bee_rect.y += 2

        if bee_rect.colliderect(flower_rect):
            score += 10
            place_flower()

    screen.blit(bee_img, bee_rect.topleft)
    screen.blit(flower_img, flower_rect.topleft)
    draw_text(f"Score: {score}", BLACK, (10, 10))

    if gameover:
        draw_text(f"Time up! Your final score: {score}", RED, (WIDTH // 4, HEIGHT // 2), size=50)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


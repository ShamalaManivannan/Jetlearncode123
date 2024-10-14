import pygame
from random import randint
from time import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Game")

# Load background and planet images
background = pygame.image.load("C:/Users/35262/Downloads/images/bckgrnd.png")  # Background image
planets_images = [
    pygame.image.load("C:/Users/35262/Downloads/images/Mercury.png"),   # Closest planet
    pygame.image.load("C:/Users/35262/Downloads/images/Venus.png"),
    pygame.image.load("C:/Users/35262/Downloads/images/Earth.png"),
    pygame.image.load("C:/Users/35262/Downloads/images/Mars.png"),
    pygame.image.load("C:/Users/35262/Downloads/images/Jupiter.png"),
    pygame.image.load("C:/Users/35262/Downloads/images/Saturn.png"),
    pygame.image.load("C:/Users/35262/Downloads/images/Uranus.png"),
    pygame.image.load("C:/Users/35262/Downloads/images/Neptune.png")    # Farthest planet
]

# Game variables
planets = []
lines = []
next_planet = 0
start_time = 0
total_time = 0
number_of_planets = len(planets_images)

# Set up font
font = pygame.font.Font(None, 30)

def create_planets():
    global start_time
    for i, planet_image in enumerate(planets_images): #index number
        planet = {
            'image': planet_image,
            'rect': planet_image.get_rect(topleft=(randint(40, WIDTH - 40), randint(40, HEIGHT - 40))),
            'number': i + 1
        }
        planets.append(planet)
    start_time = time()

def draw():
    global total_time

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the planets and their numbers
    for planet in planets:
        screen.blit(planet['image'], planet['rect'])
        number_text = font.render(str(planet['number']), True, (255, 255, 255))
        screen.blit(number_text, (planet['rect'].x, planet['rect'].y + 60))

    # Draw the lines between the planets
    for line in lines:
        pygame.draw.line(screen, (255, 255, 255), line[0], line[1], 2)

    # Draw the timer or game completed message
    if next_planet < number_of_planets:
        total_time = time() - start_time
        time_text = font.render(f"Time: {round(total_time, 1)}s", True, (255, 255, 255))
        screen.blit(time_text, (10, 10))
    else:
        completion_text = font.render("Game completed!", True, (255, 255, 255))
        screen.blit(completion_text, (10, 10))

def check_click(pos):
    global next_planet, lines
    if next_planet < number_of_planets:
        if planets[next_planet]['rect'].collidepoint(pos):
            if next_planet > 0:
                lines.append((planets[next_planet - 1]['rect'].center, planets[next_planet]['rect'].center))
            next_planet += 1
        else:
            lines = []
            next_planet = 0  # Reset if clicked out of order of the planets

def main(): 
    global next_planet

    create_planets()
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check_click(event.pos)

        if len(lines) == number_of_planets - 1:
            print("Game completed")
            next_planet = number_of_planets  # Prevent further  the game so if complete its complete game done

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

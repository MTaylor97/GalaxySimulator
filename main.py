import pygame
from sys import exit

pygame.init()

# create screen
screen = pygame.display.set_mode((1400, 900))
pygame.display.set_caption('Autonomous Car IoT')
clock = pygame.time.Clock()


# define Car class
class Entity:
    def __init__(self, x, y, mass, direction):
        self.mass = mass
        self.direction = direction
        self.speedX = 5
        self.speedY = 5
        self.x = x
        self.y = y


class Planet(Entity):
    def __init__(self, x, y, direction, mass):
        super().__init__(x, y, mass, direction)


class Sun(Entity):
    def __init__(self, x, y, direction, mass):
        super().__init__(x, y, mass, direction)


while True:

    # facilitate exiting of program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # update everything
    pygame.display.update()
    clock.tick(60)

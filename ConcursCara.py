import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mondongo")

def draw_face():

    pygame.draw.circle(screen, YELLOW, (200, 200), 150)

    pygame.draw.circle(screen, WHITE, (130, 140), 30)
    pygame.draw.circle(screen, WHITE, (270, 140), 30)

    pygame.draw.circle(screen, BLACK, (130, 140), 10)
    pygame.draw.circle(screen, BLACK, (270, 140), 10)

    pygame.draw.rect(screen, RED, (150, 280, 100, 20))

    pygame.draw.polygon(screen, WHITE, [(200, 210), (150, 280), (250, 280)])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(BLUE)

    draw_face()

    pygame.display.flip()

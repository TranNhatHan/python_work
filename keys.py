import pygame
import sys

pygame.init()
pygame.display.set_mode((500, 500))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
    pygame.display.flip()
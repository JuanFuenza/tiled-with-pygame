import pygame
from pytmx.util_pygame import load_pygame

pygame.init()
ds = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame("assets/data/tmx/basic.tmx")
print(tmx_data)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    ds.fill("black")
    pygame.display.update()

pygame.quit()
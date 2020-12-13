import sys
import os
import random
import pygame

pygame.init()

FPS = 60
WIDTH = 1024
HEIGHT = 768
STEP = 10
TILE_WIDTH = TILE_HEIGHT = 90


font = pygame.font.Font(None, 20)
text = font.render("Game over!", True, [255, 255, 255])
textpos = (10, 10)


location = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
timer = pygame.time.Clock()


tiles_group = pygame.sprite.Group()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image: ', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def terminate():
    pygame.quit()
    sys.exit()


running = True
while running:
    tiles_group.draw(screen)
    clock.tick(FPS)
terminate()

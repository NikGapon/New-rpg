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





location = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
timer = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
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




def start_screen():
    intro_text = ["New RPG"]

    fon = pygame.transform.scale(load_image('pic\menu\\fon_menu.png'), (WIDTH, HEIGHT))

    screen.blit(fon, (0, 0))
    font = pygame.font.Font("data\\tt.ttf", 100)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.display.flip()
    clock.tick(FPS)


def class_select_screen():
    fon = pygame.transform.scale(load_image('fon_menu.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)


class Button(pygame.sprite.Sprite):
    def __init__(self, logo):
        super().__init__(all_sprites)
        self.image = load_image(logo)
        self.rect = self.image.get_rect()
        self.rect.x = 4000
        self.rect.y = -4000


def terminate():
    pygame.quit()
    sys.exit()

start_screen()




running = True
while running:


    tiles_group.draw(screen)

    all_sprites.draw(screen)

    clock.tick(FPS)
terminate()

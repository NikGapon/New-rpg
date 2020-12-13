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



proverka_inv = 1


location = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
timer = pygame.time.Clock()


buy_group = pygame.sprite.Group()
shop_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
monsters_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
inv_group = pygame.sprite.Group()
decor_group = pygame.sprite.Group()
fight_group = pygame.sprite.Group()


def terminate():
    pygame.quit()
    sys.exit()


running = True
while running:

    decor_group.draw(screen)
    monsters_group.draw(screen)
    walls_group.draw(screen)
    player_group.draw(screen)
    buy_group.draw(screen)
    inv_group.draw(screen)
    fight_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
terminate()

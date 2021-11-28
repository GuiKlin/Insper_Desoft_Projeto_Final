import pygame
import os
from config import *

def carrega_assets():
    assets = {}
    
    #Sprites
    assets['vermelho'] = pygame.image.load(os.path.join(SPRITES_PATH, 'input_r.png')).convert_alpha()
    assets['vermelho'] = pygame.transform.scale(assets['vermelho'], (bolinha_width, bolinha_height))
    assets['azul'] = pygame.image.load(os.path.join(SPRITES_PATH, 'input_b.png')).convert_alpha()
    assets['azul'] = pygame.transform.scale(assets['azul'], (bolinha_width, bolinha_height))
    assets['cinza'] = pygame.image.load(os.path.join(SPRITES_PATH, 'input_judge.png')).convert_alpha()
    assets['cinza'] = pygame.transform.scale(assets['cinza'], (bolinha_width, bolinha_height))
    assets['background'] = pygame.image.load(os.path.join(SPRITES_PATH, 'bg1.png')).convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))
    assets['score_line'] = pygame.image.load(os.path.join(SPRITES_PATH, 'move_line.png')).convert_alpha()
    assets['score_line'] = pygame.transform.scale(assets['background'], (WIDTH, score_line_height))
    assets['credits'] = pygame.image.load(os.path.join(SPRITES_PATH, 'credits.png')).convert_alpha()
    assets['credits'] = pygame.transform.scale(assets['credits'], (WIDTH, HEIGHT))
    assets['HTP'] = pygame.image.load(os.path.join(SPRITES_PATH, 'howtoplay.png')).convert_alpha()
    assets['HTP'] = pygame.transform.scale(assets['HTP'], (WIDTH, HEIGHT))
    assets['menu'] = pygame.image.load(os.path.join(SPRITES_PATH, 'menu.png')).convert_alpha()
    assets['menu'] = pygame.transform.scale(assets['menu'], (WIDTH, HEIGHT))
    assets["score_font"] = pygame.font.Font('assets/lunchds.ttf', 50)

    return assets
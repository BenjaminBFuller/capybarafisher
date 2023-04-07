import pygame
from math import ceil
from pygame.locals import *  # import for flags

width, height = (1280, 800)
center_width = width / 2
center_height = height / 2
tile = 64

pygame.init()
pygame.mixer.pre_init()  # preset the mixer
pygame.display.set_caption('Capybara Fisher')
pygame.mouse.set_visible(False)  # invisible mouse cursor
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])  # types of events allowed

flags = FULLSCREEN | DOUBLEBUF | SCALED  # fullscreen, double buffering, scaled resolution
window = pygame.display.set_mode((width, height), flags)

white = [255, 255, 255]
title_font = pygame.font.Font("fonts/dpcomic.ttf", 150)
play_font = pygame.font.Font("fonts/dpcomic.ttf", 100)

menu_bg = pygame.image.load("images/menu_bg.png")
menu_bg = pygame.transform.scale(menu_bg, (width, height))
menu_bg_width = menu_bg.get_width()
menu_tiles = ceil(width / menu_bg_width) + 1  # creates the amount of tiles for the menu screen scroll

clouds_bg = pygame.image.load("images/clouds.png")
clouds_bg = pygame.transform.scale(clouds_bg, (width * 2, height))
clouds_bg.set_alpha(100)
clouds_bg_width = clouds_bg.get_width()
clouds_tiles = ceil(width / clouds_bg_width) + 1

capy_image = pygame.image.load("images/capy1.png").convert_alpha()
capy_image = pygame.transform.scale(capy_image, (64, 96))

level1_image = pygame.image.load("images/capylevel1.png").convert()
level1_image = pygame.transform.scale(level1_image, (width, height))
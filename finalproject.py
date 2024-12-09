import pygame

pygame.init()

# library of game contents
white = (255, 255, 255,)
black = (0, 0, 0)
gray = (128, 128, 128)
WIDTH = 400
HEIGHT = 500

player = pygame.image.lod('goku.png')
fps = 60
font = pygame.font.Font('freesansbold.ttf', 10)

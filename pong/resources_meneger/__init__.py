import pygame
if not pygame.font: print('fonts disambled')
if not pygame.mixer: print('sounds disambled')

from .image_src import load_image
from .sounds_src import load_sound

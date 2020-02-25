import pygame, os, sys
from pygame import locals

def load_image(filename, colorkey=None):
    fullname = os.path.join('data', filename)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as err:
        print(f'Cannot load image: {filename} : {fullname}')
        raise SystemExit(err)
    image.convert()
    if colorkey != None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, locals.RLEACCEL)
    return image, image.get_rect()
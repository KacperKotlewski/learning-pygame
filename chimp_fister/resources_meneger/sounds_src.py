import pygame, os, sys
from pygame import locals

def load_sound(filename):
    class NoneSound:
        def play(selfself):pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', filename)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as err:
        print(f'Cannot load image: {filename} : {fullname}')
        raise SystemExit(err)
    except FileNotFoundError:
        return NoneSound()
    return sound
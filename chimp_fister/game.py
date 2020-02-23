import pygame
from pygame import locals

def init():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Monkey Fever')
    pygame.mouse.set_visible(0)
    return screen

def init_background(screen:pygame.display):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    return background

def init_fonts(background:pygame.Surface):
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2)
        background.blit(text, textpos)

def display_bg(screen:pygame.display, background:pygame.Surface):
    screen.blit(background, (0, 0))
    pygame.display.flip()

def init_gameObj():
    from .resources_meneger import load_sound
    from .game_objects import Fist, Chimp
    whiff_sound = load_sound('whiff.wav')
    punch_sound = load_sound('punch.wav')
    chimp = Chimp()
    fist = Fist()
    allsprites = pygame.sprite.RenderPlain((fist, chimp))
    clock = pygame.time.Clock()
    return clock, {"fist": fist, "chimp":chimp, "whiff_sound":whiff_sound, "punch_sound":punch_sound, "allsprites": allsprites}

def mainloop(clock:pygame.time, gameObj, screen, background):
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                return
            elif event.type == locals.KEYDOWN and event.key == locals.K_ESCAPE:
                return
            elif event.type == locals.MOUSEBUTTONDOWN:
                if gameObj["fist"].punch(gameObj["chimp"]):
                    gameObj["punch_sound"].play()  # punch
                    gameObj["chimp"].punched()
                else:
                    gameObj["whiff_sound"].play()  # miss
            elif event.type == locals.MOUSEBUTTONUP:
                gameObj["fist"].unpunch()
        gameObj["allsprites"].update()

        screen.blit(background, (0, 0))
        gameObj["allsprites"].draw(screen)
        pygame.display.flip()

def play():
    screen = init()
    bg = init_background(screen)
    init_fonts(bg)
    display_bg(screen, bg)
    clock, gObj = init_gameObj()
    mainloop(clock, gObj, screen, bg)
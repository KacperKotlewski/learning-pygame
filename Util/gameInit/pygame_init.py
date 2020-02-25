import pygame
from pygame import locals
class Window:
    def __init__(self, width=600, height=400, title="The Game", bg_color=(250, 250, 250)):
        self.screen = None
        self.background = None
        self.font = None
        self.size = {"width":width, "height":height}
        self.title = title
        self.mouse_visible = True
        self.bg_color=bg_color

    def _init_pygame(self):
        pygame.init()
        screen = pygame.display.set_mode((self.size["width"], self.size["height"]))
        pygame.display.set_caption(self.title)
        self.screen = screen

    def _init_background(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill(self.bg_color)
        self.background = background

    def _init_fonts(self, background:pygame.Surface):
        if pygame.font:
            font = pygame.font.Font(None, 36)
            #text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
            #textpos = text.get_rect(centerx=background.get_width() / 2)
            #self.background.blit(text, textpos)
            self.font = font

    def _display_bg(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def Change_mouse_visability(self):
        self.mouse_visible = not self.mouse_visible
        pygame.mouse.set_visible(self.mouse_visible)

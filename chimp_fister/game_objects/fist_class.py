from pygame import sprite, mouse
from ..resources_meneger import load_image
class Fist(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('fist.png', -1)
        self.punching = False

    def update(self):
        pos = mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)

    def punch(self, target):
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5,-5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        self.punching = False
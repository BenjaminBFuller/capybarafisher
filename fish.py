import pygame as pg
from settings import *


class Hand(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.position = (900, 900)
        self.hand = capy_hand
        self.rect = self.hand.get_rect(center=self.position)
        self.hand_offset = (-235, -80)
        self.grabbing = False

    def update(self):
        self.position = pg.mouse.get_pos()
        self.rect.center = self.position
        # self.rect.move_ip(self.hand_offset)
        # when grabbing, hand moves up and left slightly for visual effect
        if self.grabbing:
            self.rect.move_ip(20, 20)

    def grab(self, fish):
        if not self.grabbing:
            self.grabbing = True
            return self.rect.colliderect(fish.rect)

    def reset_hand(self):
        self.grabbing = False

    def draw(self):
        self.update()
        window.blit(self.hand, (self.rect.x, self.rect.y))


class Fish(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.position = (300, 300)
        self.fish = fish_image
        self.rect = self.fish.get_rect(center=self.position)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.speed = 4
        self.grabbed = False

    def update(self):
        if self.grabbed:
            self.catch_and_go()
        else:
            self.swim()

    def swim(self):
        movement = self.rect.move((self.speed, 0))
        if not self.area.contains(movement):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.speed = -self.speed
                movement = self.rect.move((self.speed, 0))
                self.fish = pg.transform.flip(self.fish, True, False)
        self.rect = movement

    def catch_and_go(self):
        fish_image.set_alpha(0)

    def caught(self):
        if not self.grabbed:
            self.grabbed = True

    def draw(self):
        self.update()
        window.blit(self.fish, (self.rect.x, self.rect.y))

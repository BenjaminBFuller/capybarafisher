from board import *
from settings import *
import pygame as pg
from pygame.math import Vector2
from timer import Timer
from pygame.sprite import Sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, position, group):
        super().__init__(group)
        self.game = game
        self.board = board1
        self.image = self.standard_image = capy_image
        self.rect = self.image.get_rect(center=position)
        self.collision_rect = self.rect
        self.collision_rect.y += 32
        self.collision_rect.height = 64
        self.direction = Vector2()
        self.position = Vector2(self.rect.center)
        self.speed = 150
        self.moving = False
        self.set_animation()

    def set_animation(self):
        self.up_images = [pg.transform.scale(pg.image.load(f'images/capy/Back_0{x}.png'), (capy_width, capy_height)) for
                          x in range(8)]
        self.up_timer = Timer(self.up_images, 0, delay=50)
        self.down_images = [pg.transform.scale(pg.image.load(f'images/capy/Front_0{x}.png'), (capy_width, capy_height))
                            for x in range(8)]
        self.down_timer = Timer(self.down_images, 0, delay=50)
        self.right_images = [pg.transform.scale(pg.image.load(f'images/capy/Right_0{x}.png'), (capy_width, capy_height))
                             for x in range(8)]
        self.right_timer = Timer(self.right_images, 0, delay=50)
        self.left_images = [pg.transform.scale(pg.image.load(f'images/capy/Left_0{x}.png'), (capy_width, capy_height))
                            for x in range(8)]
        self.left_timer = Timer(self.left_images, 0, delay=50)
        self.timer = self.up_timer

    def input(self):
        keys = pygame.key.get_pressed()
        self.moving = False

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.timer = self.up_timer
            self.moving = True
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.timer = self.down_timer
            self.moving = True
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
            self.timer = self.left_timer
            self.moving = True
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.timer = self.right_timer
            self.moving = True
        else:
            self.direction.x = 0

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.position += self.direction * self.speed * dt
        self.rect.center = round(self.position)
        self.collision_rect.center = self.rect.center
        self.collision_rect.centery += 32

    def update(self, dt):
        self.input()
        print(self.moving)
        self.move(dt)

    def draw(self):
        if self.moving:
            self.image = self.timer.image()
        else:
            self.image = self.standard_image

        window.blit(self.image,
                    (self.rect.x - self.game.level.game_scroll[0], self.rect.y - self.game.level.game_scroll[1]))

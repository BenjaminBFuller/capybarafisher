import pygame
from board import *
from settings import *
from math import floor, ceil


class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.board = board1
        self.image = capy_image
        self.rect = self.image.get_rect(center=position)
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def move_check(self, row, col) -> bool:
        """
        Checks if spot on board can be moved to.

        :return: boolean value
        """
        if self.board[int(row)][int(col)] != 0:  # if move spot is not a wall
            return True
        return False

    def input(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.position += self.direction * self.speed * dt
        self.rect.center = round(self.position)

    def update(self, dt):
        self.input(dt)
        self.move(dt)

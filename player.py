from board import *
from settings import *
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, position, group):
        super().__init__(group)
        self.game = game
        self.board = board1
        self.image = capy_image
        self.rect = self.image.get_rect(center=position)
        self.collision_rect = self.rect
        self.collision_rect.y += 32
        self.collision_rect.height = 64
        self.direction = Vector2()
        self.position = Vector2(self.rect.center)
        self.speed = 150

    def move_check(self, row, col) -> bool:
        """
        Checks if spot on board can be moved to.

        :return: boolean value
        """
        if self.board[int(row)][int(col)] != 0:  # if move spot is not a wall
            return True
        return False

    def input(self):
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
        self.collision_rect.center = self.rect.center
        self.collision_rect.centery += 32
        


    def update(self, dt):
        self.input()
        self.move(dt)

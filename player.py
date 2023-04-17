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
        self.collision_rect.height = capy_height
        self.dir = "up"
        self.direction = Vector2()
        self.position = Vector2(self.rect.center)
        self.speed = 150
        self.moving = False
        self.collision_timer = pg.time.get_ticks()
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
    
    def collide_wall(self):
        if self.dir == "up":
            self.position.y += tile/2
        elif self.dir == "down":
            self.position.y -= tile/2
        elif self.dir == "left":
            self.position.x += tile /2
        elif self.dir == "right":
            self.position.x -= tile/2
        self.update_collision_rect()
       

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
        self.moving = False

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.timer = self.up_timer
            self.standard_image = self.up_images[0]
            self.dir = "up"
            self.moving = True
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.timer = self.down_timer
            self.standard_image = self.down_images[0]
            self.dir = "down"
            self.moving = True
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
            self.timer = self.left_timer
            self.standard_image = self.left_images[0]
            self.dir = "left"
            self.moving = True
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.timer = self.right_timer
            self.standard_image = self.right_images[0]
            self.dir = "right"
            self.moving = True
        else:
            self.direction.x = 0

    def update_collision_rect(self):
        self.collision_rect.center = self.rect.center
        self.collision_rect.centery += 32

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        movement = self.direction * self.speed * dt
        if not self.game.level.check_collisions():
            self.last_position = self.position
            self.position += movement
        else:
            self.position = self.last_position - movement * 15
            
        self.rect.center = round(self.position)
        self.update_collision_rect()
        

    def update(self, dt):
        self.input()
        self.move(dt)

    def draw(self):
        if self.moving:
            self.image = self.timer.image()
        else:
            self.image = self.standard_image

        window.blit(self.image,
                    (self.rect.x - self.game.level.game_scroll[0], self.rect.y - self.game.level.game_scroll[1]))

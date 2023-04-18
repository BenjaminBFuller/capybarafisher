# Capybara Fisher
# Grid based rpg; play as a capybara, fishing throughout different spots on the map

# main.py
import time
import pygame as pg
from level import Level


class Game:
    def __init__(self):
        self.previous_time = time.time()  # create clock for calculating delta time
        self.level = Level(game=self, state="fishing")

    def main(self):
        while True:
            dt = time.time() - self.previous_time  # delta time
            self.previous_time = time.time()
            self.level.update(dt)
            self.draw()

    def draw(self):
        pg.display.update()


if __name__ == "__main__":  # if in main file
    game = Game()
    game.main()  # run game loop

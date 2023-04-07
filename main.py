# Capybara Fisher
# Grid based rpg; play as a capybara, fishing throughout different spots on the map

# main.py
import time

from level import Level
from settings import *


class Game:
    def __init__(self):
        self.previous_time = time.time()  # create clock for calculating delta time
        self.level = Level("menu")

    def run_loop(self):
        while True:
            dt = time.time() - self.previous_time  # delta time
            self.previous_time = time.time()

            self.level.level_manager(dt)
            pygame.display.update()


if __name__ == "__main__":  # if in main file
    game = Game()
    game.run_loop()  # run game loop

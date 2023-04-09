import sys
from settings import *
from player import Player


class Level:
    def __init__(self, state):
        self.state = state
        self.display_surface = pygame.display.get_surface()
        self.sprite_group = pygame.sprite.Group()
        self.player = Player((400, 400), self.sprite_group)
        self.level_background = level1_image
        self.menu_scroll = 0
        self.clouds_scroll = 0
        self.game_scroll = [0, 0]
        self.wiggle = [0, 0]
        self.text_bounce = 0
        self.drop_color = [0, 0, 0]
        self.i = 0

    def level1(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # quit on esc key
                    sys.exit()
        # wiggle room: the size of the background level image - the size of the screen
        # This is the different between the size of the screen and the size of the current level
        self.wiggle[0] = self.level_background.get_size()[0] - width
        self.wiggle[1] = self.level_background.get_size()[1] - height

        # game screen scroll: screen move effect centered around player but stops at screen edges
        # dividing this value causes the scroll to smoothly follow the player in a delayed manner, not a locked scroll
        self.game_scroll[0] += (self.player.rect.x - self.game_scroll[0] - center_width) / 100
        self.game_scroll[1] += (self.player.rect.y - self.game_scroll[1] - center_height) / 100

        # game will always stop scrolling at the borders of the game map
        if self.game_scroll[0] < 0:
            self.game_scroll[0] = 0
        if self.game_scroll[1] < 0:
            self.game_scroll[1] = 0
        if self.game_scroll[0] > self.wiggle[0]:
            self.game_scroll[0] = self.wiggle[0]
        if self.game_scroll[1] > self.wiggle[1]:
            self.game_scroll[1] = self.wiggle[1]

        # blit BG image for current level, adjusting for scroll
        window.blit(self.level_background, (0 - self.game_scroll[0], 0 - self.game_scroll[1]))
        #self.sprite_group.draw(self.display_surface)
        #window.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.sprite_group.update(dt)

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.state = "level1"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # quit on esc key
                    sys.exit()

        # blit tiles so that they seamlessly align, from left to right
        for tiles in range(0, menu_tiles):
            window.blit(menu_bg, (tiles * menu_bg_width + self.menu_scroll, 0))

        for tiles in range(0, clouds_tiles):
            window.blit(clouds_bg, (tiles * -clouds_bg_width + self.clouds_scroll, 0))

        # scroll background at this rate per frame
        self.menu_scroll -= 1
        self.clouds_scroll += .5

        # reset scroll upon reaching edge of first tile
        if abs(self.menu_scroll) > menu_bg_width:
            self.menu_scroll = 0

        if abs(self.clouds_scroll) > clouds_bg_width:
            self.clouds_scroll = 0

        # blit menu titles/text with function
        self.menu_titles(155, 155, 290, 550)

        # After blitting, update display
        pygame.display.update()

    def menu_titles(self, x1, y1, x2, y2):
        """
        Main Menu Titles
        Encapsulated drop shadow functions for tiles, title bounce effect
        """
        title_drop_shadow = title_font.render("CAPYBARA FISHER", False, self.drop_color)
        title_drop_shadow.set_alpha(100)
        window.blit(title_drop_shadow, (x1 - 10 - self.text_bounce, y1 - 10 - self.text_bounce))
        title = title_font.render("CAPYBARA FISHER", False, white)
        window.blit(title, (x1 + self.text_bounce, y1 + self.text_bounce))
        play_drop_shadow = play_font.render("- press p to play -", False, self.drop_color)
        play_drop_shadow.set_alpha(100)
        play_title = play_font.render("- press p to play -", False, white)

        # Text bounce effect + flashing play title
        if self.i <= 49:
            window.blit(play_drop_shadow, (x2 - 10, y2 - 10))
            window.blit(play_title, (x2, y2))
            self.text_bounce += .1
        if self.i > 49:
            self.text_bounce -= .1
        if self.i >= 99:
            self.i = 0
        self.i += 1

    def level_manager(self, dt):
        if self.state == "menu":
            self.menu()
        if self.state == "level1":
            self.level1(dt)

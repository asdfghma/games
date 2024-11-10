import pygame
from pygame.locals import *
import pygame_menu
import random
import math

pygame.init()


fps = 120

cell_size = 30

top_panel_height = 30


left_mouse_click = 1
right_mouse_click = 3

font = pygame.font.Font(pygame.font.get_default_font(), 18)

clue_colors = [' ', 'blue', 'green', 'red', 'purple', 'turquoise', 'black', 'dimgray']

class Game:

    def __init__(self):
        self.set_difficulty('beginner')
        self.setup_window()

        self.new_game_menu = None
        self.gameover_menu = None
        self.display_new_game_menu()



    def set_difficulty(self, difficulty):
        if difficulty == 'beginner':
            self.size = {'rows': 8, 'cols': 8}
            self.num_mines = 10
        elif difficulty == 'intermediate':
            self.size = {'rows': 16, 'cols': 16}
            self.num_mines = 40
        elif difficulty == 'expert':
            self.size = {'rows': 16, 'cols': 16}
            self.num_mines = 99



    def setup_window(self):
        width = cell_size * self.size['cols']
        height = cell_size * self.size['rows'] + top_panel_height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Minesweeper')

    def new_game(self, difficulty):
        
        self.gameover = False

        self.set_difficulty(difficulty)
        self.setup_window()

        self.cells = dict()
        self.create_cells()

        self.revealed_count = 0

        self.flag_count = 0

        self.time = 0

        self.timer_event = pygame.USEREVENT + 1

        pygame.time.set_timer(self.timer_event, 1000)

        self.new_game_menu.disable()

        if self.gameover_menu is not None:
            self.gameover_menu.disable()





    def display_new_game_menu(self, heading):
        my_theme = pygame_menu.themes.Theme_BLUE
        my_theme.title_font_size = 18
        my_theme.widhet_font_size = 12
        self.new_game_menu = pygame_menu.Menu('New Game', 150, 150, theme = my_theme)
        self.new_game_menu.add.button('Beginner', lambda s=self: s.new_game('beginner'))
        self.new_game_menu.add.button('Intermediate', lambda s=self : s.new_game('intermediate'))
        self.new_game.add.button('Expert', lambda s=self: s.new_game('expert'))
        self.new_game_menu.mainloop(self.window, fps_limit = fps)

    def create_cells(self):
        pass

    def draw_cells(self):
        pass

    def draw_top_pane(self):
        pass

    def get_clicked_cell(self, click_location):
        pass

    def left_click(self, click_location):
        pass

    def right_click(self, click_location):
        pass

    def place_mines(self, clicked_cell):
        pass

    def update_clues(self):
        pass

    def reveal_all_cells(self):
        pass

class Cell(pygame.Rect):

    def __init__(self, row, col):
        pass

    def fraw(self, window):
        pass

    def reveal(self, cells):
        pass


def main():

    game = Game()

    clock = pygame.time.Clock()
    running = True
    while running:

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()

from Grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.__Grid = Grid()  # Private grid
        self.__blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # Private blocks list
        self.__current_block = self.__get_random_block()  # Private current block
        self.__next_block = self.__get_random_block()  # Private next block
        self.game_over = False  # Public game over status
        self.score = 0  # Public score
        self.__rotate_sound = pygame.mixer.music.load("Sounds/rotate.ogg")  # Private sound
        self.__clear_sound = pygame.mixer.music.load("Sounds/clear.ogg")  # Private sound

        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 10
        elif lines_cleared == 2:
            self.score += 200
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    def __get_random_block(self):  # Private method to get a random block
        if len(self.__blocks) == 0:
            self.__blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.__blocks)
        self.__blocks.remove(block)
        return block

    def move_left(self):
        self.__current_block.move(0, -1)
        if self.__block_inside() == False or self.__block_fits() == False:
            self.__current_block.move(0, 1)

    def move_right(self):
        self.__current_block.move(0, 1)
        if self.__block_inside() == False or self.__block_fits() == False:
            self.__current_block.move(0, -1)

    def move_down(self):
        self.__current_block.move(1, 0)
        if self.__block_inside() == False or self.__block_fits() == False:
            self.__current_block.move(-1, 0)
            self.__lock_block()

    def __lock_block(self):  # Private method to lock the block in place
        tiles = self.__current_block.get_cell_positions()
        for position in tiles:
            self.__Grid.grid[position.row][position.column] = self.__current_block.id
        self.__current_block = self.__next_block
        self.__next_block = self.__get_random_block()
        rows_cleared = self.__Grid.clear_full_rows()
        if rows_cleared > 0:
            self.update_score(rows_cleared, 0)
        if self.__block_fits() == False:
            self.game_over = True

    def reset(self):
        self.__Grid.reset()
        self.__blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.__current_block = self.__get_random_block()
        self.__next_block = self.__get_random_block()
        self.score = 0

    def __block_fits(self):  # Private method to check if block fits
        tiles = self.__current_block.get_cell_positions()
        for tile in tiles:
            if self.__Grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.__current_block.rotate()
        if self.__block_inside() == False or self.__block_fits() == False:
            self.__current_block.undo_rotation()

    def __block_inside(self):  # Private method to check if block is inside grid bounds
        tiles = self.__current_block.get_cell_positions()
        for tile in tiles:
            if self.__Grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        self.__Grid.draw(screen)
        self.__current_block.draw(screen, 11, 11)

        if self.__next_block.id == 3:
            self.__next_block.draw(screen, 255, 290)
        elif self.__next_block.id == 4:
            self.__next_block.draw(screen, 255, 280)
        else:
            self.__next_block.draw(screen, 270, 270)

import pygame
from utils import SCREEN_WIDTH, COLS, ROWS, BLOCK_RED, BLOCK_GREEN, BLOCK_BLUE, BG


class Wall:
    def __init__(self, screen):
        self.screen = screen
        self.width = SCREEN_WIDTH // COLS
        self.height = 50

    def create_wall(self):
        self.blocks = []
        # define an empty list for an individual block
        block_individual = []
        for row in range(ROWS):
            # reset the block row list
            block_row = []
            # iterate through each column in that row
            for col in range(COLS):
                # generate x and y position for each block
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                # assign block strength based on row
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                # create a list at this point to store a rect and a color data
                block_individual = [rect, strength]
                # append that individual block to the overall block row
                block_row.append(block_individual)
            # append the row to the full list of blocks
            self.blocks.append(block_row)

    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                # assign color based on block strength
                if block[1] == 3:
                    block_col = BLOCK_BLUE
                elif block[1] == 2:
                    block_col = BLOCK_GREEN
                elif block[1] == 1:
                    block_col = BLOCK_RED
                pygame.draw.rect(self.screen, block_col, block[0])
                pygame.draw.rect(self.screen, BG, block[0], 2)



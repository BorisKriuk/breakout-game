import pygame
from pygame.locals import *
from utils import PADDLE_COL, SCREEN_WIDTH, SCREEN_HEIGHT


class Ball:
    def __init__(self, x, y, screen):
        self.reset(x, y, screen)

    def move(self, player_paddle, wall):
        # collision threshold
        collision_thresh = 5

        # start off with the assumption that the wall has been destroyed completely
        wall_destroyed = 1

        for row_count, row in enumerate(wall.blocks):
            for item_count, item in enumerate(row):
                # check for collision
                if self.rect.colliderect(item[0]):
                    # check if collision was from above
                    if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                        self.speed_y *= (-1)
                    # check if collision was from below
                    if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                        self.speed_y *= (-1)
                    # check if collision was from left
                    if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                        self.speed_x *= (-1)
                    # check if collision was from right
                    if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                        self.speed_x *= (-1)

                    # reduce the block's strength by doing damage to it
                    if wall.blocks[row_count][item_count][1] > 1:
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        wall.blocks[row_count][item_count][0] = (0, 0, 0, 0)

                # check if blocks still exists, in which case the wall is not destroyed
                if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    wall_destroyed = 0
        # after iterating through all the blocks check if the wall is destroyed
        if wall_destroyed == 1:
            self.game_over = 1

        # check for collision with walls
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH:
            self.speed_x *= (-1)

        # check for collisions with top and bottom of the screen
        if self.rect.top < 0:
            self.speed_y *= (-1)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.game_over = -1

        # look for collision with paddle
        if self.rect.colliderect(player_paddle):
            # check if colliding from the top
            if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= (-1)
                self.speed_x += player_paddle.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= (-1)

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over

    def draw(self):
        pygame.draw.circle(self.screen, PADDLE_COL, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(self.screen, PADDLE_COL, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)

    def reset(self, x, y, screen):
        self.screen = screen
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.game_over = 0
        self.speed_max = 5
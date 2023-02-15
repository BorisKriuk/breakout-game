import pygame
from utils import SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, TEXT_COL
from wall_class import Wall
from paddle_class import Paddle
from ball_class import Ball


# function outputting text onto the screen
def draw_text(text, current_font, text_col, x, y):
    img = current_font.render(text, True, text_col)
    screen.blit(img, (x, y))


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout 1.0")

# define font
font = pygame.font.SysFont('Constantia', 30)

# define game variables
clock = pygame.time.Clock()
live_ball = False
game_over = 0

# create the wall
wall = Wall(screen)
wall.create_wall()

# create the paddle
player_paddle = Paddle(screen)

# create the ball
ball = Ball(player_paddle.x + player_paddle.width / 2, player_paddle.y - player_paddle.height, screen)

running = True
while running:

    clock.tick(FPS)

    screen.fill(BG)

    # draw objects
    wall.draw_wall()
    player_paddle.draw()
    ball.draw()

    if live_ball:
        # move objects
        player_paddle.move()
        game_over = ball.move(player_paddle, wall)
        if game_over != 0:
            live_ball = False

    # print player instructions
    if not live_ball:
        if game_over == 0:
            draw_text("CLICK ANYWHERE TO START", font, TEXT_COL, 100, SCREEN_HEIGHT // 2+100)
        elif game_over == 1:
            draw_text("YOU WON!", font, TEXT_COL, 230, SCREEN_HEIGHT // 2 + 50)
            draw_text("CLICK ANYWHERE TO START", font, TEXT_COL, 100, SCREEN_HEIGHT // 2 + 100)
        elif game_over == -1:
            draw_text("YOU LOST!", font, TEXT_COL, 230, SCREEN_HEIGHT // 2 + 50)
            draw_text("CLICK ANYWHERE TO START", font, TEXT_COL, 100, SCREEN_HEIGHT // 2 + 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            ball.reset(player_paddle.x + player_paddle.width / 2, player_paddle.y - player_paddle.height, screen)
            player_paddle.reset(screen)
            wall.create_wall()

    pygame.display.update()

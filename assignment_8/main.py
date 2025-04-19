import pgzrun

from pgzero.screen import Screen
from pygame.surface import Surface

from models.Ball import Ball
from models.Paddle import Paddle

WIDTH = 600
HEIGHT = 600
BACKGROUND_COLOR = (222, 184, 135) # BurlyWood

surface = Surface((WIDTH, HEIGHT))
screen = Screen(surface)

paddle = Paddle(WIDTH, HEIGHT, screen)
ball = Ball(screen)


def draw():
    screen.clear()
    screen.fill(BACKGROUND_COLOR)

    paddle.draw()
    ball.draw()


def update(dt: float):
    paddle.update()
    ball.update(paddle)


pgzrun.go()
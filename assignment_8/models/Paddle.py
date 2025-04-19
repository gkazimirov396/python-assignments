from pgzero.keyboard import keyboard
from pgzero.screen import Screen
from pygame import Rect

from typing import Tuple

class Paddle:
  speed: int = 20
  width: int = 10
  height: int = 100
  x: float
  y: float
  __screen: Screen

  def __init__(self, width: int, height: int, screen: Screen) -> None:
    self.x = width / 2 - self.height / 2
    self.y = height - 20
    self.__screen = screen

  def on_mouse_move(self, position: Tuple[int, int]) -> None:
    pass

  def update(self):
      if keyboard.left:
        self.x -= self.speed
      elif keyboard.right:
        self.x += self.speed

  def draw(self):
    rect = Rect((self.x, self.y), (self.height, self.width))
    self.__screen.draw.filled_rect(rect, "maroon")
    # self.__screen.draw.filled_rect(rect, "maroon")
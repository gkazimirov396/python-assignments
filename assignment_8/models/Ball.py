from pgzero.screen import Screen

from models.Paddle import Paddle

class Ball:
  def __init__(self, screen: Screen) -> None:
    self.radius = 10
    self.x = screen.width / 2
    self.y = screen.height / 2
    self.speed_x = 3
    self.speed_y = -3
    self.__screen = screen

  def paddle_collision(self, x, y, width):
    return self.y + self.radius >= y and self.x >= x and self.x <= x + width

  def update(self, paddle: Paddle):
        self.x += self.speed_x
        self.y += self.speed_y 

        if self.x <= self.radius or self.x >= self.__screen.width - self.radius:
            self.speed_x *= -1

        if self.y <= self.radius:
            self.speed_y *= -1

        if self.y >= self.__screen.height - self.radius:
            self.reset()

        if self.paddle_collision(paddle.x, paddle.y, paddle.height):
            self.speed_y *= -1

  def draw(self):
        self.__screen.draw.filled_circle((self.x, self.y), self.radius, "red")

  def reset(self):
        self.x = self.__screen.width / 2
        self.y = self.__screen.height / 2
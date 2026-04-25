from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('i.png'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

player1 = Player('list2.png', 10, 150, 5, 150, 150)
player2 = Player('list1.png', 550, 150, 5, 150, 150)
ball = GameSprite('frog.png', 350, 250, 0 ,100, 100)

speed_x = 3
speed_y = 3





clock = time.Clock()
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player1.reset()  
        player1.update_left()
        player2.reset()  
        player2.update_right()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 400 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

    display.update()
    clock.tick(60)

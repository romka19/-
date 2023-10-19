#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <=470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class wall(sprite.Sprite):
    def __init__(self,wall_x,wall_y, wall_width,wall_height):
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("лабиринт")
background = transform.scale(image.load("background.jpg"), (700, 500))

final = GameSprite("treasure.png",50,50,0)
hero1 = player("hero.png", 50, 50, 5)
hero2 = Enemy("cyborg.png", 50, 50, 5)
wall1 = wall(200,170,30,180)
wall2 = wall(200,179,30,900)
wall3 = wall(450,1,40,300)

clock = time.Clock()
game = True
speed = 5
x1 = 190
y1 = 80
x2 = 400
y2 = 300

win_width=700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption("Maze")
background = transform.scale(
    image.load("background.jpg"),
    (win_width, win_height)
)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
finish = False
font.init()
font = font.Font(None, 70)
win = font.render(
    'YOU WIN!',True, (255, 215, 0)
)

while game:

    window.blit(background,(0, 0))
    hero1.reset()
    hero2.reset()

    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()

    hero1.update()
    hero2.update()
    keys_pressed = key.get_pressed()


    for e in event.get():
        if e.type == QUIT:
            game = False
      
    if finish != True:
        if sprite.collide_rect(hero1, final):
            window.blit(win,(200, 200))
            finish = True
            money.play()
        window.blit(background,(0, 0))
        hero1.update()
        hero2.update()

        hero1.reset()
        hero2.reset()
        final.reset

        wl.draw_wall

    display.update()
    clock.tick(60)


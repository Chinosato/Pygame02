import pygame as pg
import random

WIDTH = 400
HEIGHT = 300
FPS = 30
# (R, G, B) Color System
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Yellow = (255, 255,0)
ORANGE = (255, 128, 0)

# Define My Sprite class

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.onbottom = True

    def update(self):
        if self.onbottom == True and self.rect.bottom > HEIGHT:
            self.onbottom = False
        if self.onbottom == False and self.rect.top < 0:
            self.onbottom = True
        
        if self.onbottom == True:
            self.rect.y += 5
        if self.onbottom == False:
            self.rect.y -= 5
            
            
            
            
        

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("My Python Project")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
p1 = Player()
all_sprites.add(p1)

#Create Game Loop
running = True
while running:
    clock.tick(FPS)
    #Input (event)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #Update
    all_sprites.update()
    #Render
    screen.fill(GREEN)
    all_sprites.draw(screen)

    pg.display.flip()
pg.quit()
import pygame as pg
import time

class GameSpite(pg.spriteSpite):
    def __init__(self, image, x, y, speed, width, height):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.speed = speed
        #self.width, self.height = pg.
        self.rect = pg.image.get_rect()
        self.rect.x, self.rect.y = x, y
    def draw():
        pass

background = (200, 255, 255)
window_res = (600, 500)
window = pg.display.set_mode(tuple(window_res))
window.fill(background)
window.display.update()
running = True
while running:
    for i in pg.event.get():
        if e.type() == pg.type.QUIT:
            pg.quit()
            running == False
    time.delay(20)

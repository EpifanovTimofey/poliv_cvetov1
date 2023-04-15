import pygame, random

sky = 2
y = random.randint(10, 100)
x2 = random.randint(10, 60)
x1 = random.randint(0, 100 - x2)
rect = pygame.Rect([x1, -y, x2, y])

dx = 100

def pramougolnik():
    global dx
    rect.y += sky
    if rect.top > 500:
        rect.bottom = 0
        rect.w = random.randint(10, 60)
        rect.left = random.randint(0, dx - rect.w)
        rect.h = random.randint(10, 100)
    if rect.bottom > 499:
        dx += 1
import pygame,random
sky = 2
y = random.randint(10, 100)
x1 = random.randint(10, 490)
x2 = random.randint(10, 100)
rect = pygame.Rect([x1, -y, x2, y])
def pramougolnik():
    rect.y += sky
    if rect.top > 500:
        rect.bottom = 0
        rect.left = random.randint(50,450)
        rect.w = random.randint(10, 100)
        rect.h = random.randint(10, 100)
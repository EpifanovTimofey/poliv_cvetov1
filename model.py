import pygame, random

sky = 10
y = random.randint(10, 100)
x2 = random.randint(10, 60)
x1 = random.randint(0, 100 - x2)
rect = pygame.Rect([x1, -y, x2, y])

dx = 100

rectcv1 = pygame.Rect([1, 400, 50, 100])
rectcv2 = pygame.Rect([50, 400, 50, 100])


def pramougolnik():
    global dx, visotacv1
    rect.y += sky
    if rect.top > 500:
        rect.bottom = 0
        rect.w = random.randint(10, 60)
        rect.left = random.randint(0, dx - rect.w)
        rect.h = random.randint(10, 100)
    if rect.bottom > 499:
        dx += 8
        rectcv1.w = dx / 2
        rectcv1.y -= 1
        rectcv1.h += 1

        rectcv2.left = dx / 2
        rectcv2.w = dx / 2
        rectcv2.y -= 1
        rectcv2.h += 1
        pygame.display.set_mode([dx, 500])

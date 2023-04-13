import pygame, model, random


def cveta():
    global r, g, b
    r = random.randint(0, 100)
    g = random.randint(0, 255)
    b = random.randint(0, 255)


a = pygame.display.set_mode([500, 500])

cveta()


def view1():
    global r, g, b
    a.fill([0, 0, 0])
    pygame.draw.rect(a, [r, g, b], model.rect)
    if model.rect.bottom > 500:
        r = 255
        g = 20
        b = 5
    if model.rect.top > 499:
        cveta()
    pygame.display.flip()

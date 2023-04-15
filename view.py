import pygame, model, random


def cveta():
    global r, g, b
    r = random.randint(0, 100)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

a = pygame.display.set_mode([model.dx, 500])

cveta()
kap = pygame.image.load("kaplya.png")


def view1():
    global r, g, b
    pygame.display.set_mode([model.dx, 500])
    if model.rect.top > 499:
        cveta()
    kap1 = pygame.transform.scale(kap, [model.rect.w, model.rect.h])
    a.blit(kap1, [model.rect.x, model.rect.y])
    pygame.display.flip()

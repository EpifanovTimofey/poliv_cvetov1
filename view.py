import pygame, model, random


def cveta():
    global r, g, b
    r = random.randint(0, 100)
    g = random.randint(0, 255)
    b = random.randint(0, 255)


a = pygame.display.set_mode([model.dx, 500])
cveta()

cv1 = pygame.image.load("flower1.png")
cv2 = pygame.image.load("flower2.png")
kap = pygame.image.load("kaplya.png")


def view1():
    global r, g, b

    a.fill([0, 0, 0])
    kap1 = pygame.transform.scale(kap, [model.rect.w, model.rect.h])
    cv_1 = pygame.transform.scale(cv1, model.rectcv1.size)
    cv_2 = pygame.transform.scale(cv2, model.rectcv2.size)
    a.blit(cv_1, model.rectcv1)
    a.blit(cv_2, model.rectcv2)
    a.blit(kap1, model.rect)
    # pygame.draw.rect(a, [255, 255, 255], model.rectcv1, 2)
    # pygame.draw.rect(a, [0, 255, 255], model.rectcv2, 2)
    pygame.display.flip()

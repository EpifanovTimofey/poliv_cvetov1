import random, time, pygame



def cveta():
    global r, g, b
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)


a = pygame.display.set_mode([500, 500])
sky = 1
y = random.randint(10, 100)
x1 = random.randint(10, 490)
x2 = random.randint(10, 100)
re = pygame.Rect([x1, -y, x2, y])

cveta()

while True:
    a.fill([0, 0, 0])
    pygame.event.get()
    time.sleep(1 / 60)
    re.y += sky
    if re.bottom > 500:
        r = 255
        g = 20
        b = 5
    if re.top > 500:
        re.bottom = 0
        re.left = random.randint(50,450)
        re.w = random.randint(10, 100)
        re.h = random.randint(10, 100)
        cveta()
    pygame.draw.rect(a, [r, g, b], re)
    pygame.display.flip()

import pygame

pygame.init()

#making a window
win = pygame.display.set_mode((640, 480))

#window caption
pygame.display.set_caption("The Basic Engine")

#variables
x = 50
y = 50
width = 40
height = 60
vel = 10

run = True
#game loop
while run:
    #delay by 100 miliseconds
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #get input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    #draw rectangle
    pygame.draw.rect(win, (0, 255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit

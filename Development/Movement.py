import pygame

pygame.init()

#display dimensions
display_width = 1200
display_height = 640

#colour
black = (0, 0, 0)
white = (255, 255, 255)
red = (230, 0, 0)
bright_red = (255, 0, 0)
light_brown = (139, 69, 19)
midnight_blue = (25, 25, 112)
grey = (128, 128, 128)
light_grey = (192, 192, 192)
cardboard_brown = (165, 136, 85)
mint_green = (152, 255, 152)
tan = (196,144,124)
peach = (255,224,189)

#player
plx = 500
ply = 250
xmov = 0
ymov = 0
ms = 2


displayScreen = pygame.display.set_mode((display_width,display_height))
pxa = pygame.PixelArray(displayScreen)
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

keys = pygame.key.get_pressed()

def character():
    global plx, ply
    pygame.draw.rect(displayScreen, tan, (plx+8, ply-10, 20, 10))
    head = pygame.draw.ellipse(displayScreen, peach, (plx-7, ply-55, 50, 50))
    pygame.draw.rect(displayScreen, black, (plx+8, ply-32, 4, 8))
    pygame.draw.rect(displayScreen, black, (plx+24, ply-32, 4, 8))
    pygame.draw.rect(displayScreen, black, (plx, ply, 36, 40))
    pygame.draw.rect(displayScreen, red, (plx+10, ply, 16, 40))
    pygame.draw.polygon(displayScreen, black, ((plx,ply),(plx,ply+10),(plx-22,ply+20)))
    pygame.draw.polygon(displayScreen, black, ((plx+36,ply),(plx+36,ply+10),(plx+54,ply+20)))
    pygame.draw.rect(displayScreen, black, (plx+3, ply+40, 10, 30))
    pygame.draw.rect(displayScreen, black, (plx+22, ply+40, 10, 30))
    #pxa[10, 20] = black


  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    xmov = 0
    ymov = 0
    ms = 1


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        xmov = -1
    if keys[pygame.K_d]:
        xmov = 1
    if keys[pygame.K_w]:
        ymov = -1
    if keys[pygame.K_s]:
        ymov = 1


    plx += xmov * ms
    ply += ymov * ms

    displayScreen.fill(white)
    character()
    pygame.display.update()


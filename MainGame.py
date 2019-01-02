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
pygame.display.set_caption('Test')
clock = pygame.time.Clock()


def text_font(font_type, size, bold, italic):
    font = pygame.font.SysFont(font_type, size, bold, italic)
    return font

def displayText(font, message, colour, xcoord, ycoord):
    text = font.render(message, True, colour)
    textRect = text.get_rect()
    textRect.center = ((xcoord), (ycoord))
    displayScreen.blit(text, textRect)

def quit_game():
    pygame.quit()
    quit()

def create_button(colour, hover_colour, button_action, xcoord, ycoord, rectlength, rectwidth, thickness):
    mouse_position = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if xcoord + rectlength > mouse_position[0] > xcoord and ycoord + rectwidth > mouse_position[1] > ycoord: 
        pygame.draw.rect(displayScreen, hover_colour, (xcoord, ycoord, rectlength, rectwidth), thickness)
        if mouse_click[0] == 1:
            if button_action == 'Play':
                menu = False
                main_game()
            elif button_action == 'Instructions':
                menu = False
                instructions()
            elif button_action == 'Quit':
                menu = False
                quit_game()
            elif button_action == 'Main Menu':
                instruction_menu = False
                main_menu()
    else:
        pygame.draw.rect(displayScreen, colour, (xcoord, ycoord, rectlength, rectwidth), thickness)


def character():
    global plx, ply, xmov, ymov
    pygame.draw.rect(displayScreen, tan, (plx+8, ply-10, 20, 10))
    pygame.draw.circle(displayScreen, peach, (plx+18, ply-30), 25)
    pygame.draw.rect(displayScreen, black, (plx+8, ply-32, 4, 8))
    pygame.draw.rect(displayScreen, black, (plx+24, ply-32, 4, 8))
    pygame.draw.rect(displayScreen, black, (plx, ply, 36, 40))
    pygame.draw.rect(displayScreen, red, (plx+10, ply, 16, 40))
    pygame.draw.polygon(displayScreen, black, ((plx,ply),(plx,ply+10),(plx-22,ply+20)))
    pygame.draw.polygon(displayScreen, black, ((plx+36,ply),(plx+36,ply+10),(plx+54,ply+20)))
    pygame.draw.rect(displayScreen, black, (plx+3, ply+40, 10, 30))
    pygame.draw.rect(displayScreen, black, (plx+22, ply+40, 10, 30))
    #pxa[10, 20] = black
    plx += xmov
    ply += ymov
        
        
def main_menu():
    menu = True
    while menu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        displayScreen.fill(white)
        displayText(text_font('microsofthimalaya', 180, False, False),
                    'The Survivor', red, display_width/2, display_height/3 - 40)

        create_button(red, bright_red, 'Play', 420, 320, 360, 30, 0)
        displayText(text_font('microsofthimalaya', 35, True, False),
                    'P L A Y', black, display_width/2, 340)

        create_button(red, bright_red, 'Instructions', 420, 370, 360, 30, 0)
        displayText(text_font('microsofthimalaya', 35, True, False),
                    'I N S T R U C T I O N S', black, display_width/2, 390)

        create_button(red, bright_red, 'Quit', 420, 420, 360, 30, 0)
        displayText(text_font('microsofthimalaya', 35, True, False),
                    'Q U I T', black, display_width/2, 440)
        
        pygame.display.update()
        clock.tick(60)

def instructions():    
    instruction_menu = True
    book_opening = True
    lx = 500
    rx = 720
    uy = 160
    dy = 480
    shadow = 2
    cover_x = 0
    cover_y = 0
    
    while instruction_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
                
        displayScreen.fill(light_brown)

        create_button(white, grey, 'Main Menu', 6, 6, 60, 41, 0)
        pygame.draw.polygon(displayScreen, light_brown, [(7, 27), (7, 26), (25, 7), (25, 20), (66, 20), (66, 6), (6, 6), (6, 47), (66, 47), (66, 20), (64, 20), (64, 34), (25, 34), (25, 46)])
        displayText(text_font('comicsansms', 15, True, False), 'BACK', black, 35, 26)
        
        if book_opening == True:
            pygame.draw.polygon(displayScreen, black, [(lx+shadow, uy+shadow), (lx+shadow, dy+shadow), (rx+shadow, dy+shadow), (rx+shadow, uy+shadow)])
            pygame.draw.polygon(displayScreen, midnight_blue, [(lx, uy), (lx, dy), (rx, dy), (rx, uy)])
            if uy == 20:
                uy += 0
                dy += 0
                if rx == 1100:
                    lx += 0
                    rx += 0
                    shadow = 0
                    pygame.draw.polygon(displayScreen, white, [(600, 22), (600, 618), (1098, 618), (1098, 22)])
                    pygame.draw.polygon(displayScreen, black, [(600, 22), (600, 618), (1098, 618), (1098, 22)], 1)
                    pygame.draw.polygon(displayScreen, midnight_blue, [(600, 20), (600, 620), (1100-cover_x, 620-cover_y), (1100-cover_x, 20-cover_y)])
                    pygame.draw.polygon(displayScreen, black, [(600, 20), (600, 620), (1100-cover_x, 620-cover_y), (1100-cover_x, 20-cover_y)], 1)
                    if cover_x == 1000:
                        cover_x += 0
                    else:
                        cover_x += 8

                    if cover_x < 490:
                        cover_y += 2
                    elif cover_y == 0:
                        cover_y += 0
                    elif cover_x > 490 and cover_x < 510:
                        cover_y += 0
                    elif cover_x > 510:
                        cover_y += -2
                else:
                    lx += 2
                    rx += 2
            else:
                lx -= 2
                rx += 2
                uy -= 2
                dy += 2

        pygame.display.update()
        clock.tick(120)


def starting_area():
    global xmov, ymov, ms
    game = True
    while game :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if ply-54 == 0:
                        ymov = 0
                    else:
                        ymov = -ms
                elif event.key == pygame.K_a:
                    if plx-20 == 0:
                        xmov = 0
                    else:
                        xmov = -ms
                elif event.key == pygame.K_s:
                    if ply+68 == 640:
                        ymov = 0
                    else:
                        ymov = ms
                elif event.key == pygame.K_d:
                    if plx+52 == 1200:
                        xmov = 0
                    else:
                        xmov = ms
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    ymov = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    xmov = 0

        displayScreen.fill(mint_green)
        pygame.draw.polygon(displayScreen, cardboard_brown, ((800, 100), (1200, 100), (1200, 200), (900, 200), (900, 640), (800, 640)))
        character()
        if ply-56 < 0 or ply+70 > display_height:
            ymov = 0
        if plx-22 < 0 or plx+54 > display_width:
            xmov = 0
        pygame.display.update()
        clock.tick(120)

        
def main_game():
    starting_area()

main_menu()

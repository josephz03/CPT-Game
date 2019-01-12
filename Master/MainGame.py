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
green = (0, 255, 0)
light_brown = (139, 69, 19)
midnight_blue = (25, 25, 112)
grey = (128, 128, 128)
light_grey = (192, 192, 192)
cardboard_brown = (165, 136, 85)
mint_green = (152, 255, 152)
tan = (196,144,124)
peach = (255,224,189)
brown = (92, 64, 51)

#player coordinates
plx = 500
ply = 250
xmov = 0
ymov = 0
basic_speed = 2
ms = basic_speed


displayScreen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Survivor')
clock = pygame.time.Clock()
instruction_display = False


def text_font(font_type, size, bold, italic):
    font = pygame.font.SysFont(font_type, size, bold, italic)
    return font

def displayText(animation, font, message, colour, position, xcoord, ycoord):
    if animation == True:
        text = ''
        for i in range(len(message)):
            text += message[i]
            textSurface = font.render(text, True, colour)
            textRect = textSurface.get_rect()
            textRect.midleft = (xcoord, ycoord)
            displayScreen.blit(textSurface, textRect)
            pygame.display.update()
            pygame.time.wait(5)
        animation = False
            
    elif animation == False:
        text = font.render(message, True, colour)
        textRect = text.get_rect()
        if position == 'Center':
            textRect.center = (xcoord, ycoord)
        elif position == 'Midleft':
            textRect.midleft = (xcoord, ycoord)
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
                starting_area()
            elif button_action == 'Manual':
                menu = False
                manual()
            elif button_action == 'Quit':
                menu = False
                quit_game()
            elif button_action == 'Main Menu':
                manual_menu = False
                main_menu()
    else:
        pygame.draw.rect(displayScreen, colour, (xcoord, ycoord, rectlength, rectwidth), thickness)


def instructions(animation):
    global instruction_display
    if instruction_display == True:
        animation = False
    
    displayText(animation, text_font('arial', 25, True, False), 'Instructions', black, 'Midleft', 785, 70)
    displayText(animation, text_font('arial', 25, True, False), 'WASD = controls', black, 'Midleft', 620, 100)
    displayText(animation, text_font('arial', 25, True, False), 'Space = attack/use item', black, 'Midleft', 620, 120)
    displayText(animation, text_font('arial', 25, True, False), 'Shift = sprint', black, 'Midleft', 620, 140)
    displayText(animation, text_font('arial', 25, True, False), 'Inventory = 1-5', black, 'Midleft', 620, 160)
    displayText(animation, text_font('arial', 25, True, False), 'Enter = talk', black, 'Midleft', 620, 180)
    displayText(animation, text_font('arial', 25, True, False), 'Goal', black, 'Midleft', 815, 220)
    displayText(animation, text_font('arial', 25, True, False), '-Kill as many enemies as possible and earn', black, 'Midleft', 620, 265)
    displayText(animation, text_font('arial', 25, True, False), 'rewards!', black, 'Midleft', 627, 284)
    displayText(animation, text_font('arial', 25, True, False), '-Killing enemies will drop materials and', black, 'Midleft', 620, 312)
    displayText(animation, text_font('arial', 25, True, False), 'use materials to upgrade yourself!', black, 'Midleft', 627, 334)
    displayText(animation, text_font('arial', 25, True, False), '-The more you explore, the more you will find', black, 'Midleft', 620, 362)
    displayText(animation, text_font('arial', 25, True, False), 'upgrades and side quest!', black, 'Midleft', 627, 384)
    displayText(animation, text_font('arial', 25, True, False), '-To win the game, you will need to kill the boss', black, 'Midleft', 620, 412)
    displayText(animation, text_font('arial', 25, True, False), 'and all the enemies will leave the world :)', black, 'Midleft', 627, 434)



def character(charpos):
    global plx, ply
    if charpos == 'Down':
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
        
    elif charpos == 'Left':
        pygame.draw.rect(displayScreen, tan, (plx+12, ply-10, 13, 10))
        pygame.draw.circle(displayScreen, peach, (plx+18, ply-30), 25)
        pygame.draw.rect(displayScreen, black, (plx+4, ply-32, 4, 8))
        pygame.draw.rect(displayScreen, black, (plx+10, ply, 18, 40))
        pygame.draw.polygon(displayScreen, black, ((plx+10,ply),(plx+10,ply+10),(plx-22,ply+20)))
        pygame.draw.rect(displayScreen, black, (plx+12, ply+40, 13, 30))
        
    elif charpos == 'Right':
        pygame.draw.rect(displayScreen, tan, (plx+12, ply-10, 13, 10))
        pygame.draw.circle(displayScreen, peach, (plx+18, ply-30), 25)
        pygame.draw.rect(displayScreen, black, (plx+28, ply-32, 4, 8)) 
        pygame.draw.rect(displayScreen, black, (plx+10, ply, 18, 40))
        pygame.draw.polygon(displayScreen, black, ((plx+28,ply),(plx+28,ply+10),(plx+54,ply+20))) 
        pygame.draw.rect(displayScreen, black, (plx+12, ply+40, 13, 30))

    elif charpos == 'Up':
        pygame.draw.rect(displayScreen, tan, (plx+8, ply-10, 20, 10))
        pygame.draw.circle(displayScreen, peach, (plx+18, ply-30), 25)
        pygame.draw.rect(displayScreen, black, (plx, ply, 36, 40))
        pygame.draw.polygon(displayScreen, black, ((plx,ply),(plx,ply+10),(plx-22,ply+20)))
        pygame.draw.polygon(displayScreen, black, ((plx+36,ply),(plx+36,ply+10),(plx+54,ply+20)))
        pygame.draw.rect(displayScreen, black, (plx+3, ply+40, 10, 30))
        pygame.draw.rect(displayScreen, black, (plx+22, ply+40, 10, 30))
    

def tree(tree_coordinates):
    leaves = [(35, 60), (5, 60), (65, 30), (20, 30), (-25, 30), (35, 0), (5, 0)]
    for i in range(len(tree_coordinates)):
        pygame.draw.rect(displayScreen, brown, (tree_coordinates[i][0], tree_coordinates[i][1], 40, 100))
        for leaf in range(len(leaves)):
            pygame.draw.circle(displayScreen, green, (tree_coordinates[i][0]+leaves[leaf][0],tree_coordinates[i][1]-leaves[leaf][1]), 30)

    
        
def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        displayScreen.fill(white)
        displayText(False, text_font('microsofthimalaya', 180, False, False),
                    'The Survivor', red, 'Center', display_width/2, display_height/3 - 40)

        create_button(red, bright_red, 'Play', 420, 320, 360, 30, 0)
        displayText(False, text_font('microsofthimalaya', 35, True, False),
                    'P L A Y', black, 'Center', display_width/2, 340)

        create_button(red, bright_red, 'Manual', 420, 370, 360, 30, 0)
        displayText(False, text_font('microsofthimalaya', 35, True, False),
                    'M A N U A L', black, 'Center', display_width/2, 390)

        create_button(red, bright_red, 'Quit', 420, 420, 360, 30, 0)
        displayText(False, text_font('microsofthimalaya', 35, True, False),
                    'Q U I T', black, 'Center', display_width/2, 440)
        
        pygame.display.update()


def manual():
    global instruction_display
    manual_menu = True
    book_opening = True
    instruction_display = False
    leftx = 500
    rightx = 720
    upy = 160
    downy = 480
    shadow = 2
    cover_x = 0
    cover_y = 0
    
    while manual_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
                
        displayScreen.fill(light_brown)

        create_button(white, grey, 'Main Menu', 6, 6, 60, 41, 0)
        pygame.draw.polygon(displayScreen, light_brown, [(7, 27), (7, 26), (25, 7), (25, 20), (66, 20), (66, 6), (6, 6), (6, 47), (66, 47), (66, 20), (64, 20), (64, 34), (25, 34), (25, 46)])
        displayText(False, text_font('arial', 15, True, False), 'BACK', black, 'Center', 35, 26)

        
        if book_opening == True:
            pygame.draw.polygon(displayScreen, black, [(leftx+shadow, upy+shadow), (leftx+shadow, downy+shadow), (rightx+shadow, downy+shadow), (rightx+shadow, upy+shadow)])
            pygame.draw.polygon(displayScreen, midnight_blue, [(leftx, upy), (leftx, downy), (rightx, downy), (rightx, upy)])
            if upy == 20:
                upy += 0
                downy += 0
                if rightx == 1100:
                    leftx += 0
                    rightx += 0
                    shadow = 0
                    pygame.draw.polygon(displayScreen, white, [(600, 22), (600, 618), (1098, 618), (1098, 22)])
                    pygame.draw.polygon(displayScreen, black, [(600, 22), (600, 618), (1098, 618), (1098, 22)], 1)
                    
                    pygame.draw.polygon(displayScreen, midnight_blue, [(600, 20), (600, 620), (1100-cover_x, 620-cover_y), (1100-cover_x, 20-cover_y)])
                    pygame.draw.polygon(displayScreen, black, [(600, 20), (600, 620), (1100-cover_x, 620-cover_y), (1100-cover_x, 20-cover_y)], 1)

                    if cover_x == 1000:
                        cover_x += 0                    
                        instructions(True)
                        instruction_display = True
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
                    leftx += 2
                    rightx += 2
            else:
                leftx -= 2
                rightx += 2
                upy -= 2
                downy += 2

        pygame.display.update()
        


def starting_area():
    global plx, ply, mov, ymov, ms
    charpos = 'Down'
    tree_coordinates = [(265, 400), (100, 230), (700, 100)]
    game = True
    while game :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        xmov = 0
        ymov = 0
        ms = 2

        if pygame.key.get_mods() == pygame.KMOD_LSHIFT:
            ms = 3

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            charpos = 'Up'
            if ply-54 <= 0:
                ymov = 0
            else:
                ymov = -1
        if keys[pygame.K_a]:
            charpos = 'Left'
            if plx-20 <= 0:
                xmov = 0
            else:
                xmov = -1
        if keys[pygame.K_s]:
            charpos = 'Down'
            if ply+68 >= 640:
                ymov = 0
            else:
                ymov = 1
        if keys[pygame.K_d]:
            charpos = 'Right'
            if plx+52 >= 1200:
                xmov = 0
            else:
                xmov = 1

        plx += xmov * ms
        ply += ymov * ms


        displayScreen.fill(mint_green)
        pygame.draw.polygon(displayScreen, cardboard_brown, ((800, 100), (1200, 100), (1200, 200), (900, 200), (900, 640), (800, 640)))

        tree(tree_coordinates)
        
        character(charpos)
            
        pygame.display.update()
        clock.tick(120)



main_menu()

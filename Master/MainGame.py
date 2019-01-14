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

#player info
plx = 500
ply = 250
maxhealth = 100
current_health = 100

paused = False
instruction_display = False


displayScreen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Survivor')
clock = pygame.time.Clock()


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


def create_button(colour, hover_colour, button_action, xcoord, ycoord, rectlength, rectwidth, loop, drawtype):
    global paused
    mouse_position = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if xcoord + rectlength > mouse_position[0] > xcoord and ycoord + rectwidth > mouse_position[1] > ycoord:
        if drawtype == 'rectangle':
            pygame.draw.rect(displayScreen, hover_colour, (xcoord, ycoord, rectlength, rectwidth))
        elif drawtype == 'blit':
            blitrect = pygame.Surface((rectlength, rectwidth))
            blitrect.set_alpha(150)
            blitrect.fill(hover_colour)
            displayScreen.blit(blitrect, (xcoord, ycoord))
            
        if mouse_click[0] == 1:
            if button_action == 'Play':
                loop = False
                start_area()
            elif button_action == 'Manual':
                loop = False
                manual()
            elif button_action == 'Quit':
                loop = False
                quit_game()
            elif button_action == 'Main Menu':
                loop = False
                main_menu()
            elif button_action == 'Resume':
                paused = False

    else:
        if drawtype == 'rectangle':
            pygame.draw.rect(displayScreen, colour, (xcoord, ycoord, rectlength, rectwidth))
        elif drawtype == 'blit':
            blitrect = pygame.Surface((rectlength, rectwidth))
            blitrect.set_alpha(150)
            blitrect.fill(colour)
            displayScreen.blit(blitrect, (xcoord, ycoord))


def back_button(loop):
    global paused
    if paused:
        create_button(white, grey, 'Play', 6, 6, 60, 41, loop, 'rectangle')
    else:
        create_button(white, grey, 'Main Menu', 6, 6, 60, 41, loop, 'rectangle')
    pygame.draw.polygon(displayScreen, light_brown, [(7, 27), (7, 26), (25, 7), (25, 20), (66, 20), (66, 6), (6, 6), (6, 47), (66, 47), (66, 20), (64, 20), (64, 34), (25, 34), (25, 46)])
    displayText(False, text_font('arial', 15, True, False), 'BACK', black, 'Center', 35, 26)

def health_bar():
    health_bar = pygame.Surface((maxhealth*3, 20))
    health_bar.set_alpha(100)
    health_bar.fill(black)
    displayScreen.blit(health_bar, (20, 20))

    health = pygame.Surface((current_health*3, 20))
    health.set_alpha(180)
    health.fill(red)
    displayScreen.blit(health, (20, 20))

    pygame.draw.rect(displayScreen, white, (20, 20, maxhealth*3, 20), 1)
    displayText(False, text_font('microsofthimalaya', 30, False, True),
                    '{}'.format(current_health), white, 'Center', 40, 33)


def pause(loop):
    if paused:
        pauseDisplay = pygame.Surface((display_width, display_height))
        pauseDisplay.set_alpha(60)
        pauseDisplay.fill(black)
        displayScreen.blit(pauseDisplay, (0,0))

        displayText(False, text_font('microsofthimalaya', 160, False, False),
                    'PAUSED', white, 'Center', display_width/2, display_height/3 - 40)
        create_button(grey, light_grey, 'Resume', 420, 290, 360, 30, loop, 'blit')
        displayText(False, text_font('microsofthimalaya', 35, True, False),
                    'Resume', white, 'Center', display_width/2, 310)
        create_button(grey, light_grey, 'Manual', 420, 340, 360, 30, loop, 'blit')
        displayText(False, text_font('microsofthimalaya', 35, True, False),
                    'Instructions', white, 'Center', display_width/2, 360)
        create_button(grey, light_grey, 'Main Menu', 420, 390, 360, 30, loop, 'blit')
        displayText(False, text_font('microsofthimalaya', 35, True, False),
                    'Main Menu', white, 'Center', display_width/2, 410)
        

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
    

def npc(xloc, yloc, charpos, eye_colour, skin_colour, shadow_skin_colour, shirt_colour, shirt_colour2, pants_colour):
    if charpos == 'Down':
        pygame.draw.rect(displayScreen, shadow_skin_colour, (xloc+8, yloc-10, 20, 10))
        pygame.draw.circle(displayScreen, skin_colour, (xloc+18, yloc-30), 25)
        pygame.draw.rect(displayScreen, eye_colour, (xloc+8, yloc-32, 4, 8))
        pygame.draw.rect(displayScreen, eye_colour, (xloc+24, yloc-32, 4, 8))
        pygame.draw.rect(displayScreen, shirt_colour, (xloc, yloc, 36, 40))
        pygame.draw.rect(displayScreen, shirt_colour2, (xloc+10, yloc, 16, 40))
        pygame.draw.polygon(displayScreen, shirt_colour, ((xloc,yloc),(xloc,yloc+10),(xloc-22,yloc+20)))
        pygame.draw.polygon(displayScreen, shirt_colour, ((xloc+36,yloc),(xloc+36,yloc+10),(xloc+54,yloc+20)))
        pygame.draw.rect(displayScreen, pants_colour, (xloc+3, yloc+40, 10, 30))
        pygame.draw.rect(displayScreen, pants_colour, (xloc+22, yloc+40, 10, 30))
        
    elif charpos == 'Left':
        pygame.draw.rect(displayScreen, shadow_skin_colour, (xloc+12, yloc-10, 13, 10))
        pygame.draw.circle(displayScreen, skin_colour, (xloc+18, yloc-30), 25)
        pygame.draw.rect(displayScreen, eye_colour, (xloc+4, yloc-32, 4, 8))
        pygame.draw.rect(displayScreen, shirt_colour, (xloc+10, yloc, 18, 40))
        pygame.draw.polygon(displayScreen, shirt_colour, ((xloc+10,yloc),(xloc+10,yloc+10),(xloc-22,yloc+20)))
        pygame.draw.rect(displayScreen, pants_colour, (xloc+12, yloc+40, 13, 30))
        
    elif charpos == 'Right':
        pygame.draw.rect(displayScreen, shadow_skin_colour, (xloc+12, yloc-10, 13, 10))
        pygame.draw.circle(displayScreen, skin_colour, (xloc+18, yloc-30), 25)
        pygame.draw.rect(displayScreen, eye_colour, (xloc+28, yloc-32, 4, 8)) 
        pygame.draw.rect(displayScreen, shirt_colour, (xloc+10, yloc, 18, 40))
        pygame.draw.polygon(displayScreen, shirt_colour, ((xloc+28,yloc),(xloc+28,yloc+10),(xloc+54,yloc+20))) 
        pygame.draw.rect(displayScreen, pants_colour, (xloc+12, yloc+40, 13, 30))

    elif charpos == 'Up':
        pygame.draw.rect(displayScreen, shadow_skin_colour, (xloc+8, yloc-10, 20, 10))
        pygame.draw.circle(displayScreen, skin_colour, (xloc+18, yloc-30), 25)
        pygame.draw.rect(displayScreen, shirt_colour, (xloc, xloc, 36, 40))
        pygame.draw.polygon(displayScreen, shirt_colour, ((xloc,yloc),(xloc,yloc+10),(xloc-22,yloc+20)))
        pygame.draw.polygon(displayScreen, shirt_colour, ((xloc+36,yloc),(xloc+36,yloc+10),(xloc+54,yloc+20)))
        pygame.draw.rect(displayScreen, pants_colour, (xloc+3, yloc+40, 10, 30))
        pygame.draw.rect(displayScreen, pants_colour, (xloc+22, yloc+40, 10, 30))

        
def tree(tree_coordinates):
    leaves = [(35, 60), (5, 60), (65, 30), (20, 30), (-25, 30), (35, 0), (5, 0)]
    for i in range(len(tree_coordinates)):
        pygame.draw.rect(displayScreen, brown, (tree_coordinates[i][0], tree_coordinates[i][1], 40, 100))
        for leaf in range(len(leaves)):
            pygame.draw.circle(displayScreen, green, (tree_coordinates[i][0]+leaves[leaf][0],tree_coordinates[i][1]-leaves[leaf][1]), 30)

                    
def main_menu():
    global paused
    paused = False
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        displayScreen.fill(white)
        displayText(False, text_font('microsofthimalaya', 180, False, False),
                    'The Survivor', red, 'Center', display_width/2, display_height/3 - 40)

        create_button(red, bright_red, 'Play', 420, 320, 360, 30, menu, 'rectangle')
        displayText(False, text_font('microsofthimalaya', 35, True, False),
                    'P L A Y', black, 'Center', display_width/2, 340)

        create_button(red, bright_red, 'Manual', 420, 370, 360, 30, menu, 'rectangle')
        displayText(False, text_font('microsofthimalaya', 35, True, False),
                    'M A N U A L', black, 'Center', display_width/2, 390)

        create_button(red, bright_red, 'Quit', 420, 420, 360, 30, menu, 'rectangle')
        displayText(False, text_font('microsofthimalaya', 35, True, False),
                    'Q U I T', black, 'Center', display_width/2, 440)
        pygame.display.update()


def manual():
    global instruction_display, paused
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

        back_button(manual_menu)

        #book animation
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
        


def start_area():
    global plx, ply, paused, current_health
    charpos = 'Down'
    tree_coords = [(265, 400), (80, 230), (540, 100)]
    starting_area = True
    
    while starting_area:
        xmov = 0
        ymov = 0
        ms = 3
        damaged = 0
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if paused:
                        paused = False
                    else:
                        paused = True

        if pygame.key.get_mods() == pygame.KMOD_LSHIFT:
            ms = 5
            
        if keys[pygame.K_w]:
            if not paused:
                charpos = 'Up'
                if ply-58 <= 0:
                    ymov = 0
                else:
                    ymov = -1                  
        if keys[pygame.K_s]:
            if not paused:
                charpos = 'Down'
                if ply+68 >= 640 and plx not in range(596, 669):
                    ymov = 0
                elif ply >= 130 and plx+52 > 1200:
                    ymov = 0
                else:
                    ymov = 1

            if ply >= 675:
                starting_area = False
                ply = 40
                fight_area_1()

        if keys[pygame.K_a]:
            if not paused:
                charpos = 'Left'
                if plx-20 <= 0:
                    xmov = 0
                elif plx <= 596 and ply+68 > 640:
                    xmov = 0
                else:
                    xmov = -1
                
        if keys[pygame.K_d]:
            if not paused:
                charpos = 'Right'
                if plx+52 >= 1200 and ply > 130:
                    xmov = 0
                elif plx >= 668 and ply+68 > 640:
                    xmov = 0                  
                else:
                    xmov = 1

        plx += xmov * ms
        ply += ymov * ms

        displayScreen.fill(mint_green)
        pygame.draw.rect(displayScreen, cardboard_brown, (600, 110, 100, 640))
        pygame.draw.rect(displayScreen, cardboard_brown, (700, 110, 500, 100))

        #use class
        if ply-30 <= tree_coords[0][1] and plx in range(tree_coords[0][0]-110, tree_coords[0][0]+116):
            character(charpos)
            tree(tree_coords)
        elif ply-30 <= tree_coords[1][1] and plx in range(tree_coords[1][0]-110, tree_coords[1][0]+116):
            character(charpos)
            tree(tree_coords)
        elif ply-30 <= tree_coords[2][1] and plx in range(tree_coords[2][0]-110, tree_coords[2][0]+116):
            character(charpos)
            tree(tree_coords)
        else:
            tree(tree_coords)
            character(charpos)
        
        current_health -= damaged
        health_bar()
        
        pause(starting_area)
        pygame.display.update()
        clock.tick(60)


def fight_area_1():
    global plx, ply, paused, current_health
    charpos = 'Down'
    tree_coords = [(300, 550), (850, 100)]
    area1 = True
    
    while area1:
        xmov = 0
        ymov = 0
        ms = 3
        damaged = 0
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if paused:
                        paused = False
                    else:
                        paused = True

        if pygame.key.get_mods() == pygame.KMOD_LSHIFT:
            ms = 5
        if keys[pygame.K_w]:
            if not paused:
                charpos = 'Up'
                if ply-58 <= 0 and plx not in range(596, 669):
                    ymov = 0
                else:
                    ymov = -1

                if ply <= 0:
                    area1 = False
                    ply = 640
                    start_area()
                    
        if keys[pygame.K_s]:
            if not paused:
                charpos = 'Down'
                if ply+68 >= 640 and plx not in range(596, 669):
                    ymov = 0
                elif ply >= 130 and plx+52 > 1200:
                    ymov = 0
                else:
                    ymov = 1

            if ply >= 675:
                starting_area = False
                ply = 40
                town()

        if keys[pygame.K_a]:
            if not paused:
                charpos = 'Left'
                if plx-20 <= 0:
                    xmov = 0
                elif plx <= 596 and ply < 56:
                    xmov = 0
                else:
                    xmov = -1

        if keys[pygame.K_d]:
            if not paused:
                charpos = 'Right'
                if plx+52 >= 1200:
                    xmov = 0
                elif plx >= 668 and ply < 56:
                    xmov = 0
                else:
                    xmov = 1

        plx += xmov * ms
        ply += ymov * ms

        displayScreen.fill(mint_green)
        pygame.draw.rect(displayScreen, cardboard_brown, (600, 0, 100, 640))
        pygame.draw.rect(displayScreen, cardboard_brown, (700, 200, 500, 100))
        
        pygame.draw.polygon(displayScreen, cardboard_brown,[(70,100), (50,160), (300,260), (320,200)])
        
        tree(tree_coords)
        
        character(charpos)
        current_health -= damaged
        health_bar()
        
        pause(area1)  
        pygame.display.update()
        clock.tick(60)


def town():
    global plx, ply, paused, current_health
    charpos = 'Down'
    tree_coords = [(300, 550), (850, 100)]
    town_area = True
    
    while town_area:
        xmov = 0
        ymov = 0
        ms = 3
        damaged = 0
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if paused:
                        paused = False
                    else:
                        paused = True

        if pygame.key.get_mods() == pygame.KMOD_LSHIFT:
            ms = 5
        if keys[pygame.K_w]:
            if not paused:
                charpos = 'Up'
                if ply-58 <= 0 and plx not in range(596, 669):
                    ymov = 0
                else:
                    ymov = -1

                if ply <= 0:
                    area1 = False
                    ply = 640
                    fight_area_1()
                    
        if keys[pygame.K_s]:
            if not paused:
                charpos = 'Down'
                if ply+68 >= 640:
                    ymov = 0
                else:
                    ymov = 1

        if keys[pygame.K_a]:
            if not paused:
                charpos = 'Left'
                if plx-20 <= 0:
                    xmov = 0
                elif plx <= 596 and ply < 56:
                    xmov = 0
                else:
                    xmov = -1

        if keys[pygame.K_d]:
            if not paused:
                charpos = 'Right'
                if plx+52 >= 1200:
                    xmov = 0
                elif plx >= 668 and ply < 56:
                    xmov = 0
                else:
                    xmov = 1

        plx += xmov * ms
        ply += ymov * ms

        displayScreen.fill(mint_green)
        pygame.draw.rect(displayScreen, grey, (500, 0, 200, 640))
        pygame.draw.rect(displayScreen, cardboard_brown, (0, 130, 130, 100))
        npc(50, 200, 'Right', black, peach, tan, red, red, black)
        pygame.draw.rect(displayScreen, grey, (0, 230, 130, 50))
        pygame.draw.rect(displayScreen, grey, (0, 80, 130, 50))
        pygame.draw.rect(displayScreen, grey, (130, 80, 3, 200))

        pygame.draw.rect(displayScreen, cardboard_brown, (0, 400, 130, 100))
        npc(50, 470, 'Right', black, peach, tan, red, red, black)
        pygame.draw.rect(displayScreen, grey, (0, 500, 130, 50))
        pygame.draw.rect(displayScreen, grey, (0, 350, 130, 50))
        pygame.draw.rect(displayScreen, grey, (130, 350, 3, 200))

        pygame.draw.rect(displayScreen, cardboard_brown, (1070, 130, 130, 100))
        npc(1150, 200, 'Left', black, peach, tan, red, red, black)
        pygame.draw.rect(displayScreen, grey, (1070, 230, 130, 50))
        pygame.draw.rect(displayScreen, grey, (1070, 80, 130, 50))
        pygame.draw.rect(displayScreen, grey, (1070, 80, 3, 200))

        pygame.draw.rect(displayScreen, cardboard_brown, (1070, 400, 130, 100))
        npc(1150, 470, 'Left', black, peach, tan, red, red, black)
        pygame.draw.rect(displayScreen, grey, (1070, 500, 130, 50))
        pygame.draw.rect(displayScreen, grey, (1070, 350, 130, 50))
        pygame.draw.rect(displayScreen, grey, (1070, 350, 3, 200))
        
        tree(tree_coords)
        
        character(charpos)
        current_health -= damaged
        health_bar()
        
        pause(town_area)  
        pygame.display.update()
        clock.tick(60)
        

main_menu()

import pygame

pygame.init()

#display dimensions
display_width = 1200
display_height = 640

#colour
black = (0, 0, 0)
white = (255, 255, 255)

paused = False

displayScreen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Survivor')
clock = pygame.time.Clock()

def pause():
    if paused:
        pauseDisplay = pygame.Surface((display_width, display_height))
        pauseDisplay.set_alpha(100)
        pauseDisplay.fill(black)
        displayScreen.blit(pauseDisplay, (0,0))#tuple based on starting coord of rect (top-left corner)

        
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #escape key to open pause menu
                if paused:
                    paused = False
                else:
                    paused = True



    displayScreen.fill(white)
    
    pause()
    pygame.display.update()
    clock.tick(120)

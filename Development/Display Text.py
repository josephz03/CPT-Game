import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

displayScreen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()
running = True


def text_font(font_type, size, bold, italic):
    font = pygame.font.SysFont(font_type, size, bold, italic)
    return font

def displayText(font, message, colour, xcoord, ycoord):
    text = font.render(message, True, colour)
    textRect = text.get_rect()
    textRect.center = ((xcoord), (ycoord))
    displayScreen.blit(text, textRect)
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        
    displayScreen.fill(white)
    displayText(text_font('microsofthimalaya', 155, False, False), 'Hi', black, display_width/2, display_height/2)
    
    pygame.display.update()
    clock.tick(60)

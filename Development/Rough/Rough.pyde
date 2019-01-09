page = 0
plx = 500
ply = 250
xmov = 0
ymov = 0


def setup():
    fullScreen()
    background(165,42,42)

def main_menu():
    global page
    if page == 0:
        textSize(200)
        fill(0)
        text("THE", 100, 200)
        text("SURVIVOR", 300, 400)
        #start button
        fill(139, 0, 0)
        rect(width/2-150, 450, 300, 100)
        textSize(100)
        fill(0)
        text("PLAY", 570, 535)
        if mousePressed:
            if mouseX > 550 and mouseX < 550+ 300 and mouseY > 450 and mouseY < 450+100:
                page = 1


def start_area():
    global page
    if page == 1:
        background(34,139,34)
        fill(87,59,12)
        rect(400, 200, 150, height-200)
        rect(550, 200, width-550, 150)

def character():
    global plx, ply, xmov, ymov
    if page == 1:
        fill(0)
        ellipse(plx, ply, 40, 40)
        plx = plx + xmov
        ply = ply +ymov


def draw():
    global page
    noStroke()
    main_menu()
    start_area()
    character()
    
    
def keyPressed():
    global xmov, ymov
    if keyCode == UP:
        ymov = -10
    if keyCode == LEFT:
        xmov = -10
    if keyCode == DOWN:
        ymov = 10
    if keyCode == RIGHT:
        xmov = 10
        
def keyReleased():
    global xmov, ymov
    if keyCode == UP:
        ymov = 0
    if keyCode == LEFT:
        xmov = 0
    if keyCode == DOWN:
        ymov = 0
    if keyCode == RIGHT:
        xmov = 0

x = 500
y = 300
xmov = 0
ymov = 0
ms = 4
monx = 100
mony = 100
spotplayer = False

def character():
    fill(255, 0, 0)
    rect(x, y, 20, 20)

def monster():
    fill(0)
    rect(monx, mony, 20, 20)

def setup():
    size(800, 640)
    
def draw():
    global x, y, xmov, ymov, ms, monx, mony, spotplayer
    background(255)
    rectMode(CENTER)
    x += xmov * ms
    y += ymov * ms
    if y in range(monx-10, monx+11) or x in range(mony-10, mony+11):
        spotplayer = True

    if spotplayer:
        if x-25 > monx:
            monx += 2
        if x+25 < monx:
            monx += -2
        if y-25 > mony:
            mony += 2
        if y+25 < mony:
            mony += -2
    character()
    monster()

def keyPressed():
    global xmov, ymov
    if keyCode == UP:
        ymov = -1
    if keyCode == LEFT:
        xmov = -1
    if keyCode == DOWN:
        ymov = 1
    if keyCode == RIGHT:
        xmov = 1

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

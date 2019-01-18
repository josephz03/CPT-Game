x = 500
y = 300
xmov = 0
ymov = 0
ms = 4
monx = [100, 150]
mony = [100, 150]
monstermov = True
spotplayer = False

def character():
    fill(255, 0, 0)
    rect(x, y, 20, 20)

def monster(i):
    global spotplayer, monstermov
    fill(0)
    rect(monx[i], mony[i], 20, 20)
    if y in range(monx[i]-10, monx[i]+11) or x in range(mony[i]-10, mony[i]+11):
        spotplayer = True
    if len([i for i,e in enumerate(monx) if e==monx[i]]) >= 2 and len([i for i,f in enumerate(mony) if f==mony[i]]) >= 2:
        print(True)
    if spotplayer and monstermov:
        if x-25 > monx[i]:
            monx[i] += 2
        if x+25 < monx[i]:
            monx[i] += -2
        if y-25 > mony[i]:
            mony[i] += 2
        if y+25 < mony[i]:
            mony[i] += -2

def setup():
    size(800, 640)
    
def draw():
    global x, y, xmov, ymov, ms, monx, mony, spotplayer
    background(255)
    rectMode(CENTER)
    x += xmov * ms
    y += ymov * ms
    character()
    monster(0)
    monster(1)

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

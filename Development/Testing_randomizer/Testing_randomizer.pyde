x = 500
y = 300
xmov = 0
ymov = 0
ms = 4
xlist = []
ylist = []
collided = False
delobject = False
timer = 0

def character():
    fill(200)
    rect(x, y, 20, 20)

def circles():
    global xlist, ylist, collided, delobject, timer, x, y
    while len(xlist) < 4:
        xlist.append(round(random(200, 400), 0))
        ylist.append(round(random(-200, 0), 0))
        
    for i in range(len(xlist)):
        fill(0)
        ellipse(xlist[i], ylist[i], 10, 10)
        if ylist[i] > 700:
            if ylist[i] == min(ylist):
                delobject = True
                break
        else:
            if not collided:
                if y in range(int(ylist[i]-20), int(ylist[i]+21)) and x in range(int(xlist[i]-20), int(xlist[i]+21)):
                    collided = True
                else:
                    ylist[i] += 2
            else:
                ylist[i] += 0
            
    if delobject:
        if timer == 40:
            del xlist[:]
            del ylist[:]
            timer = 0
            delobject = False
        else:
            timer += 0.5
           
def collision_message():
    global collided
    if collided:
        textSize(100)
        fill(255, 0, 0)
        text('You Lost', 190, 300)

def setup():
    size(800, 600)

def draw():
    global xlist, ylist, colided, x, y, xmov, ymov, ms
    background(255)
    ellipseMode(RADIUS)
    rectMode(CENTER)
    circles()
    x += xmov * ms
    y += ymov * ms
    character()
    collision_message()

def keyPressed():
    global xmov, ymov, collided
    if keyCode == UP:
        if not collided:
            ymov = -1
    if keyCode == LEFT:
        if not collided:
            xmov = -1
    if keyCode == DOWN:
        if not collided:
            ymov = 1
    if keyCode == RIGHT:
        if not collided:
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

    

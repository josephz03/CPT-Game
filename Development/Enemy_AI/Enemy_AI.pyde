x = 500
y = 300
xmov = 0
ymov = 0
ms = 4
moninfo = [[100, 100, 100], [150, 150, 100]]
monstermov = True
spotplayer = False
direction = 'N/A'
block = 'N/A'

def character():
    fill(255, 0, 0)
    rect(x, y, 20, 20)

def monster():
    global spotplayer, direction, moninfo, block
    for i in range(len(moninfo)):
        if moninfo[i][2] > 0:
            if i == 0:
                followx = x
                followy = y
            else:
                followx = moninfo[i-1][0]
                followy = moninfo[i-1][1]
            fill(0)
            rect(moninfo[i][0], moninfo[i][1], 20, 20)
            if y in range(moninfo[i][0]-10, moninfo[i][0]+11) or x in range(moninfo[i][1]-10, moninfo[i][1]+11):
                spotplayer = True
                
            if spotplayer:
                if moninfo[i][0] == x and moninfo[i][1] in range(y-50, y):
                    block = 'up'
                elif moninfo[i][0] == x and moninfo[i][1] in range(y, y+50):
                    block = 'down'
                elif moninfo[i][1] == y and moninfo[i][0] in range (x-50, x):
                    block = 'left'
                elif moninfo [i][1] == y and moninfo[i][0] in range(x, x+50):
                    block = 'right'
                else:
                    block = 'N/A'
                    
                if direction == 'y':
                    if followx > moninfo[i][0]:
                        moninfo[i][0] += 2
                    elif followx < moninfo[i][0]:
                        moninfo[i][0] += -2
                    if followy-25 > moninfo[i][1]:
                        moninfo[i][1] += 2
                    elif followy+25 < moninfo[i][1]:
                        moninfo[i][1] += -2
                elif direction == 'x':
                    if followx-25 > moninfo[i][0]:
                        moninfo[i][0] += 2
                    elif followx+25 < moninfo[i][0]:
                        moninfo[i][0] += -2
                    if followy > moninfo[i][1]:
                        moninfo[i][1] += 2
                    elif followy < moninfo[i][1]:
                        moninfo[i][1] += -2
        else:
            moninfo.pop(i)


def setup():
    size(800, 640)
    
def draw():
    global x, y, xmov, ymov, ms, moninfo, spotplayer
    background(255)
    rectMode(CENTER)
    x += xmov * ms
    y += ymov * ms
    character()
    monster()


def keyPressed():
    global xmov, ymov, direction, block
    if keyCode == UP and block != 'up':
        ymov = -1
        direction = 'y'
    if keyCode == LEFT and block != 'left':
        xmov = -1
        direction = 'x'
    if keyCode == DOWN and block != 'down':
        ymov = 1
        direction = 'y'
    if keyCode == RIGHT and block != 'right':
        xmov = 1
        direction = 'x'

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

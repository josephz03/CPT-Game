xlist = []
ylist = []
delobject = False

def setup():
    size(800, 600)

def draw():
    global xlist, ylist, delobject
    background(255)
    while len(xlist) < 10:
        xlist.append(round(random(0, 600), 0))
        ylist.append(round(random(0, 400), 0))
    for i in range(len(xlist)):
        fill(0)
        ellipse(xlist[i], ylist[i], 20, 20)
        if ylist[i] > 600:
            if i == 9:
                delobject = True
                break
            else:
                ylist[i] += 0
        else:
            ylist[i] += 2
    if delobject:
        del xlist[:]
        del ylist[:]
        delobject = False

    

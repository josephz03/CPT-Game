keys_pressed = [False for key_code in range(256)]
x, y = 400, 550
pause = False
def setup():
    global pause
    size(800, 700)
    frameRate(60)
    noStroke()

def draw():
    global x, y
    background(255)
    
    if keys_pressed[87]:
        if x > 125 and x < 305 and y <= 225:
            y -= 0
        else:
            y -= 5
    if keys_pressed[83]:
        y += 5
    if keys_pressed[65]:
        if x <= 135 and y > 200 and y < 625:
            x -= 0
        elif x <= 305 and y > 75 and y < 225:
            x -= 0
        else:
            x -= 5
    if keys_pressed[68]:
        x += 5

    fill(0)
    rect(185, 190, 190, 20)
    rect(270, 140, 20, 80) #305 225 175
    rect(100, 400, 20, 400)
    rectMode(CENTER)
    fill(255, 0, 0)
    rect(constrain(x, 25, 775), constrain(y, 25, 675), 50, 50)
    
def keyPressed():
    global keys_pressed, pause
    keys_pressed[keyCode] = True
    
def keyReleased():
    global keys_pressed, pause
    keys_pressed[keyCode] = False

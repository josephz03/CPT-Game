x = 0
y = 0
car_move_x = 420
car_move_y = 430
xlist = []
ylist = []
collided = False
delobject = False
timer = 0
keys_pressed = [False for key_code in range(256)]

def setup():
    size(640,480)

def circles():
    global xlist, ylist, collided, delobject, timer, car_move_x, car_move_y
    ellipseMode(RADIUS)
    while len(xlist) < 4:
        xlist.append(round(random(300, 580), 0))
        ylist.append(round(random(-200, 0), 0))
        
    for i in range(len(xlist)):
        fill(0)
        ellipse(xlist[i], ylist[i], 10, 10)
        if ylist[i] > 560:
            if ylist[i] == min(ylist):
                delobject = True
                break
        else:
            if not collided:
                if car_move_y in range(int(ylist[i]-40), int(ylist[i]+41)) and car_move_x in range(int(xlist[i]-32), int(xlist[i]+32)):
                    collided = True
                else:
                    ylist[i] += 4
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
            
def road():
    fill(115,115,115)
    rect(280,0,50,height)
    fill(128,128,128)
    rect(330,0,50,height)
    fill(139,139,139)
    rect(380,0,80,height)
    fill(139,139,139)
    rect(380+50,0,80,height)
    fill(128,128,128)
    rect(380+100,0,50,height)
    fill(115,115,115)
    rect(380+150,0,50,height)
    

def shrubs():
    global x
    for i in range (-600, 750, 80):
        fill(34,139,34)
        ellipse(600,i+x,25,25)
        fill(0,128,0)
        ellipse(640,i+x,25,25)
        fill(50,205,50)
        ellipse(620,i+x,50,50)
    if x >= 600:
        x = -200
        
        
def yellow_lines():
    global x   
    fill(255, 174, 66)
    for i in range (-600, 750, 80):
        rect(420,i+x,20,60)
    if x >= 600:
        x = -200
    x += 10


def car():
    global car_move_x
    global car_move_y
    rectMode(CENTER)
    fill (200, 0, 0)
    rect(car_move_x,car_move_y,40,60)
    fill(0)
    rect(car_move_x, car_move_y,10,15)
    if car_move_x <= 100:
        car_move_x == 279
    
    
def keyPressed():
    global keys_pressed
    keys_pressed[keyCode] = True
    
    
def keyReleased():
    global keys_pressed
    keys_pressed[keyCode] = False

    
def draw():
    background(124, 252, 0)
    noStroke()
    global y, car_move_x, car_move_y, collided
    rectMode(CORNER)
    road()
    shrubs()
    yellow_lines()
    car()
    circles()
    collision_message()
    
    if keys_pressed[37]:
        if collided or car_move_x <= 280:
            car_move_x -= 0
        else:
            car_move_x -= 5
    if keys_pressed[38]:
        if collided or car_move_y <= 0:
            car_move_y -= 0
        else:
            car_move_y -= 5
    if keys_pressed[39]:
        if collided or car_move_x >= 538:
            car_move_x += 0
        else:
            car_move_x += 5
    if keys_pressed[40]:
        if collided or car_move_y >= 400:
            car_move_x += 0
        else:
            car_move_y += 5
            
    fill(101, 67, 33)
    rect(100,100,30,60)
    
    fill(0,100,0)
    triangle(87,111,117, 55, 143, 111)

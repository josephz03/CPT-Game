x = 0
y = 0
car_move_x = 420
car_move_y = 430
speed = 6
score = 0
timer = 0
xlist = []
ylist = []
collided = False
delobject = False
cooldown = 0
keys_pressed = [False for key_code in range(256)]

def setup():
    size(640,480)

def circles():
    global xlist, ylist, collided, delobject, cooldown, car_move_x, car_move_y, score, speed
    ellipseMode(RADIUS)
    while len(xlist) < 6:
        xlist.append(round(random(300, 580), 0))
        ylist.append(round(random(-300, 0), 0))    
    for i in range(len(xlist)):
        fill(0)
        ellipse(xlist[i], ylist[i], 10, 10)
        if ylist[i] > 520:
            if ylist[i] == min(ylist):
                delobject = True
                break
        else:
            if not collided:
                if car_move_y in range(int(ylist[i]-37), int(ylist[i]+38)) \
                    and car_move_x in range(int(xlist[i]-27), int(xlist[i]+28)):
                    collided = True
                else:
                    ylist[i] += speed
            else:
                ylist[i] += 0
            
    if delobject:
        if cooldown == 40:
            del xlist[:]
            del ylist[:]
            cooldown = 0
            score += 1
            delobject = False
        else:
            cooldown += 0.5
            
def display_score():
    global score
    textAlign(CENTER, CENTER)
    textSize(20)
    text("Score: {}".format(score),60, 20)
                            
def collision_message():
    global collided
    if collided:
        textSize(100)
        fill(255, 0, 0)
        text('You Lost', 320, 220)    
        
def road():
    global x, collided, speed
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
    #yellow lines, barrier movement
    for i in range (-600, 750, 80):
        fill(255, 174, 66)
        rect(420,i+x,20,60)
        fill(30,144,255)
        rect(590,i+x,100,100)
        fill(170,170,170)
        rect(582,i+x,6,90)
        fill(211,211,211)
        rect(580,i+x,10,50)
        fill(170,170,170)
        rect(272,i+x,6,90)
        fill(211,211,211)
        rect(270,i+x,10,50)
    if x >= 600:
        x = -200
    if not collided:
        x += speed
    else:
        x += 0


def car():
    global car_move_x, car_move_y
    rectMode(CENTER)
    fill (200, 0, 0)
    rect(car_move_x,car_move_y,40,60)
    fill (150, 0, 0)
    rect(car_move_x, car_move_y,40,30)
    rectMode(CORNER)
    fill(0)
    rect(car_move_x-20, car_move_y-30,5,15)
    rect(car_move_x+15, car_move_y-30,5,15)
    rect(car_move_x-20, car_move_y+15,5,15)
    rect(car_move_x+15, car_move_y+15,5,15)
    if car_move_x <= 100:
        car_move_x == 279
    
def display_timer():
    global timer
    if not collided and frameCount % 60 == 0:
        timer += 1
    fill(0)
    rect (408,4,50,20)
    fill(255)
    textSize(20)
    text("{}:{}{}".format(timer // 60, timer % 60 // 10, timer % 10), 433, 10)
    
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
    fill(101, 67, 33)
    rect(100,100,30,60)
    fill(0,100,0)
    triangle(87,111,117, 55, 143, 111)
    road()
    circles()
    car()
    display_score()
    display_timer()
    collision_message()
    
    if keys_pressed[37]:
        if collided or car_move_x <= 300:
            car_move_x -= 0
        else:
            car_move_x -= 5
    if keys_pressed[38]:
        if collided or car_move_y <= 30:
            car_move_y -= 0
        else:
            car_move_y -= 5
    if keys_pressed[39]:
        if collided or car_move_x >= 560:
            car_move_x += 0
        else:
            car_move_x += 5
    if keys_pressed[40]:
        if collided or car_move_y >= 450:
            car_move_x += 0
        else:
            car_move_y += 5

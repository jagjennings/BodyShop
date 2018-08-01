global bodyR, bodyG, bodyB
bodyR = 255
bodyG = 255
bodyB = 255

def makeBackground():
    size(1000, 800)
    global insideOfGarage, bodyR, bodyG, bodyB, tireR, tireG, tireB
    insideOfGarage = loadImage("insideOfGarage.jpg")
    # bodyR = 255
    # bodyG = 255
    # bodyB = 255
    tireR = 0
    tireG = 0
    tireB = 0

def drawCar():
    global insideOfGarage, bodyR, bodyG, bodyB, tireR, tireG, tireB
    image(insideOfGarage, 0, 0, 1000, 800)
    
    #color choices
    stroke(0)
    strokeWeight(1)
    fill(238,180,34)
    rect(120, 50, 75, 75, 30)
    fill(238,18,137)
    rect(220, 50, 75, 75, 30)
    fill(255, 0, 0)
    rect(320, 50, 75, 75, 30)
    fill(0, 0, 255)
    rect(420, 50, 75, 75, 30)
    fill(255, 255, 255)
    rect(520, 50, 75, 75, 30)
    fill(0, 0, 0)
    rect(620, 50, 75, 75, 30)
    fill(104,34,139)
    rect(720, 50, 75, 75, 30)
    fill(0,128,0)
    rect(820, 50, 75, 75, 30)
    
    
    # #tire color options
    # fill(60, 60, 60)
    # rect(25, 650, 75, 30, 30)
    
    #color light when hover
    if (mouseX >= 120 and mouseX <= 195) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 180, 34)
        rect(120, 50, 75, 75, 30)
    elif (mouseX >= 220 and mouseX <= 295) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 18, 137)
        rect(220, 50, 75, 75, 30)
    elif (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(255, 0, 0)
        rect(320, 50, 75, 75, 30)
    elif (mouseX >= 420 and mouseX <= 495) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 0, 255)
        rect(420, 50, 75, 75, 30)
    elif (mouseX >= 520 and mouseX <= 595) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 520, 0)
        strokeWeight(4)
        fill(255, 255, 255)
        rect(520, 50, 75, 75, 30)
    elif (mouseX >= 620 and mouseX <= 695) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 0, 0)
        rect(620, 50, 75, 75, 30)
    elif (mouseX >= 720 and mouseX <= 795) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(104, 34, 139)
        rect(720, 50, 75, 75, 30)
    elif (mouseX >= 820 and mouseX <= 895) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 128, 0)
        rect(820, 50, 75, 75, 30)
    
    #body of car
    noStroke()
    fill(bodyR, bodyG, bodyB)
    bezier(200, 450, 500, 300, 650, 250, 800, 450) #top of the body
    rect(110, 440, 780, 130, 10, 2000, 200, 20) #bottom of body
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    bezier(230, 440, 500, 310, 650, 260, 780, 440) #windows
    fill(0)
    rect(350, 378, 2, 192)
    rect(560, 318, 2, 252)
    rect(793, 440, 2, 130)
    noFill()
    stroke(60)
    strokeWeight(2)
    ellipse(385, 460, 30, 10) #door handles
    ellipse(595, 460, 30, 10)
    
    #lights
    fill(255,215,0)
    ellipse(860, 490, 20, 40)
    fill(255,64,64)
    ellipse(130, 490, 20, 40)
    
    #tires
    stroke(60)
    fill(0)
    ellipse(220, 570, 100, 100)
    ellipse(780, 570, 100, 100)
    ellipse(220, 570, 80, 80)
    ellipse(780, 570, 80, 80)
    
    fill(255,215,0)
    textSize(35)
    text("Pick a Body Color!", 300, 700)
    
    #next button
    fill(0, 255, 0)
    rect(880, 700, 100, 80, 30)
    fill(255)
    textSize(25)
    text("NEXT", 888, 750)
    if (mouseX >= 880 and mouseX <= 980) and (mouseY >= 700 and mouseY <= 780):
        fill(0, 255, 0)
        stroke(127,255,0)
        rect(880, 700, 100, 80, 30)
        fill(255)
        textSize(25)
        text("NEXT", 888, 750)
        
    #back button
    stroke(0)
    strokeWeight(1)
    fill(255, 0, 0)
    rect(20, 700, 100, 80, 30)
    fill(0)
    textSize(25)
    text("BACK", 28, 750)
    if (mouseX >= 20 and mouseX <= 120) and (mouseY >= 700 and mouseY <= 780):
        fill(255, 0, 0)
        stroke(255,0,0)
        rect(20, 700, 100, 80, 30)
        fill(0)
        textSize(25)
        text("BACK", 28, 750)
    
def drawTruck():
    pass
    global insideOfGarage, bodyR, bodyG, bodyB, tireR, tireG, tireB
    image(insideOfGarage, 0, 0, 1000, 800)
    
    #color choices
    stroke(0)
    strokeWeight(1)
    fill(238,180,34)
    rect(120, 50, 75, 75, 30)
    fill(238,18,137)
    rect(220, 50, 75, 75, 30)
    fill(255, 0, 0)
    rect(320, 50, 75, 75, 30)
    fill(0, 0, 255)
    rect(420, 50, 75, 75, 30)
    fill(255, 255, 255)
    rect(520, 50, 75, 75, 30)
    fill(0, 0, 0)
    rect(620, 50, 75, 75, 30)
    fill(104,34,139)
    rect(720, 50, 75, 75, 30)
    fill(0,128,0)
    rect(820, 50, 75, 75, 30)
    
    #color light when hover
    if (mouseX >= 120 and mouseX <= 195) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 180, 34)
        rect(120, 50, 75, 75, 30)
    elif (mouseX >= 220 and mouseX <= 295) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 18, 137)
        rect(220, 50, 75, 75, 30)
    elif (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(255, 0, 0)
        rect(320, 50, 75, 75, 30)
    elif (mouseX >= 420 and mouseX <= 495) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 0, 255)
        rect(420, 50, 75, 75, 30)
    elif (mouseX >= 520 and mouseX <= 595) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 520, 0)
        strokeWeight(4)
        fill(255, 255, 255)
        rect(520, 50, 75, 75, 30)
    elif (mouseX >= 620 and mouseX <= 695) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 0, 0)
        rect(620, 50, 75, 75, 30)
    elif (mouseX >= 720 and mouseX <= 795) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(104, 34, 139)
        rect(720, 50, 75, 75, 30)
    elif (mouseX >= 820 and mouseX <= 895) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 128, 0)
        rect(820, 50, 75, 75, 30)
    
    #body of truck
    noStroke()
    fill(bodyR, bodyG, bodyB)
    rect(110, 380, 780, 190, 10, 20, 20, 20) #bottom of body
    quad(360, 380, 390, 210, 660, 210, 720, 380)
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    quad(370, 380, 400, 230, 650, 230, 705, 380)
    fill(0)
    rect(490, 225, 2, 345)
    rect(490, 225, 165, 2)
    rect(708, 375, 2, 195)
    quad(655, 225, 657, 225, 710, 375, 708, 375)
    noFill()
    stroke(60)
    strokeWeight(2)
    ellipse(515, 410, 30, 10) #door handles
    
    #lights
    fill(255,215,0)
    ellipse(860, 430, 20, 40)
    fill(255,64,64)
    ellipse(130, 430, 20, 40)
    
    #tires
    stroke(60)
    fill(0)
    ellipse(220, 570, 100, 100)
    ellipse(780, 570, 100, 100)
    ellipse(220, 570, 80, 80)
    ellipse(780, 570, 80, 80)
    
    fill(255,215,0)
    textSize(35)
    text("Pick a Body Color!", 300, 700)
    
    #next button
    fill(0, 255, 0)
    rect(880, 700, 100, 80, 30)
    fill(255)
    textSize(25)
    text("NEXT", 888, 750)
    if (mouseX >= 880 and mouseX <= 980) and (mouseY >= 700 and mouseY <= 780):
        fill(0, 255, 0)
        stroke(127,255,0)
        rect(880, 700, 100, 80, 30)
        fill(255)
        textSize(25)
        text("NEXT", 888, 750)
        
    #back button
    stroke(0)
    strokeWeight(1)
    fill(255, 0, 0)
    rect(20, 700, 100, 80, 30)
    fill(0)
    textSize(25)
    text("BACK", 28, 750)
    if (mouseX >= 20 and mouseX <= 120) and (mouseY >= 700 and mouseY <= 780):
        fill(255, 0, 0)
        stroke(255,0,0)
        rect(20, 700, 100, 80, 30)
        fill(0)
        textSize(25)
        text("BACK", 28, 750)
    
def drawBus():
    global insideOfGarage, bodyR, bodyG, bodyB, tireR, tireG, tireB
    image(insideOfGarage, 0, 0, 1000, 800)
    
    #color choices
    stroke(0)
    strokeWeight(1)
    fill(238,180,34)
    rect(120, 50, 75, 75, 30)
    fill(238,18,137)
    rect(220, 50, 75, 75, 30)
    fill(255, 0, 0)
    rect(320, 50, 75, 75, 30)
    fill(0, 0, 255)
    rect(420, 50, 75, 75, 30)
    fill(255, 255, 255)
    rect(520, 50, 75, 75, 30)
    fill(0, 0, 0)
    rect(620, 50, 75, 75, 30)
    fill(104,34,139)
    rect(720, 50, 75, 75, 30)
    fill(0,128,0)
    rect(820, 50, 75, 75, 30)
    
    #color light when hover
    if (mouseX >= 120 and mouseX <= 195) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 180, 34)
        rect(120, 50, 75, 75, 30)
    elif (mouseX >= 220 and mouseX <= 295) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 18, 137)
        rect(220, 50, 75, 75, 30)
    elif (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(255, 0, 0)
        rect(320, 50, 75, 75, 30)
    elif (mouseX >= 420 and mouseX <= 495) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 0, 255)
        rect(420, 50, 75, 75, 30)
    elif (mouseX >= 520 and mouseX <= 595) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 520, 0)
        strokeWeight(4)
        fill(255, 255, 255)
        rect(520, 50, 75, 75, 30)
    elif (mouseX >= 620 and mouseX <= 695) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 0, 0)
        rect(620, 50, 75, 75, 30)
    elif (mouseX >= 720 and mouseX <= 795) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(104, 34, 139)
        rect(720, 50, 75, 75, 30)
    elif (mouseX >= 820 and mouseX <= 895) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 128, 0)
        rect(820, 50, 75, 75, 30)
    
    #body of bus
    noStroke()
    fill(bodyR, bodyG, bodyB)
    rect(110, 220, 680, 350, 30, 30, 0, 10) #top of body
    rect(790, 380, 100, 190, 0, 50, 10, 0) #hood
    fill(60)
    textSize(25)
    text("MAGIC SCHOOL BUS", 300, 465)
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    rect(125, 235, 120, 150, 30)
    rect(260, 235, 120, 150, 30)
    rect(395, 235, 120, 150, 30)
    rect(530, 235, 120, 150, 30)
    rect(665, 235, 110, 150, 30)
    rect(140, 400, 600, 10)
    rect(140, 490, 600, 10)
    
    #lights
    strokeWeight(2)
    fill(255,215,0)
    ellipse(860, 440, 20, 40)
    fill(255,64,64)
    ellipse(130, 440, 20, 40)
    
    #tires
    stroke(60)
    fill(0)
    ellipse(220, 570, 120, 120)
    ellipse(780, 570, 120, 120)
    ellipse(220, 570, 100, 100)
    ellipse(780, 570, 100, 100)
    
    fill(255,215,0)
    textSize(35)
    text("Pick a Body Color!", 300, 700)
    
    #next button
    fill(0, 255, 0)
    rect(880, 700, 100, 80, 30)
    fill(255)
    textSize(25)
    text("NEXT", 888, 750)
    if (mouseX >= 880 and mouseX <= 980) and (mouseY >= 700 and mouseY <= 780):
        fill(0, 255, 0)
        stroke(127,255,0)
        rect(880, 700, 100, 80, 30)
        fill(255)
        textSize(25)
        text("NEXT", 888, 750)
    
    #back button
    stroke(0)
    strokeWeight(1)
    fill(255, 0, 0)
    rect(20, 700, 100, 80, 30)
    fill(0)
    textSize(25)
    text("BACK", 28, 750)
    if (mouseX >= 20 and mouseX <= 120) and (mouseY >= 700 and mouseY <= 780):
        fill(255, 0, 0)
        stroke(255,0,0)
        rect(20, 700, 100, 80, 30)
        fill(0)
        textSize(25)
        text("BACK", 28, 750)
    
def pickColor():
    global bodyR, bodyG, bodyB, tireR, tireG, tireB
    if (mouseX >= 120 and mouseX <= 195) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 238
        bodyG = 180
        bodyB = 34
    if (mouseX >= 220 and mouseX <= 295) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 238
        bodyG = 18
        bodyB = 137
    if (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 255
        bodyG = 0
        bodyB = 0
    if (mouseX >= 420 and mouseX <= 495) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 0
        bodyG = 0
        bodyB = 255
    if (mouseX >= 520 and mouseX <= 595) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 255
        bodyG = 255
        bodyB = 255
    if (mouseX >= 620 and mouseX <= 695) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 0
        bodyG = 0
        bodyB = 0
    if (mouseX >= 720 and mouseX <= 795) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 104
        bodyG = 34
        bodyB = 139
    if (mouseX >= 820 and mouseX <= 895) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 0
        bodyG = 128
        bodyB = 0
        
def setupDrive():
    size(1000, 800)
    global freeway, carX, carY, truckX, truckY, busX, busY
    carX = 0
    carY = 440
    truckX = 110
    truckY = 380
    busX = 110
    busY = 220
    
    freeway = loadImage("freeway.png")
    
def driveCar():
    global freeway, carX, carY, bodyR, bodyG, bodyB
    image(freeway, 0, 0, 1150, 874)
    #body of car
    noStroke()
    fill(bodyR, bodyG, bodyB)
    bezier(carX+90, carY+10, carX+390, carY-140, carX+540, carY-190, carX+690, carY+10) #top of the body
    rect(carX, carY, 780, 130, 10, 2000, 200, 20) #bottom of body
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    bezier(carX+120, carY, carX+390, carY-130, carX+540, carY-180, carX+670, carY) #windows
    fill(0)
    rect(carX+240, carY-62, 2, 192)
    rect(carX+450, carY-122, 2, 252)
    rect(carX+683, carY, 2, 130)
    noFill()
    stroke(60)
    strokeWeight(2)
    ellipse(carX+275, carY+20, 30, 10) #door handles
    ellipse(carX+485, carY+20, 30, 10)
    
    #lights
    fill(255,215,0)
    ellipse(carX+750, carY+50, 20, 40)
    fill(255,64,64)
    ellipse(carX+20, carY+50, 20, 40)
    
    #tires
    stroke(60)
    fill(0)
    ellipse(carX+110, carY+130, 100, 100)
    ellipse(carX+670, carY+130, 100, 100)
    ellipse(carX+110, carY+130, 80, 80)
    ellipse(carX+670, carY+130, 80, 80)
    
    carX += 12
    
    if carX >= 980:
        textSize(80)
        fill(bodyR, bodyG, bodyB)
        text("THE END", 270, 370)
    
def driveTruck():
    global freeway, truckX, truckY, bodyR, bodyG, bodyB
    image(freeway, 0, 0, 1150, 874)
    #body of truck
    noStroke()
    fill(bodyR, bodyG, bodyB)
    rect(truckX, truckY, 780, 190, 10, 20, 20, 20) #bottom of body
    quad(truckX+250, truckY, truckX+280, truckY-170, truckX+550, truckY-170, truckX+610, truckY)
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    quad(truckX+260, truckY, truckX+290, truckY-150, truckX+540, truckY-150, truckX+595, truckY)
    fill(0)
    rect(truckX+380, truckY-155, 2, 345)
    rect(truckX+380, truckY-155, 165, 2)
    rect(truckX+598, truckY-5, 2, 195)
    quad(truckX+545, truckY-155, truckX+547, truckY-155, truckX+600, truckY-5, truckX+598, truckY-5)
    noFill()
    stroke(60)
    strokeWeight(2)
    ellipse(truckX+405, truckY+30, 30, 10) #door handles
    
    #lights
    fill(255,215,0)
    ellipse(truckX+750, truckY+50, 20, 40)
    fill(255,64,64)
    ellipse(truckX+20, truckY+50, 20, 40)
    
    #tires
    stroke(60)
    fill(0)
    ellipse(truckX+110, truckY+190, 100, 100)
    ellipse(truckX+670, truckY+190, 100, 100)
    ellipse(truckX+110, truckY+190, 80, 80)
    ellipse(truckX+670, truckY+190, 80, 80)
    
    truckX += 12
    
    if truckX >= 980:
        textSize(80)
        fill(bodyR, bodyG, bodyB)
        text("THE END", 270, 370)

def driveBus():
    global freeway, busX, busY, bodyR, bodyG, bodyB
    image(freeway, 0, 0, 1150, 874)
    #body of bus
    noStroke()
    fill(bodyR, bodyG, bodyB)
    rect(busX, busY, 680, 350, 30, 30, 0, 10) #top of body
    rect(busX++680, 380, 100, 190, 0, 50, 10, 0) #hood
    fill(60)
    text("MAGIC SCHOOL BUS", busX+190, busY+245)
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    rect(busX+15, busY+15, 120, 150, 30)
    rect(busX+150, busY+15, 120, 150, 30)
    rect(busX+285, busY+15, 120, 150, 30)
    rect(busX+420, busY+15, 120, 150, 30)
    rect(busX+555, busY+15, 110, 150, 30)
    rect(busX+30, busY+180, 600, 10)
    rect(busX+30, busY+270, 600, 10)
    
    #lights
    strokeWeight(2)
    fill(255,215,0)
    ellipse(busX+750, busY+220, 20, 40)
    fill(255,64,64)
    ellipse(busX+20, busY+220, 20, 40)
    
    #tires
    stroke(60)
    fill(0)
    ellipse(busX+110, busY+350, 120, 120)
    ellipse(busX+670, busY+350, 120, 120)
    ellipse(busX+110, busY+350, 100, 100)
    ellipse(busX+670, busY+350, 100, 100)
    
    busX += 12
    
    if busX >= 980:
        textSize(80)
        fill(bodyR, bodyG, bodyB)
        text("THE END", 270, 370)

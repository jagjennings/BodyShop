def startAvatarPage():
    size(1000,800)
    background(147, 103, 89)

    textSize(20)
    text("LEFT MOUSE = FACE", 200, 700)
    text("CENTER MOUSE = EYES ", 200, 725)
    text("RIGHT MOUSE = CLOTHES", 200, 750)





    #1
    fill(255,255,255)
    rect(0,0,50,50)
    #2
    fill(0,0,0)
    rect(0,50,50,50)
    #3
    fill(255, 0, 0)
    rect(0,100,50,50)
    #4
    fill(0, 255, 0)
    rect(0,150,50,50)
    #5
    fill(0, 0, 255)
    rect(0,200,50,50)
    #6
    fill(255, 255, 0)
    rect(0,250,50,50)
    #7
    fill(0, 255, 255)
    rect(0,300,50,50)



def drawBody():
    if mouseButton == LEFT:
        if mouseX <= 50 and mouseY < 50:
            fill(255, 255, 255)
        if mouseX <= 50 and mouseY > 50 and mouseY <=100:
            fill(0, 0, 0)
        if mouseX <= 50 and mouseY > 100 and mouseY <=150:
            fill(255, 0, 0)
        if mouseX <=50 and mouseY > 150 and mouseY <=200:
            fill(0, 255, 0)
        if mouseX <=50 and mouseY > 200 and mouseY <=250:
            fill(0, 0, 255)
        if mouseX <=50 and mouseY > 250 and mouseY <=300:
            fill(255, 255, 0)
        if mouseX <=50 and mouseY > 300 and mouseY <=350:
            fill(0, 255, 255)

def mouseFunction():
    if mouseX <= 50 and mouseY < 50:
        fill(255, 255, 255)
    if mouseX <= 50 and mouseY > 50 and mouseY <=100:
        fill(0, 0, 0)
    if mouseX <= 50 and mouseY > 100 and mouseY <=150:
        fill(255, 0, 0)
    if mouseX <=50 and mouseY > 150 and mouseY <=200:
        fill(0, 255, 0)
    if mouseX <=50 and mouseY > 200 and mouseY <=250:
        fill(0, 0, 255)
    if mouseX <=50 and mouseY > 250 and mouseY <=300:
        fill(255, 255, 0)
    if mouseX <=50 and mouseY > 300 and mouseY <=350:
        fill(0, 255, 255)
    if mouseButton == LEFT:
        rect(240, 100, 200, 240)                       # make face
        quad(200, 60, 400, 60, 440, 100, 240, 100)     # top of 3D head
        quad(200, 60, 240, 100, 240, 340, 200, 300)    # left side of 3D head
        bezier(340, 220, 355, 220, 387, 195, 390, 217) # make top of nose
        bezier(340, 233, 355, 235, 389, 235, 390, 217) # make bottom of nose
        bezier(290, 225, 310, 350, 369, 330, 375, 240) # make bottom of mouth
        bezier(290, 224, 310, 240, 350, 255, 390, 241) # make top of mouth
        line(390, 241, 378, 232)                       # connect mouth to nose
        bezier(282, 225, 265, 203, 300, 190, 298, 220)
    if mouseButton == CENTER:
        ellipse(370, 170, 75, 95)                      # make right eye
        ellipse(310, 170, 75, 95)                      # make left eye
    if mouseButton == RIGHT:
        rect(240, 340, 200, 30)                        # make front of shirt
        quad(200, 300, 240, 340, 240, 370, 200, 330)   # make left side of shirt
        triangle(290, 340, 330, 340, 315, 360)         # make left collar
        triangle(345, 340, 385, 340, 365, 358)         # make right collar

        rect(240, 370, 200, 40)                        # make front of shirt
        quad(200, 330, 240, 370, 240, 410, 200, 370)   # make left side of shirt
        beltWidth = 30
        beltHeight = 10

        rect(258, 385, beltWidth, beltHeight)
        rect(303, 385, beltWidth, beltHeight)
        rect(348, 385, beltWidth, beltHeight)
        rect(393, 385, beltWidth, beltHeight)
        quad(200, 343, 210, 353, 210, 363, 200, 353)
        quad(230, 373, 240, 383, 240, 393, 230, 383)

def spongebob():
    size(1000, 800)




    noStroke()
    fill(0, 255, 255)                              # make irises light blue
    ellipse(365, 170, 25, 33)                      # make right iris
    ellipse(310, 170, 25, 33)                      # make left iris
    fill(0, 0, 0)                                  # make pupils black
    ellipse(365, 170, 10, 13)                      # make right pupil
    ellipse(310, 170, 10, 13)                      # make left pupil
    fill(255, 255, 255)                            # fill eye sparkle
    noStroke()
    ellipse(370, 165, 7, 7)                        # make right eye sparkle
    ellipse(315, 165, 7, 7)                        # make left eye sparkle

    stroke(0)
    fill(227,207,87)


    fill(139, 35, 35)                              # fill mouth inside red
    bezier(290, 225, 310, 350, 369, 330, 375, 240) # make bottom of mouth
    fill(255, 255, 255)                            # fill teeth white
    rect(315, 237, 25, 30)                         # make left tooth
    rect(350, 240, 25, 27)                         # make left tooth


    stroke(238, 106, 80)
    
    #next button
    stroke(0)
    fill(0, 255, 0)
    rect(880, 20, 100, 80, 30)
    fill(255)
    textSize(25)
    text("NEXT", 888, 70)
    if (mouseX >= 880 and mouseX <= 980) and (mouseY >= 20 and mouseY <= 100):
        fill(0, 255, 0)
        stroke(127,255,0)
        rect(880, 20, 100, 80, 30)
        fill(255)
        textSize(25)
        text("NEXT", 888, 70)
        
    #back button
    stroke(0)
    strokeWeight(1)
    fill(255, 0, 0)
    rect(20, 600, 100, 80, 30)
    fill(0)
    textSize(25)
    text("BACK", 28, 650)
    if (mouseX >= 20 and mouseX <= 120) and (mouseY >= 600 and mouseY <= 680):
        fill(255, 0, 0)
        stroke(255,0,0)
        rect(20, 600, 100, 80, 30)
        fill(0)
        textSize(25)
        text("BACK", 28, 650)

from functionsList import *
from bodyshop_background import *
from bodyshopscreen2 import *
from spongebob import *
from radio import *
#from skrt import *

def setup():
    size(1000, 800)
    global screen
    global minim
    minim = Minim(this)
    global player, player1, player2, player3
    player = minim.loadFile("No Hands Clean.mp3")
    player1 = minim.loadFile("I Bet You Wont.mp3")
    player2 = minim.loadFile("In My Feelings.mp3")
    player3 = minim.loadFile("21 Questions.mp3")
    
    
    screen = "one"
    vehicle = "car"
    
    if screen == "one":
        backgroundImage()
    

def draw():
    global screen, vehicle, player, player1, player2, player3, musicPlaying, bodyR, bodyG, bodyB
    
    if screen == "one":
        backgroundTextAndBoxes()
    elif screen == "two" and vehicle == "car":
        drawCar()
    elif screen == "two" and vehicle == "truck":
        drawTruck()
    elif screen == "two" and vehicle == "bus":
        drawBus()
    elif screen == "three":
        #drawBody()
        spongebob()
    elif screen == "four":
        musicStation(player, player1, player2, player3)
    elif screen == "five" and vehicle == "car":
        driveCar()
    elif screen == "five" and vehicle == "truck":
        driveTruck()
    elif screen == "five" and vehicle == "bus":
        driveBus()
        
        
def mouseClicked():
    global vehicle, screen, bodyR, bodyG, bodyB
    if screen == "two":
        pickColor()
    if screen == "three":
        mouseFunction()
    if screen == "four":
        musicPlayed()
    
    if screen == "two" and (mouseX >= 20 and mouseX <= 120) and (mouseY >= 700 and mouseY <= 780):
        screen = "one"
        backgroundImage()
    if screen == "three" and (mouseX >= 20 and mouseX <= 120) and (mouseY >= 600 and mouseY <= 680):
        screen = "two"
        makeBackground()
    if screen == "one" and (mouseX >= 50 and mouseX <= 200) and (mouseY >= 325 and mouseY <= 475):
        screen = "two"
        vehicle = "car"
        makeBackground()
    if screen == "one" and (mouseX >= 425 and mouseX <= 600) and (mouseY >= 325 and mouseY <= 475):
        screen = "two"
        vehicle = "truck"
        makeBackground()
    if screen == "one" and (mouseX >= 800 and mouseX <= 950) and (mouseY >= 325 and mouseY <= 475):
        screen = "two"
        vehicle = "bus"
        makeBackground()
    if screen == "two" and (mouseX >= 880 and mouseX <= 980) and (mouseY >= 700 and mouseY <= 780):
        screen = "three"
        startAvatarPage()
    if screen == "three" and (mouseX >= 880 and mouseX <= 980) and (mouseY >= 20 and mouseY <= 100):
        screen = "four"
        radioBackground()
    if screen == "four" and (mouseX >= 630 and mouseX <= 730) and (mouseY >= 700 and mouseY <= 780):
        screen = "five"
        setupDrive()

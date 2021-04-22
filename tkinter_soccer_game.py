from tkinter import *
from playerHome import playerHome
from playerVisiting import playerVisiting
from soccerBall import soccerBall
import math
import random
####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.mode = "startScreen"
    data.playerHomeIndex = 2
    data.playerVisitingIndex = 0
    data.picture = PhotoImage(file = "newSoccer pitch.png")
    data.Bayern = PhotoImage(file = "Bayern.png")
    data.Bayern = data.Bayern.subsample(2,2)
    data.realMadrid = PhotoImage(file = "realMadrid.png")
    data.realMadrid = data.realMadrid.subsample(3,3)
    data.Barcelona = PhotoImage(file = "Barcelona.png")
    data.Barcelona = data.Barcelona.subsample(5,5)
    data.Juventus = PhotoImage(file = "Juventus.png")
    data.Juventus = data.Juventus.subsample(4,4)
    data.picture = data.picture.subsample(2,2)
    data.leftPostX = 187.5
    data.rightPostX = 312.5
    data.intLeftPostX = int(data.leftPostX)
    data.intRightPostX = int(data.rightPostX)
    data.theFixedPoint = random.randint(data.intLeftPostX + 10,data.intRightPostX - 10)
    data.leftBoarder = 80
    data.rightBoarder = 420
    data.lowerBoarder = 30
    data.upperBoarder = 470
    data.soccerBall = soccerBall(data.width/2,data.height/2) 
    data.soccerMovingState = False
    #data.collided means when the soccer ball collides with the visiting player
    data.collided = False
    data.inStrategy = False
    data.inShootingProcess = False
    data.bouncedWall = False
    data.direction = 0
    data.bouncedDirection = 0
    data.collidedSpeed = 0
    data.ballSpeed = 1.5
    data.blueTeamScore = 0
    data.redTeamScore = 0
    data.playerVisitingSpeed = 0.2
    data.playerVisitingSupportingSpeed = 0.2
    data.startingPostionHome = [[200,300],[300,300],[250,450]]
    data.team1 = [playerHome(data.startingPostionHome[0][0],data.startingPostionHome[0][1]),playerHome(data.startingPostionHome[1][0],data.startingPostionHome[1][1]),playerHome(data.startingPostionHome[2][0],data.startingPostionHome[2][1])]

def mousePressed(event, data):
    if(data.mode == "levelSelection"):
        if(event.x > 200 and event.x < 400 and event.y > 300 and event.y < 350):
            data.playerVisitingSpeed = 0.05
            data.playerVisitingSupportingSpeed = 0.05
            data.mode = "gameState"
            data.team2 = [playerVisiting(200,200,data.playerVisitingSpeed,data.playerVisitingSupportingSpeed,data.theFixedPoint),playerVisiting(300,200,data.playerVisitingSpeed,data.playerVisitingSupportingSpeed,data.theFixedPoint),playerVisiting(250,50,data.playerVisitingSupportingSpeed,data.playerVisitingSupportingSpeed,data.theFixedPoint)]
        
        if(event.x > 200 and event.x < 400 and event.y > 375 and event.x < 425):
            data.playerVisitingSpeed = 0.1
            data.playerVisitingSupportingSpeed = 0.1
            data.mode = "gameState"
            data.team2 = [playerVisiting(200,200,data.playerVisitingSpeed,data.playerVisitingSupportingSpeed,data.theFixedPoint),playerVisiting(300,200,data.playerVisitingSpeed,data.playerVisitingSupportingSpeed,data.theFixedPoint),playerVisiting(250,50,data.playerVisitingSupportingSpeed,data.playerVisitingSupportingSpeed,data.theFixedPoint)]
        
        if(event.x > 200 and event.x < 400 and event.y > 450 and event.x < 500):
            data.playerVisitingSpeed = 0.5
            data.playerVisitingSupportingSpeed = 0.5
            data.mode = "gameState"
            data.team2 = [playerVisiting(200,200,data.playerVisitingSpeed,data.playerVisitingSupportingSpeed,data.theFixedPoint),playerVisiting(300,200,data.playerVisitingSpeed,data.playerVisitingSupportingSpeed,data.theFixedPoint),playerVisiting(250,50,data.playerVisitingSupportingSpeed,data.playerVisitingSupportingSpeed,data.theFixedPoint)]
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if(event.keysym == "Up"):
        data.team1[data.playerHomeIndex].move("up")
        data.team1[data.playerHomeIndex].speed = 10
    if(event.keysym == "Down"):
        data.team1[data.playerHomeIndex].move("down")
        data.team1[data.playerHomeIndex].speed = 10
    if(event.keysym == "Left"):
        data.team1[data.playerHomeIndex].move("left")
        data.team1[data.playerHomeIndex].speed = 10
    if(event.keysym == "Right"):
        data.team1[data.playerHomeIndex].move("right")
        data.team1[data.playerHomeIndex].speed = 10
    if(event.keysym == "s"):
        data.mode = "levelSelection"
    if(event.keysym == "p"):
        data.mode = "startScreen"
    pass
    
def smartAngleFunction(selfX,selfY,otherX, otherY):
    if(abs(otherX - selfX) < 0.5 and (otherY - selfY) < 0):
        return 90
    if(abs(otherX - selfX) < 0.5 and (otherY - selfY) > 0):
        return 270
    if((otherX - selfX) > 0 and abs(otherY - selfY) < 0.5):
        return 0
    if((otherX - selfX) < 0 and abs(otherY - selfY) < 0.5):
        return 180
    theta = math.atan(abs(otherY - selfY) / abs(otherX - selfX))
    theta = math.degrees(theta)
    if((otherX - selfX) > 0 and (otherY - selfY) < 0):
        return theta
    elif((otherX - selfX) < 0  and (otherY - selfY) < 0):
        return 180 - theta
    elif((otherX - selfX) < 0 and (otherY - selfY) > 0):
        return 180 + theta
    elif((otherX - selfX) > 0 and (otherY - selfY) > 0):
        return 0 - theta
        
def visitingTeamRespond(data):
    pass
    
    #Switching players based on who is the closest
    newList = []
    i = 0
    while(i < len(data.team2)):
        newList = newList + [((data.team2[i].x - data.soccerBall.x)**(2) + 
        (data.team2[i].y - data.soccerBall.y) ** (2))**(0.5)]
        i = i + 1
    data.playerVisitingIndex = newList.index(min(newList))
    
    #Check if the visiting player collides with the home player, if the visiting player collides with the home player, make the visiting player retreat back in the same direction from where it comes from by a speed, the time duration only lasts for 1ms, after a millisecond, the ball speed gets set to 0. 
    
    
    for i in data.team1:
        for j in data.team2:
            if(j.collideWithOtherTeamCheck(i)[0] == True):
                j.bounce(i)
    
    #Check if the visiting player collides with the visiting player, if the visiting player collides with the visiting player, make the visiting player bounce back
    if(data.team2[0].collideWithSameTeamCheck(data.team2[1])[0] == True):
        data.team2[0].bounce(1)
    if(data.team2[1].collideWithSameTeamCheck(data.team2[2])[0] == True):
        data.team2[1].bounce(2)
    if(data.team2[2].collideWithSameTeamCheck(data.team2[0])[0] == True):
        data.team2[2].bounce(0)
    
    
    #Make the visiting team player gravitates toward shooting position
    newDirection = data.team2[data.playerVisitingIndex].ballChasingDirection(data.soccerBall)
    if(data.inShootingProcess == False):
        data.team2[data.playerVisitingIndex].move(newDirection,data.team2[data.playerVisitingIndex].speed)
    if(data.team2[data.playerVisitingIndex].checkInFirePosition(data.soccerBall)):
        data.inShootingProcess = True
        
    #If the ball moves to the designated position, make a hit 
    if(data.inShootingProcess == True):
        toTheBallDirection = data.team2[data.playerVisitingIndex].ballShootingDirectionWhenReady(data.soccerBall)
        # print("toTheBallDirection",toTheBallDirection)
        # print("data.team2[data.playerVisitingIndex]",data.team2[data.playerVisitingIndex])
        # print("data.team2[data.playerVisitingIndex].speed",data.team2[data.playerVisitingIndex].speed)
        
        data.team2[data.playerVisitingIndex].move(toTheBallDirection,data.team2[data.playerVisitingIndex].speed)
        if(abs(data.ballSpeed-0)<0.04):
            data.inShootingProcess = False
            data.ballSpeed = 0
    #If one of the team2 player collides with the ball, make the ball move accordingly to the direction it collides
    if(data.team2[data.playerVisitingIndex].collideWithSoccerBallCheck(data.soccerBall)[0]):
        data.soccerMovingState = True
        data.direction = data.team2[data.playerVisitingIndex].collideWithSoccerBallCheck(data.soccerBall)[1]
        
#Check if the soccer ball has scored
def checkScored(data):
    if(data.soccerBall.y < data.lowerBoarder and data.soccerBall.x > data.leftPostX and data.soccerBall.x < data.rightPostX):
        data.blueTeamScore = data.blueTeamScore + 1
        data.soccerBall.y = data.width/2
        data.soccerBall.x = data.height/2
        data.ballSpeed= 1.5
        reset(data)
    if(data.soccerBall.y > data.upperBoarder and data.soccerBall.x > data.leftPostX and data.soccerBall.x < data.rightPostX):
        data.redTeamScore = data.redTeamScore + 1
        data.soccerBall.y = data.width/2
        data.soccerBall.x = data.height/2
        data.ballSpeed= 1.5
        reset(data)

#Reset Everything to the starting position
def reset(data):
    for i in data.team1:
        i.reset()
    for i in data.team2:
        i.reset()

def strategicMoveHome(data):
    if(data.playerHomeIndex == 0):
        
        if(data.team1[0].y < (data.height / 2) and 
           data.team1[0].y >= (data.height / 4) and 
           data.team1[0].x < (data.width) / 2):
            data.inStrategy = True
            data.team1[1].makingMoveUpperFieldRightSide(data.team1[0])
            if(data.team1[1].makingMoveUpperFieldRightSide(data.team1[0]) == True):
                data.inStrategy = False
            else:
                data.inStrategy = True
                
        if(data.team1[0].y < (data.height / 2) and 
        data.team1[0].y >= (data.height / 4) and 
        data.team1[0].x > (data.width) / 2):
            data.inStrategy = True
            data.team1[1].makingMoveUpperFieldLeftSide(data.team1[0])
            if(data.team1[1].makingMoveUpperFieldLeftSide(data.team1[0] == False)):
                data.inStrategy = False
            else:
                data.inStrategy = True
            
        if(data.team1[0].y > (data.height / 2) and 
           data.team1[0].y <= (data.height / 4 * 3) and 
           data.team1[0].x < (data.width) / 2):
            data.inStrategy = True
            data.team1[1].makingMoveLowerFieldRightSide(data.team1[0])
            if(data.team1[1].makingMoveLowerFieldRightSide(data.team1[0]) == True):
                data.inStrategy = False
            else:
                data.inStrategy = True
                
        if(data.team1[0].y > (data.height / 2) and 
           data.team1[0].y <= (data.height / 4 * 3) and 
           data.team1[0].x > (data.width) / 2):
            data.inStrategy = True
            data.team1[1].makingMoveLowerFieldLeftSide(data.team1[0])
            if(data.team1[1].makingMoveLowerFieldLeftSide(data.team1[0]) == True):
                data.inStrategy = False
            else:
                data.inStrategy = True
        
    if(data.playerHomeIndex == 1):
        
        if(data.team1[1].y < (data.height / 2) and 
           data.team1[1].y >= (data.height / 4) and 
           data.team1[1].x < (data.width) / 2):
            data.inStrategy = True
            data.team1[0].makingMoveUpperFieldRightSide(data.team1[1])
            if(data.team1[0].makingMoveUpperFieldRightSide(data.team1[1]) == True):
                data.inStrategy = False
            else:
                data.inStrategy = True
                
        if(data.team1[1].y < (data.height / 2) and 
        data.team1[1].y >= (data.height / 4) and 
        data.team1[1].x > (data.width) / 2):
            data.inStrategy = True
            data.team1[0].makingMoveUpperFieldLeftSide(data.team1[1])
            if(data.team1[0].makingMoveUpperFieldLeftSide(data.team1[1] == False)):
                data.inStrategy = False
            else:
                data.inStrategy = True
            
        if(data.team1[1].y > (data.height / 2) and 
           data.team1[1].y <= (data.height / 4 * 3) and 
           data.team1[1].x < (data.width) / 2):
            data.inStrategy = True
            data.team1[0].makingMoveLowerFieldRightSide(data.team1[1])
            if(data.team1[0].makingMoveLowerFieldRightSide(data.team1[1]) == True):
                data.inStrategy = False
            else:
                data.inStrategy = True
                
        if(data.team1[1].y > (data.height / 2) and 
           data.team1[1].y <= (data.height / 4 * 3) and 
           data.team1[1].x > (data.width) / 2):
            data.inStrategy = True
            data.team1[0].makingMoveLowerFieldLeftSide(data.team1[1])
            if(data.team1[0].makingMoveLowerFieldLeftSide(data.team1[1]) == True):
                data.inStrategy = False
            else:
                data.inStrategy = True
                
def strategicMoveVisiting(data):
    if(data.playerVisitingIndex == 0):
        if(data.team2[0].y > (data.height / 2) and
            data.team2[0].y <= (data.height / 4 * 3) and
            data.team2[0].x < (data.width / 2)):
                data.team2[1].makingMoveUpperFieldRightSide(data.team2[0])
        
        if(data.team2[0].y > (data.height / 2) and 
        data.team2[0].y <= (data.height / 4 * 3) and 
        data.team2[0].x > (data.width / 2)):
            data.team2[1].makingMoveUpperFieldLeftSide(data.team2[0])
        
        if(data.team2[0].y < (data.height / 2) and 
        data.team2[0].y >= (data.height / 4) and
        data.team2[0].x < (data.width / 2)):
            data.team2[1].makingMoveLowerFieldRightSide(data.team2[0])
    
    
                       
def timerFired(data):
    if(data.mode == "gameState"):
        if(data.blueTeamScore > 3):
            data.mode = "blueTeamWinState"
        if(data.redTeamScore > 3):
            data.mode = "redTeamWinState"
        # Check if the soccer has scored
        checkScored(data)
        
        #Make one of the visiting team player to chase the ball
        visitingTeamRespond(data)
        
        #Make the home team move strategically 
        strategicMoveHome(data) 
        
        #Make the oppposing team move strategically 
        strategicMoveVisiting(data)
    
        #Normal moving state
        if(data.soccerMovingState == True):
            if(data.collided == False and data.bouncedWall == False):
                data.ballSpeed = data.ballSpeed - 0.01
                if(abs(data.ballSpeed-0)<0.02):
                    data.soccerMovingState = False
                    data.ballSpeed = 1.5
                data.soccerBall.reactToKick(data.direction,data.ballSpeed)
        
        #Check if the ball collides with the wall or not
        if(data.soccerBall.bouncingBoarder(data.direction,data.leftBoarder,data.rightBoarder,data.lowerBoarder,data.upperBoarder,data.bouncedDirection)[0] == True):
            data.bouncedWall = True
        if(data.bouncedWall == True) and (data.soccerMovingState == True):
            data.bouncedDirection = data.soccerBall.bouncingBoarder(data.direction,data.leftBoarder,data.rightBoarder,data.lowerBoarder,data.upperBoarder,data.bouncedDirection)[1]
            data.ballSpeed = data.ballSpeed - 0.01
            if(abs(data.ballSpeed - 0) < 0.02):
                data.soccerMovingState = False
                data.ballSpeed = 0
                data.bouncedWall = False
            data.soccerBall.reactToKick(data.bouncedDirection,data.ballSpeed)
            
        #Check if the ball collide with Visiting player
        # for i in data.team2:
        #     if(i == data.playerHomeIndex):
        #         continue
        #     else:
        #         if(data.soccerBall.collideWithVisitingTeamCheck(i) and data.soccerMovingState == True):
        #             data.collided = True
        #             data.collidedSpeed = -data.ballSpeed
        
        #Switching Control of the ball for home player
        # for i in range(len(data.team1)):
        #     if(i == data.playerHomeIndex):
        #         continue
        #     else:
        #         if(data.soccerBall.collideWithHomeTeamCheck(data.team1[i]) and data.soccerMovingState == True):
        #             data.collided = True
        #             data.collidedSpeed = -data.ballSpeed
                    # data.playerHomeIndex = i
                    
        #Switching Control of the ball for home player
        # if(data.inStrategy == False):
        newList = []
        i = 0
        while(i < len(data.team1)):
            newList = newList + [((data.team1[i].x - data.soccerBall.x)**(2) + 
            (data.team1[i].y - data.soccerBall.y) ** (2))**(0.5)]
            i = i + 1
        data.playerHomeIndex = newList.index(min(newList))
        
        #When the control is swithced, try to make the other player accords with the player with the ball. 
        
        #If the player with the ball is greater than half of the line and is in the left, make the accompanying player move in a slow speed up. Trying to go to the point where it is 30 degrees above the home player. 
        strategicMoveHome(data)
        # strategicMoveVisiting(data)
            
            # if(data.team2[data.playerHomeIndex].y < (data.height / 4)):
            #     data.team2[1].makingMoveInPenaltyArea()
        
        # if(data.playerHomeIndex == 1):
        #     if(data.team1[1].y < (data.height / 2) and 
        #        data.team1[1].y >= (data.height /4 )and 
        #        data.team1[1].x < (data.width) / 2):
        #         data.team1[0].makingMoveUpperFieldRightSide(data.team1[1])
            # if(data.team2[data.playerHomeIndex].y < (data.height / 4)):
            #     data.team2[1].makingMoveInPenaltyArea()
        
        
        
        #This is the central control of how to react when collided
        if(data.soccerMovingState == True and data.collided == True):
            data.collidedSpeed = data.collidedSpeed + 0.07
            if(abs(data.collidedSpeed-0)<0.1):
                data.soccerMovingState = False
                data.collided = False
                data.collidedSpeed = 1.5
            data.soccerBall.reactToKick(data.team1[data.playerHomeIndex].collideWithSoccerBallCheck(data.soccerBall)[1],data.collidedSpeed)
        
        #Check if the player hits a soccer ball
        if(data.team1[data.playerHomeIndex].collideWithSoccerBallCheck(data.soccerBall)[0]):
            data.soccerMovingState = True
            data.direction = data.team1[data.playerHomeIndex].collideWithSoccerBallCheck(data.soccerBall)[1]
            
        #Check if the player hits a wall. If he hits a wall, makes him freeze
        data.team1[data.playerHomeIndex].collideWithWallCheck(data.leftBoarder,data.rightBoarder,data.lowerBoarder,data.upperBoarder)
        
        #Check if a player hits a visiting team player, if so, he can't move forward anymore. 
        for i in data.team2:
            if(data.team1[data.playerHomeIndex].collideWithOtherTeamCheck(i)):
                data.team1[data.playerHomeIndex].move(data.team1[data.playerHomeIndex].collideWithOtherTeamCheck(i)[0])
                
        #Check if a player hits a home team player, if so, he can't move forward anymore
        for i in range(len(data.team1)):
            if(i == data.playerHomeIndex):
                continue
            else:
                if(data.team1[data.playerHomeIndex].collideWithSameTeamCheck(data.team1[i])):
                    data.team1[data.playerHomeIndex].move(data.team1[data.playerHomeIndex].collideWithSameTeamCheck(data.team1[i])[0])
    

    
            
            
def draw(canvas,data):
    if(data.mode == "blueTeamWinState"):
        canvas.create_text(250,250,text = "Congratulations!",font = "30")
    if(data.mode == "redTeamWinState"):
        canvas.create_text(250,250,text = "Tough Loss",font = "30")
    if (data.mode == "startScreen"):
        canvas.create_rectangle(0,0,500,500,fill = "green")
        canvas.create_text(250,250,text = "Exciting Soccer Game",fill = "orange",
        font="Times 28 bold italic")
        canvas.create_image(125,125,image = data.Barcelona)
        canvas.create_image(125,375,image = data.Juventus)
        canvas.create_image(375,125,image = data.realMadrid)
        canvas.create_image(375,375,image = data.Bayern)
    if(data.mode == "gameState"):
        canvas.create_image(data.width/2,data.height/2,image = data.picture)
        canvas.create_text(40,50,text = "BlueTeam:%d"%data.blueTeamScore,font = "Times 12 italic")
        canvas.create_text(40,70,text = "RedTeam:%d"%data.redTeamScore,font = "Times 12 italic")
        for i in data.team1:
            i.draw(canvas)
        for i in data.team2:
            i.draw(canvas)
        data.soccerBall.draw(canvas)
    
    if(data.mode == "levelSelection"):
        levelColor = "indian red"
        canvas.create_rectangle(0,0,500,500,fill = "orange")
        canvas.create_text(200,200,text = "Choose Your Level", font = "Times 28 bold italic",)
        canvas.create_rectangle(200,300,400,350,fill = levelColor,outline = levelColor)
        canvas.create_text(300,325,text = "intramural", font = "Times 18")
        canvas.create_rectangle(200,375,400,425,fill = levelColor,outline = levelColor)
        canvas.create_text(300,400,text = "club",font = "Times 18")
        canvas.create_rectangle(200,450,400,500,fill = levelColor,outline = levelColor)
        canvas.create_text(300,475,text = "professional",font = "Times 18")
        
    
    
def redrawAll(canvas, data):
    # draw in canvas
    draw(canvas, data)
    pass

####################################
# use the run function as-is
#####################################

#Important!!!This code Is directly cited from 15112 course note. 
#This is the link to the website. Thank you! https://www.cs.cmu.edu/~112/notes/notes-graphics.html
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)
    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.timerDelay = 1
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)
from soccerBall import soccerBall
# from tkinter_soccer_game import data
import math
import random

class playerVisiting(object):
    #Model
    def __init__(self,x,y,speed,supportingSpeed,theFixedPoint):
        self.x = x
        self.y = y
        self.theFixedPoint = theFixedPoint
        self.supportingDistanceOffense = 200
        self.supportingDistanceDefense = 100
        self.supportingSpeed = supportingSpeed
        self.initialX = self.x
        self.initialY = self.y
        self.speed = speed
        self.r = 15
        self.jersey = "Red"
        self.leftPostX = 187.5
        self.rightPostX = 312.5
        leftPostX = int(self.leftPostX)
        rightPostX = int(self.rightPostX)
    #View
    def draw(self,canvas):
        canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r
        ,self.y + self.r,fill = self.jersey)
    
    #Control
    def move(self,direction,speed):
        self.x = self.x + self.speed * math.cos(math.radians(direction))
        self.y = self.y - self.speed * math.sin(math.radians(direction))
        
    def reset(self):
        self.x = self.initialX
        self.y = self.initialY
    
    def machineMove(self,direction):
        self.x = self.x + self.supportingSpeed * math.cos(math.radians(direction))
        self.y = self.y - self.supportingSpeed * math.sin(math.radians(direction))
    
    def smartAngleFunction(self,selfX,selfY,otherX, otherY):
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
    
    def makingMoveUpperFieldRightSide(self,other):
        if (not isinstance(other,playerVisiting)):
            return False
        else:
            runToX = other.x + self.supportingDistanceOffense * math.cos(math.radians(320))
            runToY = other.y - self.supportingDistanceOffense * math.sin(math.radians(320))
            angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
            self.machineMove(angleTowardsPosition)
            if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
                return True
            else:
                return False
    
    def makingMoveUpperFieldLeftSide(self,other):
        if (not isinstance(other,playerVisiting)):
            return False
        else:
            runToX = other.x + self.supportingDistanceOffense * math.cos(math.radians(220))
            runToY = other.y - self.supportingDistanceOffense * math.sin(math.radians(220))
            angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
            self.machineMove(angleTowardsPosition)
            if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
                return True
            else:
                return False
                
    def makingMoveLowerFieldRightSide(self,other):
        if (not isinstance(other,playerVisiting)):
            return False
        else:
            runToX = other.x + self.supportingDistanceDefense * math.cos(math.radians(40))
            runToY = other.y - self.supportingDistanceDefense * math.sin(math.radians(40))
            angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
            self.machineMove(angleTowardsPosition)
            if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
                return True
            else:
                return False
                
    # def makingMoveUpperFieldLeftSide(self,other):
    #     if(not isinstance(other, playerHome)):
    #         return False
    #     else:
    #         runToX = other.x + self.supportingDistanceOffense * math.cos(math.radians(140))
    #         runToY = other.y - self.supportingDistanceOffense * math.sin(math.radians(140))
    #         angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
    #         self.machineMove(angleTowardsPosition)
    #         if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
    #             return True
    #         else:
    #             return False
    #         
    # def makingMoveLowerFieldRightSide(self,other):
    #     if(not isinstance(other,playerHome)):
    #         return False
    #     else:
    #         runToX = other.x + self.supportingDistanceDefense * math.cos(math.radians(320))
    #         runToY = other.y - self.supportingDistanceDefense * math.sin(math.radians(320))
    #         angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
    #         self.machineMove(angleTowardsPosition)
    #         if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
    #             return True
    #         else:
    #             return False
    #             
    # def makingMoveLowerFieldLeftSide(self,other):
    #     if(not isinstance(other,playerHome)):
    #         return False
    #     else:
    #         runToX = other.x + self.supportingDistanceDefense * math.cos(math.radians(220))
    #         runToY = other.y - self.supportingDistanceDefense * math.sin(math.radians(220))
    #         angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
    #         self.machineMove(angleTowardsPosition)
    #         if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
    #             return True
    #         else:
    #             return False
                
    # Check if the visiting player collides with the ball or not
    def collideWithSoccerBallCheck(self,other):
        if(not isinstance(other,soccerBall)):
            return False
        else:
            dist = ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5
            if((other.x-self.x) == 0 and other.y < self.y):
                theta = 90
                finalDirection = 90
            elif((other.x-self.x) == 0 and other.y > self.y):
                theta = 270
                finalDirection = 270
            elif((other.x-self.x) > 0 and other.y == self.y):
                theta = 0
                finalDirection = 0
            elif((other.x-self.x) < 0 and other.y == self.y):
                theta = 0
                finalDirection = 180
            else:
                theta = math.atan((abs(other.y - self.y))/(abs(other.x-self.x)))
                theta = math.degrees(theta)
                if(other.x-self.x)>0 and (other.y-self.y)<0:
                    finalDirection = theta
                if(other.x-self.x<0) and (other.y-self.y)<0:
                    finalDirection = 180-theta
                if(other.x-self.x<0) and (other.y-self.y)>0:
                    finalDirection = 180+theta
                if(other.x-self.x>0) and (other.y-self.y)>0:
                    finalDirection = 360-theta
            return dist < self.r + other.r,finalDirection
            
    #Check if the visiting player collides with the ball or not
    def collideWithSameTeamCheck(self,other):
        if(not isinstance(other,playerVisiting)):
            return [False,0]
        else:
            dist = ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5
            direction = self.smartAngleFunction(self.x,self.y,other.x,other.y)
            bounceDirection = direction + 180
            if(dist < self.r + other.r):
                return [True,bounceDirection]
            else:
                return [False,bounceDirection]
    
    #Check if the visiting player collides with the ball or not
    def collideWithOtherTeamCheck(self,other):
        from playerHome import playerHome
        if(not isinstance(other,playerHome)):
            return [False,0]
        else:
            dist = ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5
            direction = self.smartAngleFunction(self.x,self.y,other.x,other.y)
            bounceDirection = direction + 180
            if(dist < self.r + other.r):
                return [True,bounceDirection]
            else:
                return [False,bounceDirection]
    
    #Bounce in the direction where the ball comes from            
    def bounce(self,other):
        self.x = self.x + math.cos(math.radians(self.collideWithOtherTeamCheck(other)[1]))*2
        self.y = self.y - math.sin(math.radians(self.collideWithOtherTeamCheck(other)[1]))*2
        
    #Return the direction of where the ball should move
    def ballShootingDirectionWhenReady(self,other):
        if(not isinstance(other,soccerBall)):
            return False
        else:
            return self.smartAngleFunction(self.x,self.y,other.x,other.y)
    
    #This is where the ball should move to to make a shot
    def ballShootingStartingPoint(self,other):
        if(not isinstance(other, soccerBall)):
            return False
        else:
            intermediateDirection = 0
            if((other.x - (self.leftPostX + 10) == 0)):
                intermediateDirection = 270
            theta = math.atan((abs(other.y - 470)/abs(other.x - (self.leftPostX + 10))))
            theta = math.degrees(theta)
            if(other.x > self.theFixedPoint):
                intermediateDirection = theta
            if(other.x < self.theFixedPoint):
                intermediateDirection = 180 - theta
            newX = other.x + math.cos(math.radians(intermediateDirection)) * 30
            newY = other.y - math.sin(math.radians(intermediateDirection)) * 30
            return [newX,newY]
    
    #This is where the ball should move to to reach that shooting point
    def ballChasingDirection(self,other):
        if(not isinstance(other,soccerBall)):
            return False
        else:
            startingPointX = self.ballShootingStartingPoint(other)[0]
            startingPointY = self.ballShootingStartingPoint(other)[1]
            beta = math.atan(startingPointX/startingPointY)
            beta = math.degrees(beta)
            if((startingPointX - self.x) > 0 and (startingPointY - self.y)<0):
                finalDirection = beta 
            if((startingPointX - self.x) < 0 and (startingPointY - self.y) < 0):
                finalDirection = 180 - beta
            if(startingPointX - self.x) < 0 and (startingPointY - self.y) > 0 :
                finalDirection = 180 + beta
            if(startingPointX - self.x) > 0 and (startingPointY - self.y) > 0:
                finalDirection = 360 - beta
            return finalDirection
            
#Check if the ball is at the right position to fire
    def checkInFirePosition(self,other):
        if((abs(self.x-self.ballShootingStartingPoint(other)[0]) < 0.2)
        and (abs(self.y - self.ballShootingStartingPoint(other)[1]) < 0.2)):
            return True
        else:
            return False
    
    
            
                
                
                
        
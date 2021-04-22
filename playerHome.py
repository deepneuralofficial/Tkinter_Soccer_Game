from playerVisiting import playerVisiting
from soccerBall import soccerBall
import math
class playerHome(object):
    #Model
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.initialX = self.x
        self.initialY = self.y
        self.speed = 10
        self.r = 15
        self.supportingDistanceOffense = 200
        self.supportingDistanceDefense = 100
        self.supportingSpeed = 0.2
        self.jersey = "Blue"
    #View
    def draw(self,canvas):
        canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r
        ,self.y + self.r,fill = self.jersey)
    
    #Control
    def reset(self):
        self.x = self.initialX
        self.y = self.initialY
        
    def move(self,direction):
        if(direction == "up"):
            self.x = self.x + self.speed * math.cos(math.radians(90))
            self.y = self.y - self.speed * math.sin(math.radians(90))
        elif(direction == "down"):
            self.x = self.x + self.speed * math.cos(math.radians(270))
            self.y = self.y - self.speed * math.sin(math.radians(270))
        elif(direction == "left"):
            self.x = self.x + self.speed * math.cos(math.radians(180))
            self.y = self.y - self.speed * math.sin(math.radians(180))
        elif(direction == "right"):
            self.x = self.x + self.speed * math.cos(math.radians(0))
            self.y = self.y - self.speed * math.sin(math.radians(0))
    
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
            
    #Making move in Upper Field, trying to move toward a point where the supporting player is twenty degree * 40pixels above the attacking player. 
    def makingMoveUpperFieldRightSide(self,other):
        if (not isinstance(other,playerHome)):
            return False
        else:
            runToX = other.x + self.supportingDistanceOffense * math.cos(math.radians(40))
            runToY = other.y - self.supportingDistanceOffense * math.sin(math.radians(40))
            angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
            self.machineMove(angleTowardsPosition)
            if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
                return True
            else:
                return False
    
    def makingMoveUpperFieldLeftSide(self,other):
        if(not isinstance(other, playerHome)):
            return False
        else:
            runToX = other.x + self.supportingDistanceOffense * math.cos(math.radians(140))
            runToY = other.y - self.supportingDistanceOffense * math.sin(math.radians(140))
            angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
            self.machineMove(angleTowardsPosition)
            if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
                return True
            else:
                return False
            
    def makingMoveLowerFieldRightSide(self,other):
        if(not isinstance(other,playerHome)):
            return False
        else:
            runToX = other.x + self.supportingDistanceDefense * math.cos(math.radians(320))
            runToY = other.y - self.supportingDistanceDefense * math.sin(math.radians(320))
            angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
            self.machineMove(angleTowardsPosition)
            if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
                return True
            else:
                return False
                
    def makingMoveLowerFieldLeftSide(self,other):
        if(not isinstance(other,playerHome)):
            return False
        else:
            runToX = other.x + self.supportingDistanceDefense * math.cos(math.radians(220))
            runToY = other.y - self.supportingDistanceDefense * math.sin(math.radians(220))
            angleTowardsPosition = self.smartAngleFunction(self.x,self.y,runToX,runToY)
            self.machineMove(angleTowardsPosition)
            if(abs(self.x - runToX) < 20 and abs(self.y - runToY) < 20):
                return True
            else:
                return False
                
    def collideWithWallCheck(self,leftBoarder,rightBoarder,lowerBoarder,upperBoarder):
        if(self.x-self.r < 80):
            self.x = 90
        if(self.x + self.r > 420):
            self.x = 410
        if(self.y-self.r < 30):
            self.y = 40
        if(self.y + self.r > 470):
            self.y = 460
            
    def collideWithOtherTeamCheck(self,other):
        if(not isinstance(other,playerVisiting)):
            return False
        else:
            dist = ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5
            if(dist < self.r + other.r and other.x-self.x >= 0 and other.y-self.y<0):
                return "down",True
            if(dist < self.r + other.r and other.x-self.x < 0 and other.y-self.y<0):
                return "down",True
            if(dist < self.r + other.r and other.x-self.x < 0 and other.y-self.y>0):
                return "up",True
            if(dist < self.r + other.r and other.x-self.x >= 0 and other.y-self.y>0):
                return "up",True
            if(dist < self.r + other.r and other.x-self.x > 0 and other.y-self.y==0):
                return "left",True
            if(dist < self.r + other.r and other.x-self.x < 0 and other.y-self.y==0):
                return "right",True
    
    def collideWithSameTeamCheck(self,other):
        if(not isinstance(other,playerHome)):
            return False
        else:
            dist = ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5
            if(dist < self.r + other.r and other.x-self.x >= 0 and other.y-self.y<0):
                return "down",True
            if(dist < self.r + other.r and other.x-self.x < 0 and other.y-self.y<0):
                return "down",True
            if(dist < self.r + other.r and other.x-self.x < 0 and other.y-self.y>0):
                return "up",True
            if(dist < self.r + other.r and other.x-self.x >= 0 and other.y-self.y>0):
                return "up",True
            if(dist < self.r + other.r and other.x-self.x > 0 and other.y-self.y==0):
                return "left",True
            if(dist < self.r + other.r and other.x-self.x < 0 and other.y-self.y==0):
                return "right",True
                
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
            return dist < self.r + other.r + 5,finalDirection
            
        

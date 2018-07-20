from turtle import *
import random
import time

SIZE = 20

class Part(RawTurtle):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        #self.shape("snake.gif")
        
    def drawSelf(self, turtle):
        turtle.goto(self.x - SIZE // 2 -1, self.y - SIZE // 2 -1)
        if random.random() < 0.5:
            turtle.color("blue")
        else:
            turtle.color("black")
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(SIZE - SIZE // 10)
            turtle.left(90)
        turtle.end_fill()
        
class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def changeLocation(self):
        self.x = random.randint(0, SIZE) * SIZE - 200
        self.y = random.randint(0, SIZE) * SIZE - 200
        
    def drawSelf(self, turtle):
        turtle.goto(self.x - SIZE // 2 - 1, self.y - SIZE // 2 -1)
        turtle.color("red")
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(SIZE - SIZE // 10)
            turtle.left(90)
        turtle.end_fill()
            
        
class Snake:
    def __init__(self, screen):
        self.headPosition = [SIZE, 0]
        self.screen = screen
        self.body = [Part(-SIZE, 0, self.screen), Part(0,0, self.screen), Part(SIZE, 0, self.screen)]
        self.nextX = 1
        self.nextY = 0
        self.crashed = False
        self.nextposition = [self.headPosition[0] + SIZE * self.nextX, self.headPosition[1] + SIZE * self.nextY]
    
    def moveOneStep(self):
        self.body.append(Part(self.nextposition[0], self.nextposition[1], self.screen)) 
        del self.body[0]
        self.headPosition[0], self.headPosition[1] = self.body[-1].x, self.body[-1].y 
        self.nextposition = [self.headPosition[0] + SIZE * self.nextX, self.headPosition[1] + SIZE * self.nextY]
            
    def testCollision(self):
        for i in range(len(self.body)-1):
            if self.nextposition[0] == self.body[i].x and self.nextposition[1] == self.body[i].y:
                self.crashed = True
        if self.nextpositon[0] < 900 or self.nextpositon[0] < 0 or self.nextposition[1] > 900 or self.nextposition[1] < 0:
            self.crashed = True
                    
            
    def moveUp(self):
        if self.nextX != 0 and self.nextY != -1:
            self.nextX, self.nextY = 0, 1
    def moveLeft(self):
        if self.nextX != 1 and self.nextY != 0:
            self.nextX, self.nextY = -1, 0
    def moveRight(self):
        if self.nextX != -1 and self.nextY != 0:
            self.nextX, self.nextY = 1, 0
    def moveDown(self):
        if self.nextX != 0 and self.nextY != 1:
            self.nextX, self.nextY = 0, -1
    def eatApple(self):
        self.body.append(Part(self.nextposition[0], self.nextposition[1], self.screen))
        self.headPosition[0], self. headPosition[1] = self.body[-1].x, self.body[-1].y
        self.nextPositon = [self.headPosition[0] + SIZE * self.nextX, self.headPosition[1] + SIZE * self.nextY]
    
    def drawSelf(self, turtle):
        if not self.crashed:
            for part in self.body:
                part.drawSelf(turtle)
        if self.crashed:
            turtle.write("Game Over!", move = False, align = "center", font = ("Arial", 20, "normal"))
            
class Game():
    def __init__(self):
        self.screen = Screen()
        self.screen.setworldcoordinates(-300, -300, 300, 300)
        self.artist = Turtle(visible = False)
        self.artist.up()
        self.artist.speed("slowest")
        
        self.snake = Snake(self.screen)
        self.apple = Apple(100,0)
        self.commandpending = False
        
        self.screen.tracer(0)
        #self.screen.register_shape("snake.gif")
        
        self.screen.listen()
        self.screen.onkey(self.snakeDown, "Down")
        self.screen.onkey(self.snakeUp, "Up")
        self.screen.onkey(self.snakeLeft, "Left")
        self.screen.onkey(self.snakeRight, "Right")
        
        self.screen.onkey(self.snakeDown, "s")
        self.screen.onkey(self.snakeUp, "w")
        self.screen.onkey(self.snakeLeft, "a")
        self.screen.onkey(self.snakeRight, "d")
        
        
    def nextFrame(self):
        self.artist.clear()
        if not self.snake.crashed:
            if (self.snake.nextposition[0], self.snake.nextposition[1]) == (self.apple.x, self.apple.y):
                self.snake.eatApple()
                self.apple.changeLocation()
            else:
                self.snake.moveOneStep()
            
            self.apple.drawSelf(self.artist)
            self.snake.drawSelf(self.artist)
            self.screen.update()
            self.screen.ontimer(lambda: self.nextFrame(), 100)      
            self.snake.testCollision()
        else:
            self.snake.drawSelf(self.artist)
        
    def snakeUp(self):
        if not self.commandpending: 
            self.commandpending = True
            self.snake.moveUp()
            self.commandpending = False
    
    def snakeDown(self):
        if not self.commandpending:
            self.commandpending = True
            self.snake.moveDown()
            self.commandpending = False
    
    def snakeLeft(self):
        if not self.commandpending:
            self.commandpending = True
            self.snake.moveLeft()
            self.commandpending = False
    
    def snakeRight(self):
        if not self.commandpending:
            self.commandpending = True
            self.snake.moveRight()
            self.commandpending = False
    
game = Game()
        
screen = Screen()
        
screen.ontimer(lambda: game.nextFrame(), 100)
        
screen.mainloop() 
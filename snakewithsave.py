from turtle import *
import random
import time

SIZE = 20

class Part(RawTurtle):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        
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
        self.body = []
        #self.body = [Part(-SIZE, 0, self.screen), Part(0,0, self.screen), Part(SIZE, 0, self.screen)]
        self.nextX = 1
        self.nextY = 0
        self.crashed = False
        self.menu = True
        self.nextPosition = [self.headPosition[0] + SIZE * self.nextX, self.headPosition[1] + SIZE * self.nextY]
    
    def moveOneStep(self):
        self.body.append(Part(self.nextPosition[0], self.nextPosition[1], self.screen)) 
        del self.body[0]
        self.headPosition[0], self.headPosition[1] = self.body[-1].x, self.body[-1].y 
        self.nextPosition = [self.headPosition[0] + SIZE * self.nextX, self.headPosition[1] + SIZE * self.nextY]
            
    def testCollision(self):
        for i in range(len(self.body)-1):
            if self.nextPosition[0] == self.body[i].x and self.nextPosition[1] == self.body[i].y:
                self.crashed = True
        if self.nextPosition[0] < -300 or self.nextPosition[0] > 300 or self.nextPosition[1] > 300 or self.nextPosition[1] < -300:
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
        self.body.append(Part(self.nextPosition[0], self.nextPosition[1], self.screen))
        self.headPosition[0], self. headPosition[1] = self.body[-1].x, self.body[-1].y
        self.nextPositon = [self.headPosition[0] + SIZE * self.nextX, self.headPosition[1] + SIZE * self.nextY]

    def drawSelf(self, turtle):
        if self.menu:
            turtle.goto(0,0)
            turtle.color("black")
            turtle.write("Welcome to Snake", move = False, align = "center", font = ("Arial", 80, "bold"))
            turtle.goto(0, -30)
            turtle.color("red")
            turtle.write("Press \"c\" to continue your game. \t Press \"n\" for new Game.", move = False, align = "center", font = ("Arial", 30, "normal"))
            turtle.goto(0, -300)
            turtle.color("blue")
            turtle.write("Danielle Bottiger and Elizabeth Ding's Research Project", move = False, align = "center", font = ("Arial", 30, "normal"))
        elif not self.crashed:
            for part in self.body:
                part.drawSelf(turtle)
        elif self.crashed:
            if self.nextPosition[0] > 300:
                turtle.write("Game Over!", move = False, align = "right", font = ("Arial", 20, "normal"))
                turtle.goto(turtle.xcor(), turtle.ycor()- 15)
                turtle.write("Press \"n\" to play again!", move = False, align = "right", font = ("Arial", 20, "normal"))               
            elif self.nextPosition[0] < -300:
                turtle.write("Game Over!", move = False, align = "left", font = ("Arial", 20, "normal"))
                turtle.goto(turtle.xcor(), turtle.ycor()- 15)
                turtle.write("Press \"n\" to play again!", move = False, align = "left", font = ("Arial", 20, "normal"))
            elif self.nextPosition[1] < -300:
                turtle.goto(turtle.xcor(), turtle.ycor()+ 15)
                turtle.write("Game Over!", move = False, align = "center", font = ("Arial", 20, "normal"))
                turtle.goto(turtle.xcor(), turtle.ycor()- 15)
                turtle.write("Press \"n\" to play again!", move = False, align = "center", font = ("Arial", 20, "normal"))                
            else:
                turtle.write("Game Over!", move = False, align = "center", font = ("Arial", 20, "normal"))
                turtle.goto(turtle.xcor(), turtle.ycor()- 15)
                turtle.write("Press \"n\" to play again!", move = False, align = "center", font = ("Arial", 20, "normal"))
            
class Game():
    def __init__(self):
        self.screen = Screen()
        self.reader = Save()
        self.screen.setworldcoordinates(-320, -320, 320, 320)
        self.artist = Turtle(visible = False)
        self.artist.up()
        self.artist.speed("slowest")
        
        self.snake = Snake(self.screen)
        self.apple = Apple(100,0)
        self.commandpending = False
        
        self.screen.tracer(0)
        
        self.screen.listen()
        self.screen.onkey(self.snakeDown, "Down")
        self.screen.onkey(self.snakeUp, "Up")
        self.screen.onkey(self.snakeLeft, "Left")
        self.screen.onkey(self.snakeRight, "Right")
        
        self.screen.onkey(self.snakeDown, "s")
        self.screen.onkey(self.snakeUp, "w")
        self.screen.onkey(self.snakeLeft, "a")
        self.screen.onkey(self.snakeRight, "d")
        
        self.screen.onkey(self.save, "Shift_L")
        self.screen.onkey(self.save, "Shift_R")
        
        
    def nextFrame(self):
        if not self.snake.menu:
            self.artist.clear()
        if not self.snake.crashed and not self.snake.menu:
            if (self.snake.nextPosition[0], self.snake.nextPosition[1]) == (self.apple.x, self.apple.y):
                self.snake.eatApple()
                self.apple.changeLocation()
            else:
                self.snake.moveOneStep()
            
            self.apple.drawSelf(self.artist)
            self.snake.drawSelf(self.artist)
            self.screen.update()
            self.screen.ontimer(lambda: self.nextFrame(), 100)      
            self.snake.testCollision()
        elif self.snake.menu or self.snake.crashed:
            self.snake.drawSelf(self.artist)
            self.screen.onkey(self.newGame,"n")
            self.screen.onkey(self.continueGame, "c")
        
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
            
    def newGame(self):
        self.snake = Snake(self.screen)
        self.snake.body = [Part(-SIZE, 0, self.screen), Part(0,0, self.screen), Part(SIZE, 0, self.screen)]
        self.snake.menu = False
        self.apple = Apple(200,0)
        self.commandpending = False
        self.nextFrame()
        
    def continueGame(self):
        self.reader.read(self, self.apple, self.snake)
        self.snake.menu = False
        self.commandpending = False
        self.snake.crashed = False
        self.nextFrame()
        
    def save(self):
        self.reader.save(self.apple, self.snake)
    
class Save:
    def read(self, game, apple, snake):
        file = open("save.txt", "r")
        file1 = file.readlines()
        if len(file1) > 0:
            apple.x = int(file1[0])
            apple.y = int(file1[1])
            for x in range(2, len(file1), 2):
                snake.body.append(Part(int(x), int(x+1), snake.screen))
        else:
            game.newGame()
        
    def save(self, apple, snake):
        #find way to clear file when saving!
        file = open("save.txt", "w")
        file.truncate(0)
        file.write(str(apple.x) + "\n")
        file.write(str(apple.y) + "\n")
        for x in range(len(snake.body)):
            file.write(str(snake.body[x].x) + "\n")
            file.write(str(snake.body[x].y) + "\n")
        
game = Game()
        
screen = Screen()
        
screen.ontimer(lambda: game.nextFrame(), 100)
        
screen.mainloop() 
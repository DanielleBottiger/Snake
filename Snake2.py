from turtle import *
import tkinter
import random
import time

screenMaxX = 300
screenMaxY = 300
screenMinX = -300
screenMinY = -300

class SnakePart(RawTurtle):
    def __init__(self, cv, dx, dy, colIndex, rowIndex, root):
        super().__init__(cv)
        
        self.penup()
        self.shape("snake.gif")
        self.dx = dx
        self.dy = dy
        self.root = root
    
    def move(self):
        newx = self.xcor() + self.dx
        newy = self.ycor() + self.dy
        
        if newx < screenMinX:
            self.gameover()
        elif newy < screenMinY:
            self.gameover()
        elif newx > screenMaxX:
            self.gameover()
        elif newy > screenMaxY:
            self.gameover()
        else:
            self.goto(newx, newy)

    def gameover(self):
        print("Game Over")
        self.root.destroy()
        self.root.quit()
        
class SnakeApplication(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)
        self.matrix = []
        self.buildWindow()
    
    def buildWindow(self):
        root = self.master
        root.title("Snake")
        cv = ScrolledCanvas(root, 600,600,600,600)
        cv.pack(side = tkinter.LEFT)
        t = RawTurtle(cv)
        
        screen = t.getscreen()
        screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
        t.ht()
        screen.tracer(0)
        screen.register_shape("snake.gif")
        
        snakeList = []
        for part in range(len(snakeList)):
            snakeList[part].dx = -32        
        def animate():
            for snake in snakeList:
                snake.move()
                screen.update()
                time.sleep(0.1)
            screen.ontimer(animate)
        
        for i in range(5):
            snake = SnakePart(cv, 0, -32, 16, 16, root)
            snake.goto(0, -32*i)
            snakeList.append(snake)
        
        def quitHnadler():
            print("Good Bye")
            root.destroy()
            root.quit()
            
        quitButton = tkinter.Button(self, text = "Quit", command = quitHnadler)
        quitButton.pack()
        
        screen.ontimer(animate)
        def key(event):
            print("pressed", repr(event.char))
            if event.char == 'a':
                    snakeList[i].dx = -32
                    snakeList[i].dy = 0
                    time.sleep(0.1)                  
            if event.char == 's':
                    snakeList[i].dy = -32
                    snakeList[i].dx = 0
            if event.char == 'd':
                    snakeList[i].dx = 32
                    snakeList[i].dy = 0                   
            if event.char == 'w':
                    snakeList[i].dy = 32
                    snakeList[i].dx = 0      
        
        
        root.bind("<Key>", key)
            
def main():
    root = tkinter.Tk()
    snakeApp = SnakeApplication(root)
    snakeApp.mainloop()
    print("Program Execution Complete")
    
if __name__ == "__main__":
    main()
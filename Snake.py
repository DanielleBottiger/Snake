from turtle import *
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import random
import datetime

class Tile(RawTurtle):
    def __init__(self,canvas,screen,rowIndex,colIndex,matrix,gameApp):
        super().__init__(canvas)
        
        self.gameApp = gameApp
        self.rowIndex = rowIndex
        self.colIndex = colIndex
        self.matrix = matrix
        self.penup()
        
        self.shape("tile36.gif")
        self.screen = screen
        
        self.goto(30+colIndex*36,30+rowIndex*36)
        
class Snake(RawTurtle):
    def __init__(self, canvas, screen, rowIndex, colIndex, gameApp):
        super().__init__(canvas)
        
        self.gameApp = gameApp
        self.rowIndex = rowIndex
        self.colIndex = colIndex
        self.penup()
        
        self.shape("soccerball.gif")
        self.screen = screen
        
        self.goto(30+colIndex*36, 30+rowIndex*36)
    
    
class SnakeBody():
    def __init__(self, canvas, screen, gameApp, xd, yd):
        self.gameApp = gameApp
        self.body = []
        for x in range(4):
            part = Snake(canvas, screen, 8,8, gameApp)
            self.body.append(part)
        
        self.xd = 0
        self.yd = -1
        
    def move(self):
        for i in range(len(self.body)):
            part = self.body[i]
            newx = self.xd*36+part.colIndex*36+30
            newy = self.xd*36+part.colIndex*36+30
            part.goto(newx, newy)
        

# Brings up the actual Application for us
class SnakeApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.matrix = []
        self.buildWindow()
        self.running = True
        
    def buildWindow(self):
        self.master.title("Snake")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)       
        
        def tickTock():
                currentTime = datetime.datetime.now()
                elapsed = currentTime - self.startTime
                elapsedSeconds = elapsed.seconds
                self.elapsedTime.set(str(elapsedSeconds))
                if self.running:
                    self.master.after(1000,tickTock)       
        
        def newGame():
            theTurtle = RawTurtle(self.canvas)
            theTurtle.ht()
            screen = theTurtle.getscreen()
        
            screen.setworldcoordinates(0,600,600,0)  
            screen.clear()
            screen.tracer(0)
            self.screen = screen
        
            screen.register_shape("tile36.gif")
            screen.register_shape("bomb36.gif")
            screen.register_shape("soccerball.gif")
            
            for row in self.matrix:
                for tile in row:
                    tile.goto(-1000,-1000)      
            
            self.matrix = []
            self.tileNum = 256
            count = 0
            
            apple = random.randrange(256)
            
            for rowIndex in range(16):
                row = []
                
                for colIndex in range(16):
                    applecol = apple//16
                    applerow = apple%16
                    aTile = Tile(self.canvas,screen,rowIndex,colIndex,self.matrix,self)
                    
                    if applecol == colIndex and applerow == rowIndex:
                        aTile.shape("bomb36.gif")
                    
                row.append(aTile)
                    
                self.matrix.append(row)
            
            snakeBody = SnakeBody(self.canvas, screen, self, 0, -1)
            self.screen.update()
            self.startTime = datetime.datetime.now()
            self.master.after(1000,tickTock)
                
        fileMenu.add_command(label="New Game",command=newGame)
 
        fileMenu.add_command(label="Exit",command=self.master.quit)

        bar.add_cascade(label="File",menu=fileMenu)

        self.master.config(menu=bar)
    
        self.canvas = tkinter.Canvas(self,width=600,height=600)
        self.canvas.pack(side=tkinter.LEFT)
        
        sideBar = tkinter.Frame(self,padx=5,pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        
        timeLabel = tkinter.Label(sideBar,text="Elapsed Seconds")
        timeLabel.pack()
                
        self.elapsedTime = tkinter.StringVar()
        self.elapsedTime.set("0")
                
        self.timeElapsed = tkinter.Label(sideBar,textvariable=self.elapsedTime)
        self.timeElapsed.pack()        
        
        newGame()
        
    
def main():
    root = tkinter.Tk()
    SnakeApp = SnakeApplication(root)
    
    SnakeApp.mainloop()
    print("Program Execution Completed.")
    
if __name__ == "__main__":
    main()
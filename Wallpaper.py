import math
from tkinter import *

root = Tk()


CanvasSize= 1000

canvas = Canvas(root,height=CanvasSize,width=CanvasSize)
canvas.pack()

def CreateCircle(x,y,r,canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0,y0,x1,y1)

def PlotPixel(x, y, canvas):
    return CreateCircle(x,y,1,canvas)

def CreateWallpaper():
    corna = 5
    cornb = 5
    side = 20

    for i in range(0,CanvasSize):
        for j in range(0,CanvasSize):
            x = corna + i * side / 100
            y = cornb + j * side / 100
            c = math.floor(x * x + y * y)
            if(c % 10 == 0):
                PlotPixel(i,j,canvas)


CreateWallpaper()
root.mainloop()
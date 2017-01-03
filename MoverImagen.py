from tkinter import *
import time

tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

def movetriangleD(event):
    canvas.move(1,5,0)

def movetriangleAb(event):
    canvas.move(1,0,5)

def movetriangleA(event):
    canvas.move(1,0,-5)

def movetriangleI(event):
    canvas.move(1,-5,0)
    
canvas.bind_all('<KeyPress-Right>',movetriangleD)
canvas.bind_all('<KeyPress-Left>',movetriangleI)
canvas.bind_all('<KeyPress-Down>',movetriangleAb)
canvas.bind_all('<KeyPress-Up>',movetriangleA)

tk.mainloop()

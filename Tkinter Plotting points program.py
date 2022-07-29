import tkinter as tk
from tkinter import *
import random
from turtle import fillcolor

### global variables ###
width, height = 600, 745
c_width, c_height = width, height-145
dimensions = str(width)+"x"+str(height)
window = tk.Tk()
window.geometry(dimensions)
canvas = tk.Canvas(window, width=c_width, height=c_height, bg="white")
midH, midW = c_width/2, c_height/2
points, points2, points3, points4 = [0, 300, 10, 290, 10, 310], [
    300, 0, 290, 10, 310, 10], [300, 600, 290, 590, 310, 590], [600, 300, 590, 290, 590, 310]
canvas.grid(row=1, column=0, padx=5, pady=5)
x, y, x1, y1, x2, y2, x3, y3, = 320, 310, 290, 280, 280, 310, 290, 320
num, num1, num2, num3, xnum, xnum2 = 2, 2, -2, -2, 0, 1
Active, Active1 = 0, 0
poix1, poiy1, poix2, poiy2, poix3, poiy3, poix4, poiy4 = 0, 0, 0, 0, 0, 0, 0, 0
intro = 0

line = canvas.create_line(midW, 0, midW, height, width=3)
line = canvas.create_line(0, midH, width, midH, width=3)

L1X, L1Y, L2X, L2Y = -3, -3, 3, 3
A1X, A1Y, A2X, A2Y = -7, -3, 10, -6


def plot():
    lst = ["blue", "red", "green", "red", "pink", "black", "orange"]
    colour = random.choice(lst)
    canvas.create_oval(((int(plotpoint1.get())*10)+(c_width/2))-2, (((int(plotpoint2.get())*-1)*10)+(c_height/2))-2, ((int(
        plotpoint1.get())*10)+(c_width/2))+2, (((int(plotpoint2.get())*-1)*10)+(c_height/2))+2, width=5, outline=random.choice(lst))


def drawline():
    global Active, poix1, poiy1, poix2, poiy2, poix3, poiy3, poix4, poiy4
    lst = ["blue", "red", "green", "red", "pink", "black", "orange"]
    colour = random.choice(lst)
    x = 30
    b = int(linep2.get())
    y = int(linep1.get())*x+b
    poix1 = 30
    poiy1 = y
    p1 = y
    x = -30
    y = int(linep1.get())*x+b
    p2 = y
    poix2 = -30
    poiy2 = y
    canvas.create_line(30*10+(c_width/2), p1*-1*10+(c_height/2), -
                       30*10+(c_width/2), p2*-1*10+(c_height/2), width=5, fill=colour)
    Active += 1
   #  y = mx+b


def drawline2():
    global Active1, poix1, poiy1, poix2, poiy2, poix3, poiy3, poix4, poiy4
    lst = ["blue", "red", "green", "red", "pink", "black", "orange"]
    colour = random.choice(lst)
    x = 30
    b = int(linep4.get())
    y = int(linep3.get())*x+b
    poix3 = 30
    poiy3 = y
    p1 = y
    x = -30
    y = int(linep3.get())*x+b
    p2 = y
    poix3 = -30
    poiy3 = y
    canvas.create_line(30*10+(c_width/2), p1*-1*10+(c_height/2), -
                       30*10+(c_width/2), p2*-1*10+(c_height/2), width=5, fill=colour)
    Active1 += 1
    drawpoi()


def findIntersection():
    x = ((int(linep2.get())-int(linep4.get()))) / \
        ((int(linep3.get())-int(linep1.get())))
    y = (((int(linep1.get())*x) + (int(linep2.get()))))
    Label(text="point of intersection: " +
          str(x) + ", " + str(y)).place(x=10, y=700)


def drawpoi():
    if int(linep1.get()) == int(linep3.get()):
        Label(text="Lines are parralell no point of intersection").place(x=10, y=700)
    else:
        poi = findIntersection()


def drawpara():
    liist = ["blue", "red", "green", "red", "pink", "black", "orange"]
    colour = random.choice(liist)
    for x in range(-30, 30):
        #y = ax2+bx+c
        y = (int(a.get())*x**2) + (int(b.get())*x) + (int(c.get()))
        canvas.create_oval((x*10)-2+300, ((y*-1)*10)-2+300,
                           (x*10)+2+300, ((y*-1)*10)+2+300, width=1, outline=colour)
        inbe = 1
        while inbe != 99:
            x -= 0.01
            y = (int(a.get())*x**2) + (int(b.get())*x) + (int(c.get()))
            canvas.create_oval((x*10)-1+300, ((y*-1)*10)-1+300,
                               (x*10)+1+300, ((y*-1)*10)+1+300, width=1, outline=colour)
            inbe += 1

## draw grid ##


def drawstuff():
    global num, num1, num2, num3, xnum, xnum2, x, y, x1, x2, x3, y1, y2, y3
    for i in range(0, c_width, 10):
        canvas.create_line([(i, 0), (i, c_height)],
                           tag='grid_line', fill="grey")
    for i in range(0, c_height, 10):
        canvas.create_line([(0, i), (c_width, i)],
                           tag='grid_line', fill="grey")
        line = canvas.create_line(midW, 0, midW, height, width=3)
    for i in range(0, c_width, 10):
        canvas.create_text(x, y, text=num, fill="black",
                           font=('Andreas 8 bold'))
        x += 20
        num += 2
    for i in range(0, c_height, 10):
        canvas.create_text(x1, y1, text=num1, fill="black",
                           font=('Andreas 8 bold'))
        y1 -= 20
        num1 += 2
    for i in range(0, c_width, 10):
        canvas.create_text(x2, y2, text=num2, fill="black",
                           font=('Andreas 8 bold'))
        x2 -= 20
        num2 -= 2
    for i in range(0, c_height, 10):
        canvas.create_text(x3, y3, text=num3, fill="black",
                           font=('Andreas 8 bold'))
        y3 += 20
        num3 -= 2


### GUI ###
### Textbox for plotting points ###
plotpoint1 = StringVar()
plotpoint2 = StringVar()
p1 = Entry(window, textvariable=plotpoint1, width=3)
p2 = Entry(window, textvariable=plotpoint2, width=3)
Label(text="x").place(x=270, y=615)
Label(text="y").place(x=330, y=615)
p1.grid(row=710, column=0, sticky=N, ipadx=5)
p2.grid(row=710, column=0, sticky=E, ipadx=5, padx=225)
### Plot button/function ###

plotbutton = tk.Frame(window)
plotbutton.grid(row=720, column=0, sticky=E, padx=235)
bplot = tk.Button(plotbutton, text="Plot point",
                  bg="grey", command=lambda: plot())
bplot.pack(side=tk.LEFT)
### Line Drawing buttons ###
linep1 = StringVar()
linep2 = StringVar()
l1 = Entry(window, textvariable=linep1, width=2)
l1.grid(row=710, column=0, sticky=W, ipadx=2, padx=65)
l2 = Entry(window, textvariable=linep2, width=2)
l2.grid(row=710, column=0, sticky=W, ipadx=2, padx=110)
line1 = tk.Frame(window)
line1.grid(row=720, column=0, sticky=W, padx=15)
lineb = tk.Button(line1, text="Draw line 1", bg="grey",
                  command=lambda: drawline())
lineb.pack(side=tk.LEFT)

Label(text="Line 1: y=").place(x=0, y=615)
Label(text="x+").place(x=90, y=615)

### Line draw 2#

linep3 = StringVar()
linep4 = StringVar()
l3 = Entry(window, textvariable=linep3, width=2)
l3.grid(row=730, column=0, sticky=W, ipadx=2, padx=65)
l4 = Entry(window, textvariable=linep4, width=2)
l4.grid(row=730, column=0, sticky=W, ipadx=2, padx=110)
line3 = tk.Frame(window)
line3.grid(row=740, column=0, sticky=W, padx=15)
linec = tk.Button(line3, text="Draw line 2", bg="grey",
                  command=lambda: drawline2())
linec.pack(side=tk.LEFT)

Label(text="Line 2: y=").place(x=0, y=665)
Label(text="x+").place(x=90, y=665)

##### Parabola ########


a = StringVar()
b = StringVar()
c = StringVar()
a1 = Entry(window, textvariable=a, width=2)
a1.grid(row=730, column=0, sticky=E, ipadx=2, padx=170)
b1 = Entry(window, textvariable=b, width=2)
b1.grid(row=730, column=0, sticky=E, ipadx=2, padx=100)
c1 = Entry(window, textvariable=c, width=2)
c1.grid(row=730, column=0, sticky=E, ipadx=2, padx=55)
plotpara = tk.Frame(window)
plotpara.grid(row=740, column=0, sticky=E, padx=100)
plotpara = tk.Button(plotpara, text="Plot Grpah",
                     bg="grey", command=lambda: drawpara())
plotpara.pack(side=tk.RIGHT)
Label(text="y =").place(x=400, y=657)
Label(text="x^2 +").place(x=450, y=657)
Label(text="x +").place(x=515, y=657)


### Loop ####

simulationactive = True

while simulationactive == True:
    if intro == 0:
        drawstuff()
        intro = 1
    if Active == 1:
        lineb.config(bg="grey", state="disabled")
    if Active1 == 1:
        linec.config(bg="grey", state="disabled")
    canvas.create_text(295, 310, text=0, fill="black", font=('Andreas 8 bold'))
    canvas.create_polygon(points, fill='black')
    canvas.create_polygon(points2, fill='black')
    canvas.create_polygon(points3, fill='black')
    canvas.create_polygon(points4, fill='black')
    canvas.create_text(310, 20, text="y", fill="red",
                       font=('Helvetica 10 bold'))
    canvas.create_text(580, 290, text="x", fill="red",
                       font=('Helvetica 10 bold'))
    window.update()


window.mainloop()

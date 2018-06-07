from turtle import *
speed(0)
colors = ["red", "blue", "brown", "yellow", "grey","white"]
for i in range(6):
    fillcolor(colors[i])
    pencolor(colors[i])
    begin_fill()
    for _ in range(4):
        forward(100)
        left(90)
    forward(50)
    end_fill()
mainloop()


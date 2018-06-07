from turtle import *
speed(0)
colors = ["red", "blue", "brown", "yellow", "grey"]
for i in range(5):
    pencolor(colors[i])
    side = i +3
    for _ in range(side):
        forward(100)
        left(360 / side)
mainloop()
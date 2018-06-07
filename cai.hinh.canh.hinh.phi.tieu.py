from turtle import *
speed(0)
for i in range(4):
    if i % 2 == 0:
        pencolor("blue")
    else:
        pencolor("red")
    side = i + 3
    for _ in range(side):
        forward(100)
        left(360 / side)
mainloop()
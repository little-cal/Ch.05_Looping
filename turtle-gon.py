import turtle
side_num = int(input("How many sides do you want the polygon to be?\n:"))
for i in range(side_num):
    turtle.fd(100)
    turtle.rt(360/side_num)

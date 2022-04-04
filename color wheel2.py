from turtle import*
t=Turtle()
wn=Screen()
wn.title("COLOR WHEEL")
wn.bgcolor("black")
colors=["red","blue","pink","skyblue","yellow","violet","green","orange",]
import random
t.backward(250)
t.speed(0)
t.width(3)
t.begin_fill()
for i in range(200):
    colorchoice=random.choice(colors)
    t.color(colorchoice)
    t.forward(500)
    t.right(170)
t.end_fill()  
done()

import turtle
import time
import random
import threading

board = turtle.Screen()
board.bgcolor("black")
board.title("CatchTheTurtle")

score = 0








xcolors=["red","blue","yellow","purple","pink","SpringGreen","WhiteSmoke","turquoise","orange","maroon"]




x = turtle.Turtle()
x.shape("turtle")
x.color("yellow")
x.hideturtle()
x.penup()
def randommoves():
    for run in range(15):
        a = random.randint(-200,200)
        b = random.randint(-200,200)


        x.goto(a,b)
        x.showturtle()
        time.sleep(1)
        x.hideturtle()
def click(x,y):
    print("Tıklandı",x,y)






########score string#######
score=turtle.Turtle()
score.color("Green")
score.hideturtle()
score.penup()
score.goto(-140,320)
score.write(f"Score :{score}",font=("Courier",24,"normal"))




################# geri sayım#############
sayac = turtle.Turtle()
sayac.speed(200000)
sayac.color("red")
sayac.penup()
sayac.hideturtle()
sayac.goto(20,350)
sayac.color("red")
########## Sayaç Stringi #############

sayacstring = turtle.Turtle()
sayacstring.hideturtle()
sayacstring.color("red")
sayacstring.penup()
sayacstring.goto(-140,350)
sayacstring.write("Sayaç :",font=("Courier",24,"normal"))
sayacstring.color("black")


def update_score():
    global score
    score+=1
    score.clear()
    score.write(f"Score :{score}", font=("Courier", 24, "normal"))



def oyundöngüsü():
    for i in range(30, -1, -1):
        sayac.clear()
        sayac.write(i, align="center", font=("Courier", 24, "normal"))
        a = random.randint(-200, 200)
        b = random.randint(-200, 200)

        x.goto(a, b)
        x.showturtle()
        time.sleep(0.75)


        x.hideturtle()









oyundöngüsü()

#########Kaplumbağa yakalama###############

def click(x,y):
    print("Tıklandı",x,y)



board.onclick(click)














turtle.mainloop()





























board.done()
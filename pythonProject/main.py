import turtle
import time
import random
import threading

board = turtle.Screen()
board.bgcolor("black")
board.title("CatchTheTurtle")




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





########score string#######
score=turtle.Turtle()
score.color("Green")
score.hideturtle()
score.penup()
score.goto(-140,320)
score.write("Score :",font=("Courier",24,"normal"))




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


def countdown():
    for i in range(30, -1, -1):
        sayac.clear()  # Önceki sayıyı temizle
        sayac.write(i, align="center", font=("Courier", 24, "normal"))
        time.sleep(1)  # 1 saniye bekle


thread1 = threading.Thread(target=randommoves())
thread2 = threading.Thread(target=countdown())
thread1.start()
thread2.start()

thread1.join()
thread2.join()


#########Kaplumbağa yakalama###############















turtle.mainloop()





























board.done()
import turtle
import time

board = turtle.Screen()
board.bgcolor("black")
board.title("CatchTheTurtle")
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



for i in range(30, -1, -1):
    sayac.clear()  # Önceki sayıyı temizle
    sayac.write(i, align="center", font=("Courier", 24, "normal"))
    time.sleep(1)  # 1 saniye bekle






turtle.mainloop()



for i in range(30):
    time.sleep(1)
    print(i)























board.done()
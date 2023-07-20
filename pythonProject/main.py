import turtle
import time
import random

board = turtle.Screen()
board.title("Catch The Turtle")
board.bgcolor("black")
score = 0
font = ("Courier", 24, "normal")

turtle.tracer(0)

# Score Yazısı
scorewrite = turtle.Turtle()
scorewrite.penup()
scorewrite.hideturtle()
scorewrite.color("red")
scorewrite.goto(0, 350)
scorewrite.write(arg=f"Score : {score}", align="center", move=False, font=font)

# Sayac yazısı
countdown = turtle.Turtle()
countdown.penup()
countdown.hideturtle()
countdown.color("blue")
countdown.goto(0, 300)

# Kaçan Kaplumbağa
x = turtle.Turtle()
x.penup()
x.shape("turtle")
x.shapesize(2, 2, 1)
x.color("turquoise")
x.hideturtle()

####Ekrana oyun bitti yazdırma###

finish = turtle.Turtle()
finish.penup()
finish.color("purple")
finish.hideturtle()




def handle_click(x, y):
    global score
    score += 1
    scorewrite.clear()
    scorewrite.write(arg=f"Score : {score}", align="center", move=False, font=font)


for i in range(30, -1, -1):
    countdown.clear()
    countdown.write(arg=i, move=False, align="center", font=font)
    a = random.randint(-200, 200)
    b = random.randint(-200, 200)
    x.goto(a, b)
    x.showturtle()
    x.onclick(handle_click)
    board.update()
    time.sleep(1)
    x.hideturtle()
    if i == 0 :
        board.clear()
        board.bgcolor("black")
        x.hideturtle()
        countdown.hideturtle()
        scorewrite.hideturtle()
        x.clear()
        countdown.clear()
        scorewrite.clear()
        finish.write(arg=f"Game Finished\n Your Score: {score}",move=False,align="center",font=font)






board.mainloop()

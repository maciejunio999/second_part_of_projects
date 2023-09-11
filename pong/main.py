import turtle
import random
from tkinter import *
import tkinter
# You can use it but it sound questionable
#import winsound

def ping_pong(max_score):
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0) # dont update window by itself, we update it manualy, helps game to be faster


    score_a = 0
    score_b = 0
    bounce = 0


    paddle_a = turtle.Turtle()
    paddle_a.speed(0) # speed of animation
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup() # tell turtle not to draw free lines, (when he moves)
    paddle_a.goto(-350, 0)

    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    # everytime ball moves it moves by 2px
    n = random.randint(3, 15)/10
    m = random.randint(5, 15)
    ball.dy = n/(m+1)
    ball.dx = n - n/(m-1)


    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align='center', font=("Courier", 24, "normal"))

    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    # listen for clicking keyboard
    wn.listen()
    # when user pres 'w' use given function
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")

    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")


    while True:
        wn.update()

        # ball moving
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # borders for ball
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            #winsound.PlaySound("tada.wav", winsound.SND_ASYNC)
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            #winsound.PlaySound("tada.wav", winsound.SND_ASYNC)
        if ball.xcor() > 390:
            ball.goto(0, 0)
            score_a += 1
            ball.dx *= -1
            #winsound.PlaySound("tada.wav", winsound.SND_ASYNC)
        if ball.xcor() < -390:
            ball.goto(0, 0)
            score_b += 1
            ball.dx *= -1
            #winsound.PlaySound("tada.wav", winsound.SND_ASYNC)
        
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=("Courier", 24, "normal"))

        # paddle and ball bounce
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
            ball.setx(340)
            ball.dx *= -1
            if bounce % 7 == 1:
                r = random.randint(12,18)/10
                ball.dy *= r
            else:
                r = random.randint(7,13)/10
                ball.dy *= r
            bounce+=1
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
            ball.setx(-340)
            ball.dx *= -1
            if bounce % 7 == 1:
                r = random.randint(11,17)/10
                ball.dy *= r
            elif bounce % 7 == 2:
                r = (-1) * random.randint(8,12)/10
                ball.dy *= r
            else:
                r = random.randint(6,12)/10
                ball.dy *= r
            bounce+=1
        if max_score == score_a or max_score == score_b:
            score_label.config(text = f"Player A: {score_a}  Player B: {score_b}")
            wn.bye()



root = Tk()
root.title("Ping-Pong")
root.geometry('500x250') # windows size

w = Label(root, text='Menu', font='45')
w.pack()

upper_frame = Frame(root)
upper_frame.pack()

mid_frame = Frame(root)
mid_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack()


instruction_label = Label(upper_frame, text="First to score this amount wins")
instruction_label.pack()

AMOUNT_OF_GOALS = [i for i in range(2, 10)]
goal_amount_var = StringVar(root)
goal_amount_var.set(AMOUNT_OF_GOALS[0])
goal_amount_menu = OptionMenu(upper_frame, goal_amount_var, *AMOUNT_OF_GOALS)
goal_amount_menu.pack()

def c():
    ping_pong(int(goal_amount_var.get()))

start_button = Button(bottom_frame, text='Start', background='#5063C7', command=c)
start_button.pack()

score_label = Label(bottom_frame, text="")
score_label.pack()

if __name__ == '__main__':
    tkinter.mainloop()

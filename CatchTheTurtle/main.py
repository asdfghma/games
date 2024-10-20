import turtle as trtl
import random as rand

color = "green"
shape = "turtle"
pen = 3
score = 0

font_setup = ("Arial", 20, "normal")
timer = 30
counter_imterval = 1000
timer_up = False

abc = trtl.Turtle()
abc.pensize(pen)
abc.shape(shape)
abc.color(color)
abc.penup()

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pencolor(color)
score_writer.penup()
score_writer.goto(-100, -150)
score_writer.pendown()

timer_writer = trtl.Turtle()
timer_writer.hideturtle()
timer_writer.pencolor(color)
timer_writer.penup()
timer_writer.goto(-100, -100)
timer_writer.pendown()

def spot_clicked(x,y):
    global timer
    if timer > 0:
        abc.goto(x, y)
        update_score()
        change_position()
    else:
        abc.hideturtle()

def change_position():
    global abc
    abc.hideturtle()
    abc.penup()
    nexxpos = rand.randint(-200,200)
    nexypos = rand.randint(-125,125)
    abc.goto(nexxpos, nexypos)
    abc.showturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write("Score: " + str(score), font = font_setup)

def countdown():
    global timer, timer_up
    timer -= 1
    if timer <= 0:
        timer_up = True
        trtl.Screen().ontimer(countdown, counter_imterval)
        timer_writer.clear()
        timer_writer.write("Times's Up", font=font_setup)
    else:
        timer_writer.clear()
        timer_writer.write("Timer:" + str(timer), font=font_setup)
        trtl.Screen().ontimer(countdown, counter_imterval)


abc.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor("light blue")
wn.ontimer(countdown, counter_imterval)
wn.mainloop()



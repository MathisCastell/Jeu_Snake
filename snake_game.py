import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Jeu du serpent")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

tete = turtle.Turtle()
tete.speed(0)
tete.shape("square")
tete.color("black")
tete.penup()
tete.goto(0, 0)
tete.direction = "stop"

nourriture = turtle.Turtle()
nourriture.speed(0)
nourriture.shape("circle")
nourriture.color("red")
nourriture.penup()
nourriture.goto(0, 100)

segments = []

stylo = turtle.Turtle()
stylo.speed(0)
stylo.shape("square")
stylo.color("white")
stylo.penup()
stylo.hideturtle()
stylo.goto(0, 260)
stylo.write("Score: 0  Meilleur Score: 0", align="center", font=("Courier", 24, "normal"))

def monter():
    if tete.direction != "down":
        tete.direction = "up"

def descendre():
    if tete.direction != "up":
        tete.direction = "down"

def aller_a_gauche():
    if tete.direction != "right":
        tete.direction = "left"

def aller_a_droite():
    if tete.direction != "left":
        tete.direction = "right"

def deplacement():
    if tete.direction == "up":
        y = tete.ycor()
        tete.sety(y + 20)

    if tete.direction == "down":
        y = tete.ycor()
        tete.sety(y - 20)

    if tete.direction == "left":
        x = tete.xcor()
        tete.setx(x - 20)

    if tete.direction == "right":
        x = tete.xcor()
        tete.setx(x + 20)

wn.listen()
wn.onkeypress(monter, "z")
wn.onkeypress(descendre, "s")
wn.onkeypress(aller_a_gauche, "q")
wn.onkeypress(aller_a_droite, "d")

while True:
    wn.update()

    if tete.xcor() > 290 or tete.xcor() < -290 or tete.ycor() > 290 or tete.ycor() < -290:
        time.sleep(1)
        tete.goto(0, 0)
        tete.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear()

        score = 0
        delay = 0.1

        stylo.clear()
        stylo.write("Score: {}  Meilleur Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    if tete.distance(nourriture) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        nourriture.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score
        
        stylo.clear()
        stylo.write("Score: {}  Meilleur Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = tete.xcor()
        y = tete.ycor()
        segments[0].goto(x, y)

    deplacement()    

    for segment in segments:
        if segment.distance(tete) < 20:
            time.sleep(1)
            tete.goto(0, 0)
            tete.direction = "stop"
        
            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()
            score = 0
            delay = 0.1
        
            stylo.clear()
            stylo.write("Score: {}  Meilleur Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

turtle.mainloop()

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t
import random
import time

# screen
g = t.Screen()
g.title("Snake game")
g.bgcolor("black")
g.setup(width=700, height=700)
g.tracer(0)
delay = 0.1

# SCORE
score,hs = 0,0

# scoring board
gb = t.Turtle()
gb.speed(0)
gb.penup()
gb.shape("square")
gb.color("white")
gb.hideturtle()
gb.goto(0, 260)
gb.write("SCORE: " + str(score) + "  High Score: " + str(hs), align="center", font=("Lucida Calligraphy", 23, "italic"))
# snakes head
head = t.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# making food symbols
food = t.Turtle()
food.speed(0)
fc=random.choice(["orange","green"])
fsh=random.choice(["circle","square","triangle"])
food.shape(fsh)
food.color(fc)
food.penup()
food.goto(0, 100)

def move_u():
    if head.direction != "down":
        head.direction = "up"

def move_d():
    if head.direction != "up":
        head.direction = "down"

def move_r():
    if head.direction != "left":
        head.direction = "right"

def move_l():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

g.listen()
g.onkeypress(move_u, "w")
g.onkeypress(move_d, "s")
g.onkeypress(move_l, "a")
g.onkeypress(move_r, "d")

segments = []

while True:
    g.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"
        for j in segments:
            j.goto(1000, 1000)
        segments.clear()
        # reset the score
        score = 0

        #reset the delay
        delay=0.1

        gb.clear()
        gb.write("SCORE: " + str(score) + "  High Score: " + str(hs), align="center",font=("Lucida Calligraphy", 23, "italic"))

    # this part changes the coordinates of the food after the collision with the snake
    # generates random position
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        # add new segment
        sg = t.Turtle()
        sg.speed(0)
        sg.shape("square")
        sg.color("blue")
        sg.penup()
        segments.append(sg)

        #shorten the delay
        delay-=0.001
        # increase the score
        score += 10
        if score > hs:
            hs = score
        gb.clear()
        gb.write("SCORE: " + str(score) + "  High Score: " + str(hs), align="center",font=("Lucida Calligraphy", 23, "italic"))


    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for a in segments:
        if a.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"
            for j in segments:
                j.goto(1000, 1000)
            segments.clear()
            # set the score
            score = 0
            gb.clear()
            gb.write("SCORE: " + str(score) + "  High Score: " + str(hs), align="center",font=("Lucida Calligraphy", 23, "italic"))

    time.sleep(delay)

g.mainloop()


# In[ ]:





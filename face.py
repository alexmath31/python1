import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(1) 
pen.pensize(2)

def draw_mona_lisa():
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(100) 
    pen.end_fill()

    pen.penup()
    pen.goto(-30, 30)
    pen.pendown()
    pen.color("white")
    pen.dot(20)
    
    pen.penup()
    pen.goto(30, 30)
    pen.pendown()
    pen.dot(20)
    
    pen.penup()
    pen.goto(-30, 30)
    pen.pendown()
    pen.color("black")
    pen.dot(10)
    
    pen.penup()
    pen.goto(30, 30)
    pen.pendown()
    pen.dot(10)
    
    pen.penup()
    pen.goto(-20, -20)
    pen.pendown()
    pen.right(90)
    pen.circle(20, 180)

    pen.penup()
    pen.goto(-80, 50)
    pen.setheading(45)
    pen.pendown()
    pen.color("black")
    pen.width(3)
    pen.circle(100, 90)

draw_mona_lisa()

pen.hideturtle()
turtle.done()

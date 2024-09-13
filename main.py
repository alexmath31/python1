import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Setup the turtle
pen = turtle.Turtle()
pen.speed(1)  # Adjust the speed as needed
pen.pensize(2)

# Simplified outline of Mona Lisa
def draw_mona_lisa():
    # Draw the head (a simple oval for simplicity)
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(100)  # Simplified as a circle
    pen.end_fill()

    # Draw eyes
    pen.penup()
    pen.goto(-30, 30)
    pen.pendown()
    pen.color("white")
    pen.dot(20)
    
    pen.penup()
    pen.goto(30, 30)
    pen.pendown()
    pen.dot(20)
    
    # Draw pupils
    pen.penup()
    pen.goto(-30, 30)
    pen.pendown()
    pen.color("black")
    pen.dot(10)
    
    pen.penup()
    pen.goto(30, 30)
    pen.pendown()
    pen.dot(10)
    
    # Draw the mouth
    pen.penup()
    pen.goto(-20, -20)
    pen.pendown()
    pen.right(90)
    pen.circle(20, 180)  # Simplified mouth

    # Draw hair (simple arc)
    pen.penup()
    pen.goto(-80, 50)
    pen.setheading(45)
    pen.pendown()
    pen.color("black")
    pen.width(3)
    pen.circle(100, 90)  # Simple arc to resemble hair

# Call the function
draw_mona_lisa()

# Hide the pen and keep the window open
pen.hideturtle()
turtle.done()

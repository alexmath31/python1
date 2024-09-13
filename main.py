import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
flower = turtle.Turtle()
flower.speed(0)  # Fastest drawing speed
flower.width(2)

# List of colors to use
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# Draw a flower-like pattern
for i in range(36):
    flower.color(colors[i % len(colors)])  # Cycle through the colors
    flower.circle(100)  # Draw a circle of radius 100
    flower.right(10)  # Turn 10 degrees to the right

# Hide the turtle and display the window
flower.hideturtle()
turtle.done()

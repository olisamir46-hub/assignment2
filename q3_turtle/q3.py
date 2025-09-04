@@ -1,37 +1,80 @@
import turtle
import math

def draw_koch_edge(t, length, depth):
def setup_turtle():
    """Initialize turtle settings"""
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def draw_koch_segment(length, depth):
    """Recursively draw a Koch curve segment"""
    if depth == 0:
        t.forward(length)
        turtle.forward(length)
    else:
        length /= 3
        draw_koch_edge(t, length, depth-1)
        t.left(60)
        draw_koch_edge(t, length, depth-1)
        t.right(120)
        draw_koch_edge(t, length, depth-1)
        t.left(60)
        draw_koch_edge(t, length, depth-1)
        # Divide the segment into three parts
        segment_length = length / 3
        
        # Draw first segment
        draw_koch_segment(segment_length, depth - 1)
        
        # Turn left and draw the "triangle" part
        turtle.left(60)
        draw_koch_segment(segment_length, depth - 1)
        
        # Turn right and draw the next part
        turtle.right(120)
        draw_koch_segment(segment_length, depth - 1)
        
        # Turn left and draw the final segment
        turtle.left(60)
        draw_koch_segment(segment_length, depth - 1)

def draw_polygon(t, sides, length, depth):
def draw_koch_polygon(sides, side_length, depth):
    """Draw a Koch polygon with the given parameters"""
    # Calculate the angle for the polygon
    angle = 360 / sides
    
    # Position the turtle to center the drawing
    turtle.penup()
    
    # Calculate the starting position based on the polygon
    if sides % 2 == 0:  # Even number of sides
        start_x = -side_length / 2
        start_y = -side_length / (2 * math.tan(math.pi / sides))
    else:  # Odd number of sides
        start_x = -side_length / 2
        start_y = -side_length / (2 * math.tan(math.pi / sides))
    
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.setheading(0)
    
    # Draw each side of the polygon
    for _ in range(sides):
        draw_koch_edge(t, length, depth)
        t.right(angle)

# User inputs
sides = int(input("Enter number of sides: "))
length = int(input("Enter side length: "))
depth = int(input("Enter recursion depth: "))

# Turtle setup
t = turtle.Turtle()
t.speed('fastest')
screen = turtle.Screen()
screen.bgcolor("white")

draw_polygon(t, sides, length, depth)
        draw_koch_segment(side_length, depth)
        turtle.right(angle)

screen.mainloop()
def main():
    # Get user input
    sides = int(turtle.textinput("Number of Sides", "Enter the number of sides:"))
    side_length = float(turtle.textinput("Side Length", "Enter the side length:"))
    depth = int(turtle.textinput("Recursion Depth", "Enter the recursion depth:"))
    
    # Setup turtle
    setup_turtle()
    
    # Draw the pattern
    turtle.color("blue")
    turtle.begin_fill()
    draw_koch_polygon(sides, side_length, depth)
    turtle.end_fill()
    
    # Keep the window open until clicked
    turtle.exitonclick()

if _name_ == "_main_":
    main()

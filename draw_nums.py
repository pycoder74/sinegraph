import turtle

def draw_number(number, screen, turtle):
    turtle.speed(1)
    turtle.penup()
    turtle.pendown()
    turtle.write(str(number), align="center", font=("Arial", 20, "normal"))

if __name__ == '__main__':
    # Create a turtle screen
    screen = turtle.Screen()

    # Create a turtle object
    pen = turtle.Turtle()

    # Replace the argument with the number you want to draw
    draw_number(7, screen, pen)

    # Close the turtle graphics window when clicked
    screen.exitonclick()

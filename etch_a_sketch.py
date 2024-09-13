from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def forwards():
    tim.forward(10)

def backwards():
    tim.backward(10)

def left():
    tim.left(10)

def right():
    tim.right(10)

def clear():
    """
    Clear the drawing on the screen and reset the turtle to its initial state.
    
    This function clears the drawing, lifts the pen to move without drawing, 
    returns the turtle to the center of the screen, and then puts the pen down 
    to resume drawing if needed.
    """
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(forwards, "Up")    
screen.onkey(backwards, "Down") 
screen.onkey(left, "Left")      
screen.onkey(right, "Right")    
screen.onkey(clear, "c")       
screen.exitonclick()

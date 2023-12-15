
import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle() # create a turtle named alex
jamal = turtle.Turtle()
jamal.color('green')
alex.shape('turtle')
distance = 1
angle = 45
for _ in range(75):
    alex.forward(distance)
    alex.left(angle)
    jamal.forward(distance)
    jamal.right(angle)
    distance += 1

wn.exitonclick()

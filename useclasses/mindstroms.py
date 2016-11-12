import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor('red')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('blue')
    brad.speed(2)

    for j in range(36):
        for i in range(4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)

#    angie = turtle.Turtle()
##    angie.shape('arrow')
##    angie.color('green')
##    angie.circle(100)
##
##    tri = turtle.Turtle()
##    tri.shape('turtle')
##    tri.color('yellow')
##
##    for i in range(3):
##        tri.forward(100)
##        tri.right(120)
    
    
    window.exitonclick()

draw()

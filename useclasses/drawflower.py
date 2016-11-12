import turtle

def draw_rhombus(some_turtle,length,angel):
    for i in range(1,3):
        some_turtle.forward(length)
        some_turtle.left(180-angel)
        some_turtle.forward(length)
        some_turtle.left(angel)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor('white')

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('yellow')
    angie.speed(10)

    for i in range(1,73):
        draw_rhombus(angie,100,140)
        angie.right(5)

    angie.right(90)
    angie.forward(300)

 #   angie.right(150)
 #   draw_rhombus(angie,150,140)

 #   angie.right(60)
 #   draw_rhombus(angie,150,140)

    angie.hideturtle()

    window.exitonclick()

draw_flower()

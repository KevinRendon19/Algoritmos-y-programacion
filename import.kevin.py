import turtle

# Configuración de la ventana
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(3)
t.pensize(35)
t.shape("circle")

# Función para dibujar círculos de decoración
def draw_decorative_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Círculo de decoración antes de la letra K
draw_decorative_circle("aqua", 50, -400, 50)

# K
t.color("aqua")
t.penup()
t.goto(-400, -90)
t.pendown()
t.setheading(90)
t.fd(140)
t.penup()
t.goto(-400, 0)
t.setheading(45)
t.pendown()
t.fd(100)
t.penup()
t.goto(-400, 0)
t.setheading(-45)
t.pendown()
t.fd(100)

# Círculo de decoración antes de la letra E
draw_decorative_circle("lime", 50, -270, 50)

# E
t.color("lime")
t.penup()
t.goto(-270, 50)
t.setheading(270)
t.pendown()
t.fd(140)
t.backward(70)
t.setheading(0)
t.fd(60)
t.penup()
t.goto(-270, 50)
t.pendown()
t.fd(60)
t.penup()
t.goto(-270, -90)
t.pendown()
t.fd(60)

# Círculo de decoración antes de la letra V
draw_decorative_circle("magenta", 50, -100, 50)

# V
t.color("magenta")
t.penup()
t.goto(-100, 50)
t.setheading(-75)
t.pendown()
t.fd(150)
t.setheading(75)
t.fd(150)

# Círculo de decoración antes de la letra I
draw_decorative_circle("white", 50, 80, 50)

# I
t.color("white")
t.penup()
t.goto(80, -90)
t.setheading(90)
t.pendown()
t.fd(140)

# Círculo de decoración antes de la letra N
draw_decorative_circle("purple", 50, 160, 50)

# N
t.color("purple")
t.penup()
t.goto(160, -90)
t.setheading(90)
t.pendown()
t.fd(140)
t.setheading(-45)
t.fd(170)
t.setheading(90)
t.fd(140)

# Movimiento adicional decorativo
t.penup()
t.goto(-450, 200)
t.pendown()
t.color("yellow")
t.pensize(3)
t.circle(80, 180)  # Un semicírculo adicional para un toque extra de decoración

# Finaliza el dibujo
t.hideturtle()
turtle.done()

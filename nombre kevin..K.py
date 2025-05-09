import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Nombre KEVIN con tortuquita")


tortuquita = turtle.Turtle()
tortuquita.color("white")
tortuquita.pensize(5)
tortuquita.speed(2)


tortuquita.penup()
tortuquita.goto(-250, -100)  
tortuquita.pendown()
tortuquita.goto(-250, 100)  

tortuquita.penup()
tortuquita.goto(-250, 0)
tortuquita.pendown()
tortuquita.goto(-150, 100)  

tortuquita.penup()
tortuquita.goto(-250, 0)
tortuquita.pendown()
tortuquita.goto(-150, -100)  


tortuquita.penup()
tortuquita.goto(-100, 100)
tortuquita.pendown()
tortuquita.goto(-100, -100)  

tortuquita.penup()
tortuquita.goto(-100, 100)
tortuquita.pendown()
tortuquita.goto(-50, 100)  

tortuquita.penup()
tortuquita.goto(-100, 0)
tortuquita.pendown()
tortuquita.goto(-50, 0)  

tortuquita.penup()
tortuquita.goto(-100, -100)
tortuquita.pendown()
tortuquita.goto(-50, -100)  


tortuquita.penup()
tortuquita.goto(50, 100)
tortuquita.pendown()
tortuquita.goto(100, -100)  

tortuquita.penup()
tortuquita.goto(50, 100)
tortuquita.pendown()
tortuquita.goto(150, -100)  


tortuquita.penup()
tortuquita.goto(200, 100)
tortuquita.pendown()
tortuquita.goto(200, -100)  


tortuquita.penup()
tortuquita.goto(250, -100)
tortuquita.pendown()
tortuquita.goto(250, 100)  

tortuquita.penup()
tortuquita.goto(250, 100)
tortuquita.pendown()
tortuquita.goto(350, -100) 

tortuquita.penup()
tortuquita.goto(350, -100)
tortuquita.pendown()
tortuquita.goto(350, 100)  

turtle.done()

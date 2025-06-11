import turtle

t = turtle.Turtle()
t.speed(5)
t.color("blue")

for _ in range(5):
    t.forward(150)
    t.right(144)  # Ángulo para formar una estrella

turtle.done()
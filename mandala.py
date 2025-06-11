import turtle
t = turtle.Turtle()
t.speed(10)
colors = ["red", "blue", "green", "purple"]
for i in range(72):
    t.color(colors[i % 4])
    t.circle(100)
    t.left(5)
turtle.done()
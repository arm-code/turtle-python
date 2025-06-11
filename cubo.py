import turtle
import math

# Configuración inicial
pantalla = turtle.Screen()
pantalla.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(1)

radio = 40  # radio de los círculos
centros = []

# Función para mover sin dibujar
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Función para dibujar un círculo centrado en (x, y)
def dibujar_circulo(x, y, r):
    mover(x, y - r)
    t.setheading(0)
    t.circle(r)

# Crear los 13 centros (semilla de la vida expandida)
def generar_centros(r):
    centros = [(0, 0)]  # centro
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        x = math.cos(rad) * r
        y = math.sin(rad) * r
        centros.append((x, y))
    # Segunda capa alrededor
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        cx = math.cos(rad) * r
        cy = math.sin(rad) * r
        for inner_angle in range(0, 360, 60):
            inner_rad = math.radians(inner_angle)
            x = cx + math.cos(inner_rad) * r
            y = cy + math.sin(inner_rad) * r
            if (round(x, 2), round(y, 2)) not in centros:
                centros.append((x, y))
    return centros

# Dibujar todos los círculos
centros = generar_centros(radio)
for x, y in centros:
    dibujar_circulo(x, y, radio)

# Dibujar líneas entre todos los pares de centros
t.pensize(1)
for i in range(len(centros)):
    for j in range(i + 1, len(centros)):
        mover(*centros[i])
        t.goto(*centros[j])

t.hideturtle()
pantalla.mainloop()

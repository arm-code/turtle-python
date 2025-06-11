import turtle
import math

# Configuración inicial
pantalla = turtle.Screen()
pantalla.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

radio = 80  # Tamaño de los círculos

# Función para dibujar un círculo desde el centro
def dibujar_circulo_centro(x, y, radio):
    t.penup()
    t.goto(x, y - radio)
    t.setheading(0)
    t.pendown()
    t.circle(radio)

# Función para calcular posiciones hexagonales
def posiciones_hexagonales(x, y, radio, niveles):
    posiciones = [(x, y)]
    for nivel in range(1, niveles + 1):
        for i in range(6):
            angulo = math.radians(i * 60)
            for j in range(nivel):
                dx = math.cos(angulo) * radio * nivel
                dy = math.sin(angulo) * radio * nivel
                offset_x = -math.sin(angulo) * radio * j * 2
                offset_y = math.cos(angulo) * radio * j * 2
                pos_x = x + dx + offset_x
                pos_y = y + dy + offset_y
                if (pos_x, pos_y) not in posiciones:
                    posiciones.append((pos_x, pos_y))
    return posiciones

# Obtener posiciones y dibujar
centros = posiciones_hexagonales(0, 0, radio, 2)

for centro in centros:
    dibujar_circulo_centro(centro[0], centro[1], radio)

t.hideturtle()
pantalla.mainloop()

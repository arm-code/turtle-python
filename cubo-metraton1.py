import turtle
import math

# Configuración inicial
screen = turtle.Screen()
screen.title("Cubo de Metatrón - Versión Ampliada")
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)  # Máxima velocidad
t.color("gold")  # Color de los nodos
t.pensize(3)  # Líneas más gruesas

# --- Parámetros ajustables ---
radius = 25  # Aumenta el tamaño de los círculos (antes 15)
distance_multiplier = 5  # Aumenta la separación entre nodos (antes 3)
# ----------------------------

nodes = []
center_x, center_y = 0, 0

# Dibujar los 13 círculos (nodos)
def draw_circle(x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)
    nodes.append((x, y))

# Posiciones de los nodos
angles = [30 * i for i in range(12)]
for i in range(13):
    if i == 0:
        draw_circle(center_x, center_y)  # Nodo central
    else:
        angle = angles[i-1]
        distance = distance_multiplier * radius  # Aplica el multiplicador
        x = center_x + distance * math.cos(math.radians(angle))
        y = center_y + distance * math.sin(math.radians(angle))
        draw_circle(x, y)

# Conectar todos los nodos entre sí (líneas blancas más gruesas)
t.color("cyan")
t.pensize(2)  # Grosor de las conexiones
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        x1, y1 = nodes[i]
        x2, y2 = nodes[j]
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

# Opcional: Resaltar el círculo central
t.penup()
t.goto(center_x, center_y - radius - 5)
t.color("red")
t.write("Centro", align="center", font=("Arial", 12, "bold"))

t.hideturtle()
turtle.done()
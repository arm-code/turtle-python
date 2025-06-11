import turtle

# Configuración inicial
screen = turtle.Screen()
screen.title("Ejemplo de Turtle")

t = turtle.Turtle()  # Crea la tortuga

# Dibuja un cuadrado
for _ in range(4):
    t.forward(100)  # Avanza 100 píxeles
    t.right(90)     # Gira 90 grados

turtle.done()  # Mantiene la ventana abierta
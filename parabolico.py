from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)  # Posición inicial de la bola
speed = vector(0, 0)  # Velocidad inicial de la bola
targets = []  # Lista para almacenar los objetivos

# Función que responde al clic en la pantalla
def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):  # Si la bola está fuera de la pantalla
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15  # Aumenta la velocidad, pasando la posicion a velocidad 
        speed.y = (y + 200) / 15  # Aumenta la velocidad, pasando la posicion a velocidad

# Función que verifica si un punto está dentro de la pantalla
def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Función que dibuja los objetivos y la bola
def draw():
    """Draw ball and targets."""
    clear()
    
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')  # Dibuja los objetivos en azul

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')  # Dibuja la bola en rojo

    update()

# Función que mueve la bola y los objetivos
def move():
    """Move ball and targets."""
    if randrange(30) == 0:  # Hace que aparezcan más objetivos
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 3.2  # reduce el eje X en 3.2 unidades. Por lo que da la sensacion de ir mas rapido
        if target.x < -210:  # Si el objetivo sale de la ventana, lo reposiciona. Ya que mide 200x200
            target.x = 200  #reposiciona el objetivo
            target.y = randrange(-150, 150) #aleatorio en eje Y

    if inside(ball):
        speed.y -= 0.5  # Aumenta la gravedad para un movimiento más rápido
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    ontimer(move, 30)  # Disminuye el intervalo de tiempo para mayor velocidad

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

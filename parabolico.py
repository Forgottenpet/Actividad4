from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200) #posicion inicial de la pelota
speed = vector(0, 0) #velocidad inicial de la pelota roja
targets = [] #lista para almacenar los objetivos

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15  #aumenta la velocidad, pasando la posicion a una velocidad. Se cambio el 25 por un 15
        speed.y = (y + 200) / 15  #aumenta la velocidad, pasando la posicion a una velocidad. Se cambio el 25 por un 15

def inside(xy):  #verifica si un punto esta dentro del rango de la pantalla
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw(): #funcion que dibuja los objetivos
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue') #dibuja los objetivos en azul

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red') #dibuja la pelota roja

    update()

def move(): 
    "Move ball and targets." #los objetivos aparecen en pantalla 
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 3.2 #reduce el eje x en 3.2 unidades. Por lo que da la sensación de ir más rápido

    if inside(ball):
        speed.y -= 0.5 #aumentamos el valor en y, para que en el mov en y sea más rápido
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 35) #disminuimos el intervalo del tiempo a 35 para mayor velocidad

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

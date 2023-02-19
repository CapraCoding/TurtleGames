import random
from turtle import Screen, Turtle
colors = ['Blue', 'Red', 'Violet', 'Yellow', 'Brown', 'Green']

#setup screen
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)

#Pedindo pra qual tartaruga irá torcer
user_turtle = screen.textinput(title="Faça a aposta", prompt=f'Escolha a tartaruga para apostar: \n {colors}')

#Colocando posições do Y das tartarugas
y_loc = [-30, 0, 30, 60, 90, 120]

is_the_race_on = False

all_turtles = []
used = []

#Criando tartarugas
for turtle_index in range(0,6):

    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    #Randomizando cores
    cor_random = random.choice([x for x in colors if x not in used])
    used.append(cor_random)
    new_turtle.color(cor_random)

    #Posição tartaruga
    new_turtle.goto(-240, y= y_loc[turtle_index])
    #Adicionando ela na lista
    all_turtles.append(new_turtle)


if user_turtle:
    is_the_race_on = True

#Randomizando a distancia que irá percorrer
while is_the_race_on:
    for turtle in all_turtles:
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            is_the_race_on = False

#Verificar se o usurio acertou
if user_turtle.lower() == win_color.lower():
    print(f"Tartaruga vencedora: {win_color}")
    print("Você acertou a tartaruga vencedoda!")
else:
    print(f"Tartaruga vencedora: {win_color}")
    print("Infelizmente você errou a vencedora!")

screen.exitonclick()
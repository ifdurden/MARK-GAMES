
import turtle
import random
HEIGHT , WIDTH = 500 , 500
COLORS = ["brown","red" , "yellow" , "green" , "blue" , "black" , "cyan" , "orange" , "purple" , "pink"]


def get_racer():
    while True :
        
        try:
            print("Please Enter a number between 2-10")
            racers = int(input("How many racer would you like : "))
            if 2 <= racers <= 10 :
                return racers 
            print("Please enter number between 2 and 10 (INCLUSIVE)")

        except ValueError:
            print("Error :Please enter a valid number!")



def racer(colors):
    turtles = create_turtle(colors)
    while True :
        for i , turtle in enumerate(turtles):
            speed = random.randrange(1,20)
            turtle.forward(speed)
            x , y = turtle.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(turtle)]


def create_turtle(colors):
    turtles =[]
    spacing = WIDTH // (len(colors) + 1)
    for i , color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing , -HEIGHT//2 + 20 )
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_screen():
    screen = turtle.Screen()
    turtle.setup(HEIGHT , WIDTH)
    turtle.title("Turtle racing!")



racers = get_racer()
init_screen()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = racer(colors)
print(f"So the winner is {winner} TURTLE!")


turtle.done()
import turtle
import random
import time
import winsound  # Windows only. For Mac/Linux: see below.

HEIGHT, WIDTH = 500, 500
COLORS = ["brown", "red", "yellow", "green", "blue", "lime", "cyan", "orange", "purple", "pink"]

def get_racer():
    while True:
        try:
            racers = int(input("How many racers would you like: "))
            if 2 <= racers <= 10:
                return racers
            print("Please enter a number between 2 and 10 (INCLUSIVE)")
        except ValueError:
            print("Please enter a valid number")


def play_beep():
    try:
        winsound.Beep(1000, 300)  # Frequency, Duration
    except:
        print("Beep skipped (sound unsupported on this system)")

def countdown(screen):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("white")
    pen.penup()
    pen.goto(0, 0)
    pen.write("Get Ready!", align="center", font=("Arial", 24, "bold"))
    time.sleep(1)
    pen.clear()

    for i in range(3, 0, -1):
        pen.write(str(i), align="center", font=("Arial", 40, "bold"))
        play_beep()
        time.sleep(1)
        pen.clear()

    pen.write("GO!", align="center", font=("Arial", 30, "bold"))
    play_beep()
    time.sleep(0.7)
    pen.clear()

def start_race(colors) -> str:
    turtles = create_turtle(colors)
    while True:
        for turtle_obj in turtles:
            speed = random.randint(1, 10)
            turtle_obj.forward(speed)
            x, y = turtle_obj.pos()
            if y >= HEIGHT // 2 - 10:
                return turtle_obj.pencolor()


def create_turtle(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.goto(-WIDTH // 2 + (i + 1) * spacing, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def init_screen():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    return screen


# MAIN PROGRAM
print("Welcome to the turtle racing game!")
print("**************************************")
num_racers = get_racer()
screen = init_screen()
random.shuffle(COLORS)
colors = COLORS[:num_racers]

countdown(screen)
winner = start_race(colors)

print("So the winner is", winner.upper(), "TURTLE!")

turtle.done()

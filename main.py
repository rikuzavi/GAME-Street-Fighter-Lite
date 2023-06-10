import turtle
import random
import time
import tkinter as tk


def instruction():
    window = tk.Tk()
    label = tk.Label(window, text="")
    label.pack()
    with open("intruction", "r") as file:
        contents = file.read()
    label.config(text=contents,font=("Arial", 15),bg="black",fg="red")
    label.pack()
    window.mainloop()

screen = turtle.Screen()
screen.setup(1000, 600)
screen.bgcolor("black")


stamp= turtle.Turtle()
stamp.hideturtle()
stamp.penup()
stamp.color("white")
stamp.goto(445, -290)
stamp.write("@Rikuzavi 2023", align="center", font=("Arial", 9, "bold"))

entry_image=turtle.Screen()
entry_image.addshape('fighter/intro_image.gif')
entry_image= turtle.Turtle()
entry_image.hideturtle()
entry_image.penup()
entry_image.shape('fighter/intro_image.gif')
entry_image.setpos(0,40)
entry_image.showturtle()

main = turtle.Turtle()
main.hideturtle()
main.penup()
main.color("red")
main.setpos(0, -255)
main.write("   ▂ ▄ ▅ ▆ ▇ █STREET FIGHTER LITE█ ▇ ▆ ▅ ▄ ▂ \n\npress START to enter the game\npress ESCAPE to exit\npress [i] to read Key Bindings\n\nSelect level\n1 : easy   |   2: Medium   |   3 : Hard ", align="center", font=("Arial", 15, "bold"),)
score1 = 350
score2 = 350
level=500
def START():
    global score1,score2
    answer = screen.textinput("LEVEL", "ENTER THE DIFFICULTY LEVEL : ")
    screen.onkey(None,"Return")
    global score1,score2
    entry_image.hideturtle()
    main.clear()
    score_turtle1 = turtle.Turtle()
    score_turtle1.hideturtle()
    score_turtle1.penup()
    score_turtle1.color("white")
    score_turtle1.goto(-450, 250)
    score_turtle1.write(f"Player 1: {score1}", align="center", font=("Arial", 10, "bold"))

    score_turtle2 = turtle.Turtle()
    score_turtle2.hideturtle()
    score_turtle2.penup()
    score_turtle2.color("white")
    score_turtle2.goto(450, 250)
    score_turtle2.write(f"Player 2: {score2}", align="center", font=("Arial", 10, "bold"))

    health_bar1 = turtle.Turtle()
    health_bar1.hideturtle()
    health_bar1.shape("square")
    health_bar1.color("white")
    health_bar1.penup()
    health_bar1.goto(-480, 280)
    health_bar1.pendown()
    health_bar1.setheading(0)
    health_bar1.shapesize(1,35,0)
    health_bar1.fillcolor("red")
    health_bar1.showturtle()

    health_bar2 = turtle.Turtle()
    health_bar2.hideturtle()
    health_bar2.shape("square")
    health_bar2.color("white")
    health_bar2.penup()
    health_bar2.goto(480, 280)
    health_bar2.pendown()
    health_bar2.setheading(0)
    health_bar2.shapesize(1, 35, 0)
    health_bar2.fillcolor("red")
    health_bar2.showturtle()

    w3= turtle.Screen()
    w3.addshape('fighter/BRICK.gif')
    base= turtle.Turtle()
    base.hideturtle()
    base.penup()
    base.shape('fighter/BRICK.gif')
    base.shapesize(2, 2, 0)
    base.sety(-515)
    base.setx(0)
    base.showturtle()


    w = turtle.Screen()
    w.addshape('fighter/STAND.gif')
    w1 = turtle.Screen()
    w1.addshape('fighter/KICK.gif')
    w2 = turtle.Screen()
    w2.addshape('fighter/PUNCH.gif')
    w3= turtle.Screen()
    w3.addshape('fighter/RUN.gif')
    player = turtle.Turtle()
    player.hideturtle()
    player.penup()
    player.shape('fighter/STAND.gif')
    player.shapesize(2, 2, 0)
    player.sety(-165)
    player.setx(-400)
    player.showturtle()
    player.speed("fastest")

    p = turtle.Screen()
    p.addshape('fighter/STAND_2.gif')
    p1 = turtle.Screen()
    p1.addshape('fighter/KICK_2.gif')
    p2 = turtle.Screen()
    p2.addshape('fighter/PUNCH_2.gif')
    player1 = turtle.Turtle()
    player1.hideturtle()
    player1.penup()
    player1.shape('fighter/STAND_2.gif')
    player1.shapesize(2, 2, 0)
    player1.sety(-165)
    player1.setx(400)
    player1.showturtle()

    main.clear()
    main.setpos(0,0)
    main.write("3",font=("Arial", 30, "bold"))
    time.sleep(1)
    main.clear()
    main.write("2",font=("Arial", 30, "bold"))
    time.sleep(1)
    main.clear()
    main.write("1", font = ("Arial", 30, "bold"))
    time.sleep(1)
    main.clear()
    main.setpos(-45,0)
    main.write("FIGHT", font = ("Arial", 30, "bold"))
    time.sleep(0.3)
    main.clear()
    def game_over_1():
        player1.clear()
        player1.ht()
        player.clear()
        player.ht()
        main.clear()
        main.setpos(0,0)
        main.write("CONGRATULATION 🙂\nYOU  Win\n\n\npress ESC to exit and Rerun the game to play again",align="center", font=("Arial", 15, "bold"))

    def game_over_2():
        player1.clear()
        player1.ht()
        player.clear()
        player.ht()
        main.clear()
        main.setpos(0,0)
        main.write("GAME OVER 😞\nCPU  Wins\nOMAEWA MOU SHINDEIRU\n\n\n press ESC to exit and Rerun the game to play again",align="center", font=("Arial", 15, "bold"))
    def update_score1():
        score_turtle1.clear()
        score_turtle1.write(f"Player 1: {score1}", align="center", font=("Arial", 10, "bold"))
    def update_score2():
        score_turtle2.clear()
        score_turtle2.write(f"Player 2: {score2}", align="center", font=("Arial", 10, "bold"))

    def trigger_kick():
        global score2
        player.shape('fighter/KICK.gif')
        if player.distance(player1) <= 100:
            score2 -= 3
            health_bar2.shapesize(1, (score2 / 10), 0)
            update_score2()
            if score2 <=1:
                game_over_1()
                win()
                return False

    def trigger_punch():
        global score2
        player.shape('fighter/PUNCH.gif')
        if player.distance(player1) <= 100:
            score2 -= 1
            health_bar2.shapesize(1, (score2 / 10), 0)
            update_score2()
            if score2 <=1:
                game_over_1()
                win()
                return False

    def move_left():
        if player.xcor() <= -450:
            return False
        player.setx(player.xcor() - 10)

    def move_right():
        if player.distance(player1) <= 10:
            return False
        player.setx(player.xcor() + 10)

    def stand():
        player.shape('fighter/STAND.gif')

    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.onkeypress(trigger_punch, "a")
    screen.onkeypress(trigger_kick, "s")
    screen.onkeyrelease(stand, "a")
    screen.onkeyrelease(stand,"s")
    screen.listen()


    def trigger_kick1():
        global score1,score2
        if player1.xcor() <= player.xcor():
            player1.setx(player1.xcor() + 60)
        player1.shape('fighter/KICK_2.gif')
        if player1.distance(player) <= 100:
            score1 -= 4
            health_bar1.shapesize(1, (score1/10), 0)
            update_score1()

    def trigger_punch1():
        global score1,score2
        if player1.xcor() <= player.xcor():
            player1.setx(player1.xcor() + 60)
        player1.shape('fighter/PUNCH_2.gif')
        if player1.distance(player) <= 100:
            score1 -= 2
            health_bar1.shapesize(1, (score1/10), 0)
            update_score1()

    def move_left1():
        if player1.xcor() <= player.xcor():
            player1.setx(player1.xcor() + 60)
        player1.setx(player1.xcor() - 80)
    def move_right1():
        if player1.xcor() >= 450:
            return False
        player1.setx(player1.xcor() + 20)
    def stand1():
        player1.shape('fighter/STAND_2.gif')
    com_move=[move_left1,move_right1,stand1]
    def computer_movement():
        global score1,score2
        if score1<=4:
            game_over_2()
            return False
        elif score2<=1:
            game_over_1()
            win()
            return False
        else:
            fr=random.choice(com_move)
            fr()
            screen.ontimer(computer_movement, 150)
    computer_movement()
    def computer():
        global level,score2,score1
        if int(answer) == 1:
            level = 300
        elif int(answer) == 2:
            level = 150
        elif int(answer) == 3:
            level = 50
        elif int(answer) >= 4:
            level = 20
        com_fight = [trigger_punch1, trigger_kick1]
        if score1<=4:
            game_over_2()
            return False
        elif score2<=1:
            game_over_1()
            win()
            return False
        else:
            if player1.distance(player) <= 21:
                player1.setx(player1.xcor() + 10)
                computer()
            else:
                f = random.choice(com_fight)
                f()
                screen.ontimer(computer, level)
    computer()

screen.onkey(START, "Return")
screen.onkey(instruction, "i")
screen.onkey(exit, "Escape")
screen.listen()


screen.mainloop()

from turtle import Turtle,Screen
import time
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
def game_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800,height=900)
    screen.title("Advance Snake Game")
    screen.listen()
    screen.tracer(0)
    return screen
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
def create_snake():
    snake1 = Turtle()
    snake1.color("red")
    snake1.shape("square")
    snake1.penup()

    snake2 = Turtle()
    snake2.color("red")
    snake2.shape("square")
    snake2.penup()
    snake2.goto(-20,0)
    

    snake3 = Turtle()
    snake3.color("red")
    snake3.shape("square")
    snake3.penup()
    snake3.goto(-40,0)
    

    snakes = [snake1,snake2,snake3]

    return snakes
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
is_game_on = True
# Screen Setup
screen = game_screen()
# snake
snake_body = create_snake()
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
def up():
    snake_body[0].setheading(90)
    snake_body[1].setheading(90)
    snake_body[2].setheading(90)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////    
def down():
    snake_body[0].setheading(270)
    snake_body[1].setheading(270)
    snake_body[2].setheading(270)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
def left():
    snake_body[0].setheading(180)
    snake_body[1].setheading(180)
    snake_body[2].setheading(180)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
def right():
    snake_body[0].setheading(0)
    snake_body[1].setheading(0)
    snake_body[2].setheading(0)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////



screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

while is_game_on: 
    screen.update()
    time.sleep(0.1)
    # Move the snake segments from tail to head
    for seg_num in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[seg_num - 1].xcor()
        new_y = snake_body[seg_num - 1].ycor()
        snake_body[seg_num].goto(new_x, new_y)
    snake_body[0].forward(20)

# last line
screen.exitonclick()




















 # score board
    # score = Turtle()
    # score.color("white")
    # score.penup()
    # score.hideturtle()
    # score.goto(0,400)
    # score.write("Score Board Position",align="center", font=("Courier", 18, "normal"))
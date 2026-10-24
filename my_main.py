from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_SIDE_LENGTH = 600

screen = Screen()
screen.setup(width=SCREEN_SIDE_LENGTH, height=SCREEN_SIDE_LENGTH)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def bind_event_listeners():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

game_is_on = True

bind_event_listeners()

def game_ends():
    global game_is_on

    game_is_on = False

    scoreboard.game_over()
    screen.update()
    time.sleep(2)
    scoreboard.display_final_score()
    screen.update()
    time.sleep(2)
    ask_user()

def ask_user():
    user_input = screen.textinput(
        "Play again",
        "Type 'y' to play again or 'n' to quit:"
    )
    if user_input == 'y':
        restart()
    else:
        time.sleep(0.5)
        scoreboard.display_highest_score_at_last()

def restart():
    global snake, game_is_on

    for segment in snake.segment_list:
        segment.hideturtle()

    snake = Snake()

    scoreboard.score = 0
    scoreboard.clear()
    scoreboard.write_score_n_highest_score()

    bind_event_listeners()

    game_is_on = True
    game()

def game():   

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        #Detect collision with food
        if snake.head.distance(food)<15:
            food.refresh()
            snake.extend()
            scoreboard.score_tracker()
        #Detect collision with wall   
        if snake.head.xcor() < -SCREEN_SIDE_LENGTH//2 + 10 or snake.head.xcor() > SCREEN_SIDE_LENGTH//2 - 10 or snake.head.ycor() < -SCREEN_SIDE_LENGTH//2 + 10 or snake.head.ycor() > SCREEN_SIDE_LENGTH//2 - 22:
            game_ends()
        #Detect collision with tail
        for i in range(len(snake.segment_list) -1, 1, -1):
            if snake.segment_list[i].distance(snake.head) <= 10:              
                game_ends()

game()

screen.exitonclick()

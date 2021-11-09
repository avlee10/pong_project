## https://docs.python.org/3/library/turtle.html -> Turtle library documentation
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

# Creating the screen resolution
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
# Screen tracer to skip turtle animation.
screen.tracer(0)

# Creating objects.
scoreboard = Scoreboard()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()


# Create screen listeners so that right and left paddles can move.
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    #sleep determines the ball's movement speed. By increasing the ball speed, will increase how fast it "refreshes" which will increase speed.
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting ball collision against y cordinates. Y cordinates represent the upper and lower limits of the "screen walls"
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    

    # Detecting collision with paddle. The ball will find the distance between other object. Once ball is in range of either paddles, it will call another method to redirect the ball's bounce.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting when paddle misses and ball is now out of bounds.
    ## Once out of bound, it will call function to update scoreboards.
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()

from turtle import Screen
from stick import Stick
from dividing_line import DivingLine
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.title("The Air Hockey Game")
screen.setup(900, 500)
screen.bgcolor("#161724")
screen.tracer(0)


# Create two stick objects for the players, positioned on the left and right.
player_one = Stick(-420)
player_two = Stick(410)

# Create the dividing line, ball, and scoreboard objects.
line = DivingLine()
ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkeypress(player_one.move_up, "w")
screen.onkeypress(player_two.move_up, "Up")
screen.onkeypress(player_one.move_down, "s")
screen.onkeypress(player_two.move_down, "Down")
screen.onkey(ball.reset, "Escape")


game_is_on = True
while game_is_on:
    screen.update()
    # Move the ball forward one step.
    ball.move()

    # Detect collision with the top and bottom walls.
    # The y-coordinates 240 and -240 are used to account for the ball's size.
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()

    # Detect collision with the paddles.
    # The logic checks if the ball is close to a paddle AND on the correct side of the screen.
    if (
        ball.distance(player_two) < 50
        and ball.xcor() > 390
        or ball.distance(player_one) < 50
        and ball.xcor() < -390
    ):
        ball.bounce_x()

    # Detect when the ball goes past the right paddle (a goal for player one).
    if ball.xcor() > 420:
        scoreboard.l_point()
        ball.reset()

    # Detect when the ball goes past the left paddle (a goal for player two).
    if ball.xcor() < -420:
        scoreboard.r_point()
        ball.reset()


##############################
screen.exitonclick()

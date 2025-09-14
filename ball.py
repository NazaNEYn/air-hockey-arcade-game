from turtle import Turtle


class Ball(Turtle):
    """
    A class to represent the game ball.

    The ball is a subclass of the Turtle class and is responsible for its own movement,
    bouncing off walls and paddles, and resetting its position.
    """

    def __init__(self):
        """
        Initializes the Ball object.

        Sets up the ball's appearance, starting position, and initial movement speed.
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.goto(0, 0)
        # Set the initial horizontal speed.
        self.x_move = 0.2
        # Set the initial vertical speed.
        self.y_move = 0.2

    def move(self):
        """
        Moves the ball based on its current speed.

        Calculates a new position by adding the horizontal and vertical speed to the
        current coordinates and then moves the ball to that new position.
        """
        # Calculate the new x-coordinate.
        new_x = self.xcor() + self.x_move
        # Calculate the new y-coordinate.
        new_y = self.ycor() + self.y_move
        # Move the ball to the new coordinates.
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverses the ball's vertical direction.

        Multiplies the vertical speed by -1 to reverse it.
        This is used when the ball hits the top or bottom walls.
        """
        # Reverse the vertical movement direction.
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the ball's horizontal direction.

        Multiplies the horizontal speed by -1 to reverse it.
        This is used when the ball hits a paddle.
        """
        # Reverse the horizontal movement direction.
        self.x_move *= -1

    def reset(self):
        """
        Resets the ball's position to the center of the screen.

        Also reverses the horizontal direction so the ball serves to the other side.
        This is used after a player scores a goal.
        """
        self.goto(0, 0)
        # Reverse the horizontal direction for the next serve.
        self.bounce_x()

from turtle import Turtle


class Stick(Turtle):
    """
    A class to represent the paddles in the air hockey game.

    Each stick is a Turtle object and is responsible for its own position and movement,
    staying within the game boundaries.
    """

    def __init__(self, x_cor):
        """
        Initializes the Stick object.

        Args:
            x_cor: The starting x-coordinate of the stick.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.x_cor = x_cor
        self.goto(self.x_cor, 0)

    def move_up(self):
        """
        Moves the stick up.

        Checks for a boundary to prevent the stick from going off the top of the screen.
        """
        new_y = self.ycor() + 20
        # Check if the new position is within the upper boundary.
        # The value 200 accounts for the stick's size and the screen dimensions.
        if new_y < 200:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        """
        Moves the stick down.

        Checks for a boundary to prevent the stick from going off the bottom of the screen.
        """
        new_y = self.ycor() - 20
        # Check if the new position is within the lower boundary.
        # The value -180 accounts for the stick's size and the screen dimensions.
        if new_y > -180:
            self.goto(self.xcor(), new_y)

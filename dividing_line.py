from turtle import Turtle


class DivingLine(Turtle):
    """
    A class to represent the diving line in an air hockey game.

    The line is created by moving a hidden Turtle object with its pen down
    from the top to the bottom of the screen.
    """

    def __init__(self):
        """
        Initializes the DivingLine object.

        Sets up the appearance and draws the line in the center of the screen.
        """
        super().__init__()
        self.color("white")
        self.pensize(2.5)
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.pendown()
        self.goto(0, -250)
        self.penup()

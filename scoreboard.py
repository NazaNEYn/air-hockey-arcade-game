from turtle import Turtle


class Scoreboard(Turtle):
    """
    A class to represent the game's scoreboard.

    This single object manages and displays the scores for both players.
    It updates the score on the screen whenever a point is scored.
    """

    def __init__(self):
        """
        Initializes the Scoreboard object.

        Sets up the scoreboard's appearance, initial scores, and displays them.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears the old scores and displays the new ones.

        Moves the turtle to the left and right positions to write each player's score.
        """
        self.clear()
        self.goto(-370, 210)
        self.write(
            f"Score: {self.l_score}", align="center", font=("Courier", 14, "normal")
        )
        self.goto(370, 210)
        self.write(
            f"Score: {self.r_score}", align="center", font=("Courier", 14, "normal")
        )

    def l_point(self):
        """
        Increases the left player's score by one and updates the display.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increases the right player's score by one and updates the display.
        """
        self.r_score += 1
        self.update_scoreboard()

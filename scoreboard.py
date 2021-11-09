from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        #To refresh scoreboard when points have been scored.
        self.update_score()

    def update_score(self):
        """Update the scoreboard."""
        # Clear function erases the last score so that the updated score can replace it
        self.clear()
        self.goto(-100, 190)
        self.write(self.left_score, align="center", font=("Courier", 88, "normal"))
        self.goto(100, 190)
        self.write(self.right_score, align="center", font=("Courier", 88, "normal"))

    def left_point(self):
        """Add a point to the left_score"""
        self.left_score += 1
        # Updates the scoreboard
        self.update_score()

    def right_point(self):
        """Add a point to the right_score"""
        self.right_score += 1
        # Updates the scoreboard
        self.update_score()
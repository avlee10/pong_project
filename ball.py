from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        



    def move(self):
        """Function sets a y and x cordinate and has the ball move."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        """When ball hits along the y-axis, function sets the ball to opposite"""
        self.y_move *= -1


    def bounce_x(self):
        """When ball hits along x-axis, function sets the ball to opposite direction."""
        self.x_move *= -1
        self.move_speed *= .8

    def reset_position(self):
        """When ball becomes out of bounds, this function is called to reset it's position."""
        self.home()
        self.move_speed = 0.1
        self.bounce_x()



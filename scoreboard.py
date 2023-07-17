from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.score = -1
        self.update_board()

    def update_board(self):
        self.clear()
        self.score += 1
        self.write(
            arg=f"Score: {self.score}",
            move=False,
            align="center",
            font=("Consolas", 15, "bold")
        )

    def game_over(self):
        self.home()
        self.color("lawngreen")
        self.write(
            arg=f"GAME OVER",
            move=False,
            align="center",
            font=("Consolas", 25, "bold")
        )

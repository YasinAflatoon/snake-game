from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        file = open("data.txt")
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.score = -1
        self.high_score = int(file.read())
        file.close()
        self.over = Turtle()
        self.over.penup()
        self.over.hideturtle()
        self.hs = Turtle()
        self.hs.penup()
        self.hs.color("white")
        self.hs.hideturtle()
        self.hs.goto(0, 260)
        self.update_score()
        self.update_highscore(self.high_score)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(
            arg=f"Score: {self.score}",
            move=False,
            align="center",
            font=("Consolas", 15, "bold")
        )

    def update_highscore(self, score):
        self.hs.clear()
        self.high_score = score
        f = open("data.txt", mode="w")
        written_data = str(self.high_score)
        f.write(written_data)
        f.close()
        self.hs.write(
            arg=f"High score: {self.high_score}",
            move=False,
            align="center",
            font=("Consolas", 10, "bold")
        )

    def game_over(self):
        self.over.home()
        self.over.color("lawngreen")
        self.over.write(
            arg=f"GAME OVER",
            move=False,
            align="center",
            font=("Consolas", 25, "bold")
        )
        self.over.goto(0, -20)
        self.over.write(
            arg=f"Score: {self.score}",
            move=False,
            align="center",
            font=("Consolas", 17, "bold")
        )
        if self.score > self.high_score:
            self.over.goto(0, -35)
            self.over.write(
                arg=f"NEW HIGHSCORE!",
                move=False,
                align="center",
                font=("Consolas", 10, "bold")
            )
            self.update_highscore(self.score)
        self.score = -1
        self.update_score()

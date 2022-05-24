from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.high_score = 0
        #self.import_high_score()
        self.update_scoreboard()

    # def import_high_score(self):
    #     file = open("snakeGame/highscore.txt", mode="a+")
    #     content = file.read()
    #     self.high_score = int(content)
    #     file.close()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score = {self.score}    High Score = {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.update_scoreboard()
            # file = open("snakeGame/highscore.txt", mode="a+")
            # file.write(str(self.high_score))
            # file.close()
        else:
            self.score = 0
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    #def game_over(self):
       # self.goto(0, 0)
        #self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)








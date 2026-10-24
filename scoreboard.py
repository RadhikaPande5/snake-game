from turtle import Turtle

SCREEN_SIDE_LENGTH = 600

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        try:
            with open("highest_score_keeper.txt") as h_score:
                content = h_score.read().strip()
                self.highest_score = int(content) if content else 0
        except FileNotFoundError:
            self.highest_score = 0
            with open("highest_score_keeper.txt", "w") as h_score:
                h_score.write("0")
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()      
        self.write_score_n_highest_score()

    def write_score_n_highest_score(self):
        self.goto(0, SCREEN_SIDE_LENGTH / 2 - 20)

        if self.score > self.highest_score:
            self.highest_score = self.score

            with open("highest_score_keeper.txt", "w") as h_score:
                h_score.write(str(self.highest_score))

        self.write(
            f"Score : {self.score}   Highest Score: {self.highest_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def score_tracker(self):
        self.clear()
        self.score += 1
        self.write_score_n_highest_score()
    
    def game_over(self):
        self.home()
        self.write("Game over...", align=ALIGNMENT, font=FONT)

    def display_final_score(self):
        self.clear()
        self.write(f"Your final score is {self.score}.", align=ALIGNMENT, font=FONT)

    def display_highest_score_at_last(self):
        self.clear()          
        self.write(f"Highest score : {self.highest_score}.", align=ALIGNMENT, font=FONT)

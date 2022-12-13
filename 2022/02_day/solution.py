import os

from advent_handler import AdventHandler


class Solution(AdventHandler):
    def __init__(self, day=0, year=0, is_testing=False):
        super().__init__(day, year, is_testing)
        self.strategy_lines = open(self.file_path, "r").readlines()
        self.game_points = 0
        self.shape_points = 0

    def reset_points(self):
        self.game_points = 0
        self.shape_points = 0

    def answer_one(self):
        choices = {
            "X": {"points": 1, "A": 3, "B": 0, "C": 6},
            "Y": {"points": 2, "A": 6, "B": 3, "C": 0},
            "Z": {"points": 3, "A": 0, "B": 6, "C": 3},
        }
        for game in self.strategy_lines:
            player = game.split("\n")[0].split(" ")[1]
            enemy = game.split("\n")[0].split(" ")[0]
            self.game_points += choices[player][enemy]
            self.shape_points += choices[player]["points"]

        self.result_1 = self.game_points + self.shape_points
        print(f"The Answer is: {self.result_1}")
        self.reset_points()


    def answer_two(self):
        rock = {"name": "rock", "points": 1}
        paper = {"name": "paper", "points": 2}
        scissor = {"name": "scissor", "points": 3}

        rock["X"] = scissor
        rock["Y"] = rock
        rock["Z"] = paper

        paper["X"] = rock
        paper["Y"] = paper
        paper["Z"] = scissor

        scissor["X"] = paper
        scissor["Y"] = scissor
        scissor["Z"] = rock

        choices = {
            "A": rock,
            "B": paper,
            "C": scissor
        }

        player_strategy = {"X": 0, "Y": 3, "Z": 6}
        for game in self.strategy_lines:
            enemy = choices[game.split("\n")[0].split(" ")[0]]
            player = enemy[game.split("\n")[0].split(" ")[1]]
            self.game_points += player_strategy[game.split("\n")[0].split(" ")[1]]
            self.shape_points += player["points"]
        self.result_2 = self.game_points + self.shape_points
        print(f"The Answer for 2 is: {self.result_2}")
        self.reset_points()


if __name__ == "__main__":
    print(f"Start of: {__file__}")
    s = Solution()
    s.answer_one()
    s.answer_two()
    s.set_answers()

import os

from advent_handler import AdventHandler


class Solution(AdventHandler):
    def __init__(self, day, year, is_testing):
        super().__init__(day, year, is_testing)

    def answer_one(self):
        self.result_1 = 0

    def answer_two(self):
        self.result_2 = 0


if __name__ == "__main__":
    print(f"Start of: {__file__}")
    day_int = int(os.getcwd().split("\\")[-1].split("_")[0])
    year_int = int(os.getcwd().split("\\")[-2])
    s = Solution(day_int, year_int, False)
    s.answer_one()
    s.answer_two()
    s.set_answers()

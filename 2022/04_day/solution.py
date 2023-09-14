import os

from advent_handler import AdventHandler


class Solution(AdventHandler):
    def __init__(self, day=0, year=0, is_testing=False):
        super().__init__(day, year, is_testing)
        self.pairs = self.get_pairs()

    def get_pairs(self):
        pairs = []
        lines = open(self.file_path)
        for line in lines:
            line = line.split("\n")[0].split(",")
            pair_one = line[0]
            range_one = []
            for i in range(int(pair_one.split("-")[0]), int(pair_one.split("-")[1]) + 1):
                range_one.append(i)
            pair_two = line[1]
            range_two = []
            for i in range(int(pair_two.split("-")[0]), int(pair_two.split("-")[1]) + 1):
                range_two.append(i)
            sections = {"pair_one": pair_one, "pair_two": pair_two, "range_one": range_one, "range_two": range_two}
            pairs.append(sections)
        return pairs

    def answer_one(self):
        counter = 0
        for pair in self.pairs:
            counter_updated = False
            pair_range = len(pair["range_one"])
            pair_counter = 0
            for p in pair["range_one"]:
                if p in pair["range_two"]:
                    pair_counter += 1
            if pair_counter == pair_range:
                counter += 1
                counter_updated = True
            pair_range = len(pair["range_two"])
            pair_counter = 0
            for p in pair["range_two"]:
                if p in pair["range_one"]:
                    pair_counter += 1
            if pair_counter == pair_range:
                if not counter_updated:
                    counter += 1
        print(counter)
        self.result_1 = counter

    def answer_two(self):
        ol_counter = 0
        for pair in self.pairs:
            counter = 0
            for p in pair["range_one"]:
                if p in pair["range_two"]:
                    counter += 1
            for p in pair["range_two"]:
                if p in pair["range_one"]:
                    counter += 1
            if counter > 0:
                ol_counter += 1

        print(ol_counter)
        self.result_2 = ol_counter


if __name__ == "__main__":
    print(f"Start of: {__file__}")
    s = Solution()
    s.answer_one()
    s.answer_two()
    s.set_answers()

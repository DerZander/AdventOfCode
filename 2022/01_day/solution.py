from advent_handler import AdventHandler


class ElvesCalorien(AdventHandler):
    def __init__(self, day, year, is_testing):
        super().__init__(day, year, is_testing)
        self.elves = [0]
        self.get_elves()

    def get_elves(self):
        lines = open(self.file_path, "r").readlines()
        for line in lines:
            if line == "\n":
                self.elves.append(0)
            else:
                self.elves[len(self.elves) - 1] += int(line)
        return self.elves

    def answer_1(self):
        print(max(self.elves))
        self.result_1 = max(self.elves)

    def answer_2(self):
        s_elves = sorted(self.elves)
        print(s_elves[-1] + s_elves[-2] + s_elves[-3])
        self.result_2 = s_elves[-1] + s_elves[-2] + s_elves[-3]


if __name__ == "__main__":
    ec = ElvesCalorien(1, 2022, False)
    ec.answer_1()
    ec.answer_2()
    ec.set_answers()



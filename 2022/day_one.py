class ElvesCalorien():
    def __init__(self):
        self.elves = [0]
        self.get_elves()
    
    def get_elves(self):
        for line in open("2022/data/day_one.txt").readlines():
            if line == "\n":
                print("New Elve")
                self.elves.append(0)
            else:
                self.elves[len(self.elves)-1] += int(line)
        return self.elves

    def answer_1(self):
        print(max(self.elves))

    def answer_2(self):
        s_elves = sorted(self.elves)
        print(s_elves[-1] + s_elves[-2] + s_elves[-3])


if __name__ == "__main__":
    ec = ElvesCalorien()
    ec.answer_2()

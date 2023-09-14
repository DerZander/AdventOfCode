import os

from advent_handler import AdventHandler


class Solution(AdventHandler):
    def __init__(self, day=0, year=0, is_testing=False):
        super().__init__(day, year, is_testing)
        self.bagpacks = self.get_bagpack()
        self.groups = self.get_groups()

    @staticmethod
    def create_table():
        table = {}
        j = 1
        for i in range(97, 123):
            table[chr(i)] = j
            j += 1
        j = 27
        for i in range(65, 91):
            table[chr(i)] = j
            j += 1
        return table

    def get_bagpack(self):
        rucksack = open(self.file_path, "r")
        bagpacks = []
        for bagpack_line in rucksack.readlines():
            bagpack = {"total": bagpack_line.split("\n")[0]}
            bagpack["length"] = len(bagpack["total"])
            half_length = round(bagpack["length"] / 2)
            bagpack["left"] = bagpack["total"][:half_length]
            bagpack["right"] = bagpack["total"][half_length:]
            for c in bagpack["left"]:
                if c in bagpack["right"]:
                    bagpack["key"] = c
                    bagpack["priority_point"] = self.get_priority_points(c)
                    break
            bagpacks.append(bagpack)
        return bagpacks

    def get_groups(self):
        groups = []
        group = {"group_key": None, "bags": []}
        for bag in self.bagpacks:
            if len(group["bags"]) > 2:
                groups.append(group)
                group = {"key": None, "bags": []}
            group["bags"].append(bag)
        groups.append(group)

        for group in groups:
            bags = group["bags"]
            for char in bags[0]["total"]:
                if char in bags[1]["total"] and char in bags[2]["total"]:
                    group["group_key"] = char
        return groups

    def get_priority_points(self, char):
        table = self.create_table()
        return table[char]

    def answer_one(self):
        points = 0
        for bagpack in self.bagpacks:
            points += bagpack["priority_point"]
        self.result_1 = points
        print(self.result_1)

    def answer_two(self):
        points = 0
        for group in self.groups:
            points += self.get_priority_points(group["group_key"])
        self.result_2 = points
        print(self.result_2)


if __name__ == "__main__":
    print(f"Start of: {__file__}")
    s = Solution()
    s.answer_one()
    s.answer_two()
    s.set_answers()

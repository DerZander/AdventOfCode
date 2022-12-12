file_path = "./data/day_three.txt"


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


class Bagpack():
    def __init__(self):
        self.bagpacks = self.get_bagpack()
        self.groups = self.get_groups()

    def get_priority_points(self, char):
        table = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                 'm': 13,
                 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                 'y': 25,
                 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
                 'K': 37,
                 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48,
                 'W': 49,
                 'X': 50, 'Y': 51, 'Z': 52}
        return table[char]

    def get_bagpack(self):
        rucksack = open(file_path, "r")
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

    def answer_one(self):
        points = 0
        for backpack in self.bagpacks:
            points += backpack["priority_point"]
        return points

    def answer_two(self):
        points = 0
        print(self.groups)
        for group in self.groups:
            points += self.get_priority_points(group["group_key"])
        return points

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


if __name__ == "__main__":
    print(f"Start of: {__file__}")

    bagpack = Bagpack()
    print(f"Answer One: {bagpack.answer_one()}")
    print(f"Answer Two: {bagpack.answer_two()}")



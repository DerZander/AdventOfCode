from advent_handler import AdventHandler


class SectionCleanup(AdventHandler):
    def __init__(self, day, year, is_testing):
        super().__init__(day, year, is_testing)
        self.section_pairs = self.get_section_pairs()

    def get_section_pairs(self):
        section_pairs = []
        sections_list = open(self.file_path, "r").readlines()
        for sl in sections_list:
            section = {}
            section_pair = sl.split("\n")[0].split(",")
            section["one"] = {"range": section_pair[0], "numbers": []}
            section["two"] = {"range": section_pair[1], "numbers": []}
            for s_char in ["one", "two"]:
                range_one = section[s_char]["range"].split("-")[0]
                range_two = section[s_char]["range"].split("-")[1]
                for n in range(int(range_one), int(range_two) + 1):
                    section[s_char]["numbers"].append(n)

            section_pairs.append(section)
        return section_pairs

    def answer_one(self):
        print(self.section_pairs)
        counter = 0
        for section_pair in self.section_pairs:
            for section in section_pair["one"]["numbers"]:
                if int(section_pair["two"]["range"].split("-")[1]) > section > int(
                        section_pair["two"]["range"].split("-")[0]):
                    counter += 1
                    break
        print(counter)

    def answer_two(self):
        pass


if __name__ == "__main__":
    print(f"Start of: {__file__}")
    sc = SectionCleanup(4, 2022, False)
    sc.answer_one()
    sc.answer_two()

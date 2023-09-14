import datetime
import json
import os

import requests
from dotenv import load_dotenv


def get_day_name(value):
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
               17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty-one', 22: 'twenty-two',
               23: 'twenty-three', 24: 'twenty-four', 25: 'twenty-five'}
    return numbers[value]


class AdventHandler:
    def __init__(self, day=0, year=0, is_testing=False):
        load_dotenv()
        self.day = day
        self.year = year
        self.is_testing = is_testing
        self.result_1 = 0
        self.result_2 = 0
        self.file_path = self.get_file_path()
        self.setup()

    def setup(self):
        if self.day == 0:
            self.day = int(os.getcwd().split("\\")[-1].split("_")[0])
        if self.year == 0:
            self.year = int(os.getcwd().split("\\")[-2])

    def get_file(self):
        return self.file_path

    def get_file_path(self):
        file = ""
        if self.is_testing:
            file += "test_"
        file += "data.txt"
        file_path = os.path.join(os.getcwd(), file)
        return file_path

    def create_day(self, day=None, year=None):
        if year is None:
            year = self.year
        if day is None:
            day = self.day

        # Set session for getting Data
        session = os.getenv("SESSION_COOKIE")
        s = requests.Session()
        s.cookies.set("session", session)

        # Create Folder, Data and Solution
        path = os.path.join(os.getcwd(), f"{year}/{day:02}_day")
        if not os.path.exists(path):
            os.mkdir(path)
        open(f"{path}/__init__.py", "w")

        if not os.path.exists(f"{path}/solution.py"):
            open(f"{path}/solution.py", "w").close()

        if len(open(f"{path}/solution.py", "r").readlines()) == 0:
            with open(f"{path}/solution.py", "w") as f:
                blueprint = open("blueprint_solution.txt", "r").read()
                f.write(blueprint)
        open(f"{path}/test_data.txt", "w")
        if len(open(f"{path}/data.txt", "r").readlines()) == 0:
            with open(f"{path}/data.txt", "w") as f:
                f.write(s.get(f"https://adventofcode.com/{year}/day/{day}/input").text)
        print(f"The day {get_day_name(day)} was created.")

    def create_days(self):
        for i in range(1, int(datetime.datetime.now().strftime("%d")) + 1):
            self.create_day(day=i, year=self.year)

    # Create Result.txt with the answer

    def set_answers(self):
        path = os.path.join(os.getcwd(), f"{self.year}/{self.day:02}_day")
        if str(self.year) in path:
            path = f"{os.getcwd()}"
        with open(f"{path}/result.json", "w") as f:
            json.dump({'answer_1': self.result_1, 'answer_2': self.result_2}, f)
        self.update_readme(self.day)
        return True

    def create_current_day(self):
        day = int(datetime.datetime.now().strftime("%d"))
        year = int(datetime.datetime.now().strftime("%y"))
        self.create_day(day=day, year=year)

    def update_readme(self, day, year):
        rd_list = {}
        rm = open("README.md", "r").read()
        # for line in open("README.md", "r").readlines():
        #     if "###" in line:
        #         rd_list[int(line.split(" ")[1].split("\n")[0])] = []
        #     if "Day" in line:
        #         print(line.split(" "))
        #         if len(line.split(" ")) > 4:
        #             d = {line.split(" ")[-1].split("\n")[0]: line.split(" ")[1 - 2]}
        #         else:
        #             d = {line.split(" ")[-1].split("\n")[0]: line.split(" ")[1]}
        #         print(d)
        if not f"- [x] Day {day}" in rm:
            with open("README.md", "a") as f:
                f.write(f"- [x] Day {day}\n")
        print(rd_list)

    def create_readme(self):
        with open("README.md", "a") as f:
            f.write("#")


if __name__ == "__main__":
    ah = AdventHandler(day=1, year=2022, is_testing=True)
    ah.update_readme(5, 2022)
    # ah.create_current_day()

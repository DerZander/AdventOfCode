file_path = "./data/day_two.txt"


def answer_one():
    choices = {
        "X": {"points": 1, "A": 3, "B": 0, "C": 6},
        "Y": {"points": 2, "A": 6, "B": 3, "C": 0},
        "Z": {"points": 3, "A": 0, "B": 6, "C": 3},
    }
    game_points = 0
    shape_points = 0
    for game in open(file_path, "r").readlines():
        player = game.split("\n")[0].split(" ")[1]
        enemy = game.split("\n")[0].split(" ")[0]

        game_points += choices[player][enemy]
        shape_points += choices[player]["points"]
    print(f"The Answer is: {game_points + shape_points}")


def answer_two():
    # x = lose
    # y = draw
    # z = win

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
    game_points = 0
    shape_points = 0
    for game in open(file_path, "r").readlines():
        enemy = choices[game.split("\n")[0].split(" ")[0]]
        player = enemy[game.split("\n")[0].split(" ")[1]]
        game_points += player_strategy[game.split("\n")[0].split(" ")[1]]
        shape_points += player["points"]
    print(f"The Answer for 2 is: {game_points + shape_points}")


if __name__ == "__main__":
    print(f"Start of: {__file__}")
    answer_one()  # 14297
    answer_two()  # 10498

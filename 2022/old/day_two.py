rock = {"name": "rock", "points": 1}
paper = {"name": "paper", "points": 2}
scissors = {"name": "scissors", "points": 3}

rock["others"] = {rock["name"]: 3, paper["name"]: 0, scissors["name"]: 6}
paper["others"] = {paper["name"]: 3, scissors["name"]: 0, rock["name"]: 6}
scissors["others"] = {scissors["name"]: 3, rock["name"]: 0, paper["name"]: 6}

rock["weakness"] = paper
paper["weakness"] = scissors
scissors["weakness"] = rock

rock["draw"] = rock
paper["draw"] = paper
scissors["draw"] = scissors


if __name__ == "__main__":
    choices = {"A": rock, "B": paper, "C": scissors, "X": rock, "Y": paper, "Z": scissors}

    opponent_points = 0
    my_points = 0
    moves = 0

    strategies = open("2022/data/day_two.txt").readlines()

    for _strategy in strategies:
        strategy = _strategy.split("\n")[0].split(" ")
        my_strategy = choices[strategy[0]]
        opponent_strategy = choices[strategy[1]]
        game_points = my_strategy["others"][opponent_strategy["name"]]
        my_points += game_points + my_strategy["points"]
        moves += 1
    print(f"Moves: {moves}, Points: {my_points}")

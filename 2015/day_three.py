if __name__ == "__main__":
    print("Day 3")
    x = 0
    y = 0
    house_list = [f"{x}|{y}"]
    santa_houses = {house_list[-1]: 1}
    robo_houses = {house_list[-1]: 1}
    for move in open("data/day_three.txt").read():
        if move == ">":
            x += 1
        elif move == "v":
            y += 1
        elif move == "<":
            x -= 1
        elif move == "^":
            y -= 1
        house_list.append(f"{x}|{y}")
        if santa_houses.get(house_list[-1]) is None:
            santa_houses[house_list[-1]] = 1
        else:
            santa_houses[house_list[-1]] += 1

    counter = 0
    for house in house_list:
        if santa_houses[house] == 1:
            counter += 1
    print(counter)
    print(len(santa_houses))

if __name__ == "__main__":
    moves = open("data/day_one.txt").read()
    moved = 0
    floor = 0
    for move in moves:
        if move == "(":
            floor += 1
        elif move == ")":
            floor -= 1
        moved += 1
        if floor == -1:
            print(f"Erste mal im Keller: {moved}")
    print(f"Stockwerk: {floor}")


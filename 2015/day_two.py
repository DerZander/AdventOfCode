print("Day 2")
total_square_feet = 0
total_ribbon = 0
for present in open("data/day_two.txt").readlines():
    l, w, h = (present.split("x"))
    l = int(l)
    w = int(w)
    h = int(h)

    square_l = l*w
    square_w = w*h
    square_h = h*l

    square_slack = min(square_l, square_w, square_h)
    square = square_l*2 + square_w*2 + square_h*2

    square_feet = square + square_slack
    total_square_feet += square_feet

    s_1 = sorted([l, w, h])[0]
    s_2 = sorted([l, w, h])[1]
    ribbon = s_1*2 + s_2*2
    ribbon_bow = l * w * h
    total_ribbon += ribbon + ribbon_bow

print(f"Answer 1: {total_square_feet}")
print(f"Answer 2: {total_ribbon}")
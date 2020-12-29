import math


def compare_leds(all_lit, some_lit):
    relevant = []
    for s in some_lit:
        closest = all_lit[0]
        dist = math.sqrt((closest[0] - s[0]) ** 2 + (closest[1] - s[1]) ** 2)
        for a in all_lit:
            new_dist = math.sqrt((a[0] - s[0]) ** 2 + (a[1] - s[1]) ** 2)
            if new_dist < dist:
                closest = a
                dist = new_dist
        relevant.append(closest)
    binary = ""
    for a in all_lit:
        binary += "1" if a in relevant else "0"
    return binary


# print(compare_leds([[0, 0], [2, 0], [4, 0], [6, 0], [8, 0]], [[0.1, -0.1], [3.9, -0.1], [8.4, -0.1]]))

def min_directions_count(direction_str: str):
    directions = {}

    for i in range(len(direction_str)):
        if direction_str[i] in directions.keys():
            directions[direction_str[i]] = directions[direction_str[i]] + 1
        else:
            directions[direction_str[i]] = 1

    min_directions = min(directions.values())

    return min_directions if (min_directions != len(direction_str)) else 0


for str_input in ["^<^<^<", "<<<<<<", "^<<^<<", "^^<^^^"]:
    print(str_input + " :: ", min_directions_count(str_input))

def count_of_char(s: str, c: str):
    count = 0

    for i in range(len(s)):
        if s[i] == c:
            count += 1

    return count


print("Given character occurrence in string ::", count_of_char("pradip", "p"))

# Output:
# ---------
# Given character occurrence in string :: 2

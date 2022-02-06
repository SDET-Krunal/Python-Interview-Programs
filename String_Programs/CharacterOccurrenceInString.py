def count_of_character_occurrence(s: str, c: str):
    count = 0

    for i in range(len(s)):
        if s[i] == c:
            count += 1

    return count


print("Given character occurrence in string ::", count_of_character_occurrence("pradip", "p"))

# Output:
# ---------
# Given character occurrence in string :: 2

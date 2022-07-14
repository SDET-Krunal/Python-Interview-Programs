def count_of_character_occurrence(s: str) -> dict:
    result = {}
    count = 1

    for i in range(len(s)):
        if s[i] != " ":
            if s[i] in result.keys():
                result[s[i]] = result.get(s[i]) + 1
            else:
                result[s[i]] = count

    return result


print("Given character occurrence in string :: ", count_of_character_occurrence("hello folks"))

# Output:
# ---------
# Given character occurrence in string ::  {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'f': 1, 'k': 1, 's': 1}

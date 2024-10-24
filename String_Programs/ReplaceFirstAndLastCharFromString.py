def replace_first_and_last_char_with_given_char(string_value, char_to_be_replace):
    res = ""

    for i in range(len(string_value)):
        if i == 0:
            res = char_to_be_replace
        elif i == len(string_value) - 1:
            res += char_to_be_replace
        else:
            res += string_value[i]

    return res


input_str = "Python"
output = replace_first_and_last_char_with_given_char(input_str, "*")
print(output)

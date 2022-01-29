def remove_char(s: str, c: str):
    ns = ""

    for i in s:
        if c != i:
            ns += i

    return ns


print("Given string after removing given character ::", remove_char("krunal", 'r'))

# Output:
# ---------
# Given string after removing given character :: kunal

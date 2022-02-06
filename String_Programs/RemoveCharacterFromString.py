# Method :: 1
# ============
def remove_char_method_1(s: str, c: str):
    ns = ""

    for i in s:
        if c != i:
            ns += i

    return ns


print("Given string after removing given character ::", remove_char_method_1("Krunal", 'r'))


# Method :: 2
# ============
def remove_char_method_2(s: str, c: str):
    return s.replace(c, '')


print("Given string after removing given character ::", remove_char_method_2("Krunal", 'r'))


# Method :: 3
# ============
def remove_char_method_3(s: str, c: str):
    return s[:s.index(c)] + s[s.index(c) + 1:]


print("Given string after removing given character ::", remove_char_method_3("Krunal", 'r'))


# Method :: 4
# ============
def remove_char_method_4(s: str, c: str):
    return ''.join([s[i] for i in range(len(s)) if i != s.index(c)])


print("Given string after removing given character ::", remove_char_method_4("Krunal", 'r'))

# Output:
# ---------
# Given string after removing given character :: Kunal

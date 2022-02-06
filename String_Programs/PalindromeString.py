# Method :: 1
# ============
def is_string_palindrome_method_1(s: str):
    s = s.lower()

    if s == s[::-1]:
        print("Given string is Palindrome...")
    else:
        print("Oops!! Given string is not Palindrome...")


is_string_palindrome_method_1("Malayalam")
is_string_palindrome_method_1("Tanna")


# Method :: 2
# ============
def is_string_palindrome_method_2(s: str):
    s = s.lower()

    for i in range(0, int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            print("Oops!! Given string is not Palindrome...")
            break
    else:
        print("Given string is Palindrome...")


is_string_palindrome_method_2("Anna")
is_string_palindrome_method_2("Tanna")


# Method :: 3
# ============
def is_string_palindrome_method_3(s: str):
    s = s.lower()
    reverse_string = ''.join(reversed(s))

    if s == reverse_string:
        print("Given string is Palindrome...")
    else:
        print("Oops!! Given string is not Palindrome...")


is_string_palindrome_method_3("Radar")
is_string_palindrome_method_3("Tanna")


# Method :: 4
# ============
def is_string_palindrome_method_4(s: str):
    s = s.lower()
    reverse = ""

    for c in s:
        reverse = c + reverse

    if s == reverse:
        print("Given string is Palindrome...")
    else:
        print("Oops!! Given string is not Palindrome...")


is_string_palindrome_method_4("Noon")
is_string_palindrome_method_4("Tanna")

# Output:
# ---------
# Given string is Palindrome...
# Oops!! Given string is not Palindrome...


# Other Palindrome string examples ::
# ====================================
# - Civic
# - Madam
# - Mom
# - Refer
# - Rotator
# - Wow

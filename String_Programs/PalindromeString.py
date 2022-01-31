def is_string_palindrome(s: str):
    if s == s[::-1]:
        print("Given string is Palindrome...")
    else:
        print("Oops!! Given string is not Palindrome...")


is_string_palindrome("anna")
is_string_palindrome("tanna")

# Output:
# ---------
# Given string is Palindrome...
# Oops!! Given string is not Palindrome...

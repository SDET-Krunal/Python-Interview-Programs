a = "I like to do programming in Python"


def reverse_words_from_string(s: str) -> str:
    return " ".join(reversed(s.split()))


print("Actual String ::", a)
r = reverse_words_from_string(a)
print("Given string after reversing words ::", r)

# Output:
# ---------
# Actual String :: I like to do programming in Python
# Given string after reversing words :: Python in programming do to like I

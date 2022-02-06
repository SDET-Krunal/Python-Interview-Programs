# Method :: 1
# ============
def is_anagram_string_method_1(s1: str, s2: str):
    if len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower()):
        print("Given both strings are Anagram...")
    else:
        print("Oops!! Given both strings are not Anagram...")


is_anagram_string_method_1("Keep", "Peek")
is_anagram_string_method_1("Cat", "Take")


# Method :: 2
# ============
def is_anagram_string_method_2(s1: str, s2: str):
    if len(s1) == len(s2) and all([c in s2.lower() for c in s1.lower()]):
        print("Given both strings are Anagram...")
    else:
        print("Oops!! Given both strings are not Anagram...")


is_anagram_string_method_2("MotherInLaw", "HitlerWoman")
is_anagram_string_method_2("Gender", "General")

# Output:
# ---------
# Given both strings are Anagram...
# Oops!! Given both strings are not Anagram...


# Other Anagram strings examples ::
# ==================================
# - Silent and Listen
# - Triangle and Integral
# - Rat and Art
# - Cat and Act
# - Dog and God
# - Heart and Earth

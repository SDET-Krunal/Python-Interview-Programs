from collections import Counter


# Method :: 1
# ============
def count_of_word_occurrence_method_1(s: str) -> dict:
    return {word.strip(','): s.count(word.strip(',')) for word in s.split()}


word_occurrence_count = count_of_word_occurrence_method_1("I slit the sheet, and on the slitted sheet I sit")
print(word_occurrence_count)


# Method :: 2
# ============
def count_of_word_occurrence_method_2(s: str) -> str:
    return str(dict(Counter(s.split())))


word_occurrence_count = count_of_word_occurrence_method_2("I slit the sheet, and on the slitted sheet I sit")
print(word_occurrence_count)

import string


def get_scramble_words(words: list, mask_pattern: str) -> list:
    matched_words = []

    for word in words:
        if len(word) == len(mask_pattern):
            for i in range(len(mask_pattern)):
                if mask_pattern[i] not in string.punctuation and mask_pattern[i] == word[i]:
                    matched_words.append(word)
                else:
                    matched_words.append(word)

                break

    return matched_words


for mask_word in ["*re**", "***"]:
    print("Scramble words matched with '{}' :: {}".format(
        mask_word, get_scramble_words(["red", "dee", "cede", "reed", "creed", "decree"], mask_word)))

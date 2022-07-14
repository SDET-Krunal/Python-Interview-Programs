def reverse_number(num: int) -> int:
    reverse = 0

    while num > 0:
        reverse = 10 * reverse + (num % 10)
        num = num // 10

    return reverse


def is_palindrome_number(n: int) -> bool:
    return reverse_number(num=n) == n


for number in [12321, 123]:
    print("Is given number '{}' Palindrome :: {}".format(number, is_palindrome_number(n=number)))

# Output:
# --------
# Is given number '12321' Palindrome :: True
# Is given number '123' Palindrome :: False

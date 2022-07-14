def sum_of_n_number(n: int) -> int:
    result = 0

    while n > 0:
        result = result + n
        n = n - 1

    return result


number = 5
print("Sum of '{}' numbers :: {}".format(number, sum_of_n_number(number)))

# Output:
# --------
# Sum of '5' numbers :: 15

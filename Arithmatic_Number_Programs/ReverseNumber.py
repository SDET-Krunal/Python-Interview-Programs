actual_number = 12345


def reverse_number(num: int) -> int:
    reverse = 0

    while num > 0:
        reverse = 10 * reverse + (num % 10)
        num = num // 10

    return reverse


print("Actual number ::", actual_number)
print("Number after reversing ::", reverse_number(actual_number))

# Output:
# --------
# Actual number :: 12345
# Number after reversing :: 54321

def is_binary_number(num: int):
    while num > 0:
        rem = num % 10

        if rem != 0 and rem != 1:
            print("Oops!! Given number is not binary number...")
            break

        num = num // 10

        if num == 0:
            print("Given number is Binary number...")


is_binary_number(101015)
is_binary_number(101011)

# Output:
# --------
# Oops!! Given number is not binary number...
# Given number is Binary number...

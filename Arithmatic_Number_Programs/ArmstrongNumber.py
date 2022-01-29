def is_armstrong(num: int):
    sum_num = 0
    actual_num = num

    while num > 0:
        sum_num = sum_num + (num % 10) * (num % 10) * (num % 10)
        num = num // 10

    if sum_num == actual_num:
        print("Given number is Armstrong number...")
    else:
        print("Oops!! Given number is not Armstrong number...")


is_armstrong(371)

# Output:
# --------
# Given number is Armstrong number...

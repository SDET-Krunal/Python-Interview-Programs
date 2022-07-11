def is_perfect_number(num: int):
    sum_num = 0

    for i in range(1, num):
        r = num % i

        if r == 0:
            sum_num += i

    if sum_num == num:
        print("Perfect number...")
    else:
        print("Not Perfect...")


is_perfect_number(6)

# Output:
# --------
# Perfect number...

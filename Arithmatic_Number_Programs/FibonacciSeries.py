def fibonacci_series(num: int):
    first, second = 0, 1

    for i in range(0, num):
        if i <= 1:
            result = i
        else:
            result = first + second
            first = second
            second = result

        print(result)


fibonacci_series(5)

# Output:
# --------
# 0
# 1
# 1
# 2
# 3

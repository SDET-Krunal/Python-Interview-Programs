def is_greatest_num(a: int, b: int, c: int):
    if a > b and a > c:
        print("Greatest number ::", a)
    else:
        if b > c and b > a:
            print("Greatest number ::", b)
        else:
            print("Greatest number ::", c)


is_greatest_num(10, 20, 333)
is_greatest_num(10, 200, 33)
is_greatest_num(100, 20, 33)

# Output:
# --------
# Greatest number :: 333
# Greatest number :: 200
# Greatest number :: 100

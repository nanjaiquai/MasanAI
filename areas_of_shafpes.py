def func(shape, width=1, height=1, radius=1):
    if shape == 0:
        return width * height

    elif shape == 1:
        return 3.14 * radius ** 2

    else :
        print("아무것도")
        return 999

print("rect area =", func(0, width=10, height=2))
print("circle area =", func(1, radius=5))
print("circle area =", func(10, radius=5))
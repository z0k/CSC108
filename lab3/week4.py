def mystery(a, b):
    if a > b:
        c = a + b
    elif a < b:
        c = 2 * a + b
    else:
        c = b - 2 * a
    c = c * 10
    return c

result = mystery(12, 5)
print(result)

first = int(input('please enter the first integer '))
second = int(input('please enter the second integer '))
print(mystery(first, second))

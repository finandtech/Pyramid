def makeNumberPyramid(num):
    l = len(str(num))
    n = l * int((num + 1) / 2) + int((num + 1) / 2)
    for i in range(1, num + 1):
        if (i < 10):
                for j in range(1, n - i):
                    print(' ', end="")
    for j in range(1, i + 1):
        print(i, end=" ")
    else:
        for j in range(1, l * num - l * i):
            print(' ', end="")
    for j in range(1, i + 1):
        print(i, end=" ")
    print()


    num = eval(input("Enter the number of rows: "))

output = makeNumberPyramid(num)
print(output)

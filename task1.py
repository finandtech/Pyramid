def makeNumberPyramid(num):
    lenght = len(str(num))
    number = lenght * int((num + 1) / 2) + int((num + 1) / 2)
    for i in range(1, num + 1):
        if (i < 10):
                for j in range(1, number - i):
                    print(' ', end="")
                for j in range(1, i + 1):
                    print(i, end=" ")
        else:
            for j in range(1, lenght * num - lenght * i):
                print(' ', end="")
            for j in range(1, i + 1):
                print(i, end=" ")
        print()
    print(str(num))


num = eval(input("Enter the number of rows: "))
output = makeNumberPyramid(num)

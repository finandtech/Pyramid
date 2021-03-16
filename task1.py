def makeNumberPyramid(num):
    lenght = len(str(num))
    number = (lenght + 1) * num
    for i in range(1, num + 1):
        message = ""
        for j in range(i):
            message += str(i)+" "
        print(format(message, "^"+str(number)))
num = eval(input("Enter the number of rows: "))
output = makeNumberPyramid(num)

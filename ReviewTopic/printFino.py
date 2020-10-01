def printFib(length):
    n1= 1
    n2= 1
    if length < 2:
        print(1)
    else:
        print(n1)
        print(n2)
        for i in range(length-2):
            newN = n1 + n2
            print(newN)
            n1 = n2
            n2 = newN
        


# recussive solution
def recursiveFib(position):
    if position == 2 or position == 1:
        return 1
    else:
        return recursiveFib(position-2) + recursiveFib(position-1)


print(recursiveFib(10))


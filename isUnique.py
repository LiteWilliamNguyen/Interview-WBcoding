# isUnique
test_list = [1,3,4,5,5]

def sample1():
#print original list
    print("The original list is: " + str(test_list))

flag = 0

# checking all unique list elements
for i in range(len(test_list)):
    for i1 in range(len(test_list)):
        if i != i1:
            if test_list[i] == test_list[i1]:
                flag = 1

# printing result
if(not flag):
    print("List contains all unique elements")
else:
        print("List does not contains all unique elements")

def sample2():
    # printing original list
    print("The original list is: " + str(test_list))

    flag = 0
    # using set() + len() to check all unique list elements
    flag = len(set(test_list)) == len(test_list)

    #print result
    if(flag):
        print("List contains all unique elements")
else:
        print("List does not contains all unique elements")

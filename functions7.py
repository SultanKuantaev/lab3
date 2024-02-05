input_str = input("Enter elements separated by space: ")
mylist = [int(x) for x in input_str.split()]

def has_33(mylist):
    for i in range(len(mylist) - 1):
        if (mylist[i] == 3 and mylist[i+1] == 3):
            return True
    return False

print(has_33(mylist))  
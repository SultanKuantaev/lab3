input_str = input("Enter elements separated by space: ")
mylist = [int(x) for x in input_str.split()]

def has_007(mylist):
    for i in range(len(mylist) - 1):
        if (mylist[i] == 0 and mylist[i+1] == 0 and mylist[i+2] == 7):
            return True
    return False

print(has_007(mylist))  
input_str = input("Enter elements separated by space: ")
mylist = [int(x) for x in input_str.split()]

def uniqe(mylist):
    new = []
    for x in mylist:
        if(x not in new):
            new.append(x)
    return new

print(uniqe(mylist))
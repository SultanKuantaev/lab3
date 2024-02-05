input_str = input("Enter words separated by space: ")
mylist = [str(x) for x in input_str.split()]

def reverse(mylist):
    return mylist[::-1]


print(" ".join(reverse(mylist)))

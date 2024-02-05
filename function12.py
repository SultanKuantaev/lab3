input_str = input("Enter elements separated by space: ")
mylist = [int(x) for x in input_str.split()]

def histogram(mylist):
    new_list = []  
    for x in mylist: 
        s = "*" * x  
        new_list.append(s)  
    return new_list  

result = histogram(mylist)
for x in result:
    print(x)


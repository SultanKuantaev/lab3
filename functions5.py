from itertools import permutations

def print_permutations():
    input_str = input("Enter a string: ")
    perms = permutations(input_str)
    
    for perm in list(perms):
        print(''.join(perm))

print_permutations()

input_str = input("Enter elements separated by space: ")
mylist = [int(x) for x in input_str.split()]

def isprime(n):
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

def prime(mylist):
    primes = [x for x in mylist if isprime(x)]
    return primes

print(prime(mylist))

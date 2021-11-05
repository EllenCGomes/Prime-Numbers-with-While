def Prime(x):
    factor = 2
    if x == 2:
        return True
        
    while x % factor != 0 and factor <= x/2:
        factor = factor + 1
    if x % factor == 0:
        return False
    else:
        return True

n = int(input("Enter an integer number: "))

while n > 0:
    if Prime(n):
        print(n, "is a prime")
    else:
        print(n, "is not a prime")
    n = int(input("Enter an integer number: "))
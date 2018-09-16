from math import sqrt

N = int(input("\n List Fibonacci sequence to nth place.\n What is your n: "))

def fib(n): #Binet's formula
    fib_list = []
    root = sqrt(5)
    phi = (1 + root) / 2

    for n in range(0, n):
        bin = str(round(phi ** n / root))
        fib_list.append(bin)
    return fib_list

print(fib(N))

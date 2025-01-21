def getNthFibonacci(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    
    return getNthFibonacci(n-1) + getNthFibonacci(n-2)



print(getNthFibonacci(10))









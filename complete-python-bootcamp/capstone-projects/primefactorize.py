import math

factors = lambda n : [x for x in range(1,n+1) if not n%x]

def is_prime(n):
    if n <= 1:
        return False
         
    if n <= 3:
        return True 
    
    if n%2 == 0 or n%3 == 0:
        return False 
    
    for i in range(5, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return False 
        
    return True


def primeFactorize(n):
    values = ""

    prime_factors = list(filter(is_prime, factors(n)))
    
    counter = 0
    while n > 1:
        if n%prime_factors[counter] == 0:
            values += str(prime_factors[counter]) + "*"
            n = n/prime_factors[counter]
        else:
            counter += 1

    if values[-1] == '*':
        values = values[:-1]
    
    return values

print(primeFactorize(100))

print(primeFactorize(110))
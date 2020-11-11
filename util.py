import random

def extended_euclidean_algorithm(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp
    
    if x % y == 0:
        return (0, 1, y)
    
    p = extended_euclidean_algorithm(y, x % y)
    return (p[1], -(x // y) * p[1] + p[0], p[2])


def get_reverse_bitstring(n):
    td = ""
    while n != 0:
        td = td + str(n % 2)
        n = n // 2
    
    return td

def power_with_mod(g, a, p):
    td = get_reverse_bitstring(a)
    res = 1
    t = g
    for d in td:
        if d == '1':
            res = (res * t) % p
        t = (t * t) % p
    
    return res


def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    
    return True


def gcd(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp
    
    if y == 0:
        return x
    
    return gcd(y, x % y)


def choose_random_prime(min, max):
    result = random.randint(min, max)
    while not is_prime(result):
        result = random.randint(min, max)

    return result


def choose_random_coprime(min, max, n):
    result = random.randint(min, max)
    while gcd(n, result) != 1:
        result = random.randint(min, max)

    return result

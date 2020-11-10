def extended_euclidean_algorithm(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp
    
    if y % (x % y) == 0:
        return (1, -(x // y), x % y)
    
    p = extended_euclidean_algorithm(y, x % y)
    return (p[1], -(x // y) * p[1] + p[0], p[2])


def gcd(x, y):
    if y == 0:
        return x
    
    return gcd(y, x % y)


def power_with_mod(g, a, p):
    td = ""
    while a != 0:
        td = td + str(a % 2)
        a = a // 2

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

import random
import util

def key_gen():
    p = random.randint(10000, 32000)
    while not util.is_prime(p):
        p = random.randint(10000, 32000)
    
    q = random.randint(10000, 32000)
    while not util.is_prime(q):
        q = random.randint(10000, 32000)
    
    n = p * q
    pn = (p - 1) * (q - 1)

    e = random.randint(2, pn - 1)
    while util.gcd(pn, e) != 1:
        e = random.randint(2, pn - 1)
    
    sk = (util.extended_euclidean_algorithm(pn, e)[1] + pn) % pn

    return ((n, e), sk)


def encrypt(pk, m):
    return util.power_with_mod(m, pk[1], pk[0])


def decrypt(sk, n, c):
    return util.power_with_mod(c, sk, n)

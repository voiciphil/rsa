import util

def key_gen():
    p = util.choose_random_prime(10000, 32000)
    q = util.choose_random_prime(10000, 32000)
    n = p * q
    pn = (p - 1) * (q - 1)
    e = util.choose_random_coprime(2, pn - 1, pn) 
    sk = (util.extended_euclidean_algorithm(pn, e)[1] + pn) % pn

    return ((n, e), sk)


def encrypt(pk, m):
    return util.power_with_mod(m, pk[1], pk[0])


def decrypt(sk, n, c):
    return util.power_with_mod(c, sk, n)

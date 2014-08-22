import math
import itertools


##### NUMERIC PALINDROMES, ETC. ####

def is_palindrome(n):
	return str(n) == str(n)[::-1]


def permutations(numbers):
    perms = list(map("".join, itertools.permutations(str(numbers[0]))))

    for n in numbers:
        if str(n) not in perms:
            return False
    
    return True

##### PRIME NUMBERS ####

def factor(n):

    if n in [-1, 0, 1]:
        return []

    if n < 0:
        n = -1

    factors = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n /= p
        while n % p == 0:
            e += 1;
            n /= p

        factors.append((p, e))

    factors.sort()
    return factors
 

def trial_division(n):
    if n == 1:
        return 1

    for p in [2, 3, 5]:
        if n % p == 0:
            return p

    bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7
    i = 1

    while m <= bound and m * m <= n:
        if n % m == 0:
            return m

        m += dif[i % 8]
        i += 1

    return n


def is_prime(n):
	if(n == 2):
		return True
	if(n % 2 == 0):
		return False

	sqrtn = round(math.sqrt(n))
	for i in range(3, sqrtn):
		if( n % i == 0):
			return False

	return True


def find_nth_prime(n):
    # A good guess of how far we have to go, to include nth prime
    max = math.ceil(1.2 * n * math.log(n))

    primes = sieve_of_erastothenes(max)

    if len(primes) < n:
        print(
		    "Not enough primes were calculated (last prime in sequence was {}th = {})"
		    .format(len(primes), primes[-1]))
        return -1

    return primes[n-1]



def sieve_of_erastothenes(max):
	ps = []
	sieve = [True] * (max + 1)

	for p in range(2, max + 1):
		if sieve[p]:
			ps.append(p)
			for i in range(p * p, max + 1, p):
				sieve[i] = False

	return ps


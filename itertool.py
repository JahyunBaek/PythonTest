from itertools import islice, count

def is_prime(x):
    if x > 1:
        for i in range(2,x):
            if x % i == 0:
                return False
    else:
        return False
    return True


print(is_prime(5))
print(is_prime(8))


thousand_primes = islice((x for x in count() if is_prime(x)),1000)


print(next(thousand_primes))

print(next(thousand_primes))

print(next(thousand_primes))
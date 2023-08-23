def gen_prime(x=2):
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            yield x
        x += 1


prime_generator = gen_prime(10)
for _ in range(10):
    print(next(prime_generator), end=" ")
print("")

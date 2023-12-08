def primes(number_of_primes):
  

    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer")

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes_list = []
    num = 2
    while len(primes_list) < number_of_primes:
        if is_prime(num):
            primes_list.append(num)
        num += 1

    return primes_list
primes(10), primes(1), primes(20)  # examples from the test cases


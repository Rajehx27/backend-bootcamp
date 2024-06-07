
def sieve_of_eratosthenes(n):
    main_number_list = list(range(4, n + 1))
    prime_numbers = [2, 3]
    for num in main_number_list[:]:
        is_prime = True
        for prime in prime_numbers:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
            for multiple in range(num * 2, n + 1, num):
                if multiple in main_number_list:
                    main_number_list.remove(multiple)
    return prime_numbers
N = int(input("Enter the upper limit for the prime numbers search: "))
prime_numbers = sieve_of_eratosthenes(N)
print(f"Prime numbers up to {N}: {prime_numbers}")
print(f"Total number of prime numbers found: {len(prime_numbers)}")

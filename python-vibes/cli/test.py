
from vibes.services import is_prime_number_efficient


primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

if __name__ == "__main__":
    for num in primes :# range(1, 50):
        print(f"{num} is prime: {is_prime_number_efficient(num)}")
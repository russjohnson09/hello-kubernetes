from vibes.services import *


# array of primes up to 100
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]


# pytest --verbose -s
#print("hello")
# pytest primes functions test
def test_is_prime():
    #print("hello")

    # loop through array of primes to check if number is prime
    for i in range(len(primes)):
        #print(primes[i])
        assert is_prime_number_efficient(primes[i]) == True

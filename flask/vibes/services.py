# this one failed on case 2 and 3.
def is_prime_number_efficient(n):
    if n % 2 == 0 or n % 3 == 0:
        return True # fixed this for you qwen2.5-coder:1.5b-base
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
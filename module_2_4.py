# Teplova //
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # list
primes = [] # an empty list for prime numbers
not_primes = [] # an empty list for not prime numbers
for i in range(len(numbers)): # 0=1, 1 = 2, 2 = 3, ... 14 = 15, it is restricted by the length of the list
    print(i)
#
for i in numbers:
    if i == 1: # if the number is 1, we continue
        continue
    is_prime = True # operator # the condition, check the simplicity of the number# if 2%2>0, 3%3 , it's true, if
    for j in range(2, i): # if i = 2, j - from 2 to 2; if i = 3, j = 2 to 3, if i = 4, j = 2 to 4, if i = 5, j = 2 to 5
        # if i = 6, j = 2 to 6,.. i = 15, j = 2 to 15
        if i % j == 0:
            not_primes.append(i) # add to a list
            is_prime = False  # if 2/2 doesn't have a divide 0, it's not a prime number
            break
    if is_prime: # if the number is prime, add to a list "primes"
        primes.append(i)
print(primes)
print(not_primes)

# 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # list

primes = [] # an empty list for prime numbers

not_primes = [] # an empty list for not prime numbers

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            break
        is_prime = False
        primes.append(i)
        break
print(not_primes)
print(primes)
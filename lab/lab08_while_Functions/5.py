def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

numbers = []

while True:
    n = int(input())
    if n == 0:
        break
    numbers.append(n)

for num in numbers:
    if is_prime(num):
        print(f"{num}: prime")
    else:
        print(f"{num}: not prime")

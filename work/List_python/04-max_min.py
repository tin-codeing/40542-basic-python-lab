n = int(input())
numbers = []

for _ in range(n):
    num = int(input())
    numbers += [num]

print("มากที่สุด:", max(numbers))
print("น้อยที่สุด:", min(numbers))

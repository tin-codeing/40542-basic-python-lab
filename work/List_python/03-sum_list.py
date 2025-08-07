n = int(input())
numbers = []

for _ in range(n):
    num = int(input())
    numbers += [num]

total = sum(numbers)
print("ผลรวม:", total)

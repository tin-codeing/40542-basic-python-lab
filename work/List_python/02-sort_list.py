n = int(input())
numbers = []

for _ in range(n):
    num = int(input())
    numbers += [num]

print("ลิสต์เดิม:", numbers)
sorted_numbers = sorted(numbers)
print("ลิสต์เรียงแล้ว:", sorted_numbers)

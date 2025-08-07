set = int(input())
output = 0

for _ in range(set):
    num = int(input())
    if num > 50:
        output += 1

print("จำนวนที่มากกว่า 50:", output)

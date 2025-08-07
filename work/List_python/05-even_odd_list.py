n = int(input())
even = []
odd = []

for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even += [num]
    else:
        odd += [num]

print("เลขคู่:", even)
print("เลขคี่:", odd)

input = int(input("enter a number did you like: "))
total = 0

for i in range(1, input + 1):
    if i % 2 == 1:
        total += i

print("the answer is: ",total)

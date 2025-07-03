amount = float(input("Enter how much you spent: "))
if amount >= 2000:
    print(amount * 0.15)
elif 1000 <= amount < 2000:
    print(amount * 0.10)
elif 500 <= amount < 1000:
    print(amount * 0.05)
else:
    print(amount * 1)
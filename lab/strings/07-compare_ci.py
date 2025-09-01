text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

t1 = text1.lower()
t2 = text2.lower()

if t1 < t2:
    print("A comes before B")
elif t1 > t2:
    print("A comes after B")
else:
    print("A equals B")

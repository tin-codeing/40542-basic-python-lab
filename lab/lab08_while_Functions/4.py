x = int(input("please_enter_the_input: "))

def math(x):
    result = 1
    i = 1
    while i <= x:
        result *= i
        i += 1
    print(f"{x}! = {result}")

if 0 <= x <= 20:
    math(x)
else:
    print("error")

n = int(input("Enter_a_number_n: "))
limit = int(input("Enter_a_number_limit: "))

i = 1

def doingsomething():
    print(n,"x",limit,"=",n*i)

while i <= limit:
    doingsomething()
    i += 1
temp = int(input("enter temp: "))

if(temp <= 0):
    print("Freezing")

elif(1 <= temp <= 15):
    print("Cold")

elif(16 <= temp <= 30):
    print("Warm")

else:
    print("HOT")
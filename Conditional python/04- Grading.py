score1 = int(input("please enter score: "))
score2 = int(input("please enter score: "))
score3 = int(input("please enter score: "))


final = (score1 + score2 + score3)

if(0 <= final <= 49):
    print("F")
elif(50 <= final <= 54):
    print("D")
elif(55 <= final <= 59):
    print("D+")
elif(60 <= final <= 64):
    print("C")
elif(65 <= final <= 69):
    print("+C")
elif(70 <= final <= 74):
    print("B")
elif(75 <= final <= 79):
    print("+B")

else:
    print("A")
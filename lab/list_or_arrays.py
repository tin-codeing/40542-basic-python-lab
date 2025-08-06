Name = ["krittin","tin-tin","24504"]
print(Name[0])
print(Name[1])
print(Name[2])
Name += ["I am hamesome"]#เป็นการ add เพื่ม
print(Name[3],"\n")

Num = int(input('enter your loop: '))
NumTotal = []
for x in range(Num):
    data = int(input('Enter your Data: '))
    NumTotal += [data]
print(NumTotal)
NumTotal.sort()#จัดเรียง จากน้อยไปมาก
print(NumTotal)
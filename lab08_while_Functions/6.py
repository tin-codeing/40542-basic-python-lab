def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b
while True:
    print("\nเมนู:")
    print("1. บวกเลขสองจำนวน")
    print("2. ลบเลขสองจำนวน")
    print("3. คูณเลขสองจำนวน")
    print("4. ออก")

    choice = int(input("กรุณาเลือกเมนู (1-4): "))

    if choice == 4:
        print("จบโปรแกรม")
        break
    elif choice in [1, 2, 3]:
        a = int(input("กรอกตัวเลขที่ 1: "))
        b = int(input("กรอกตัวเลขที่ 2: "))

        if choice == 1:
            result = add(a, b)
        elif choice == 2:
            result = sub(a, b)
        elif choice == 3:
            result = mul(a, b)

        print("ผลลัพธ์:", result)
    else:
        print("เมนูไม่ถูกต้อง กรุณาเลือกใหม่")

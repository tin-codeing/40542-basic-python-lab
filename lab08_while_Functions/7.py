numbers = []

while True:
    user_input = input()
    if user_input.lower() == "end":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("กรุณากรอกตัวเลขหรือพิมพ์ 'end' เพื่อจบ")

if len(numbers) == 0:
    print("ไม่มีข้อมูล")
else:
    print("ค่าสูงสุด:", max(numbers))
    print("ค่าต่ำสุด:", min(numbers))

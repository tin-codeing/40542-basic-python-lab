import random

secret = random.randint(1, 20)
count = 0

while True:
    guess = input("ทายเลข (1-20): ")
    try:
        guess_num = int(guess)
        count += 1
        if guess_num < secret:
            print("น้อยไป")
        elif guess_num > secret:
            print("มากไป")
        else:
            print(f"ถูกต้อง! คุณทายทั้งหมด {count} ครั้ง")
            break
    except ValueError:
        print("กรุณากรอกตัวเลขระหว่าง 1 ถึง 20")

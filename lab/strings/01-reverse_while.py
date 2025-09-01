text = input("enter the text: ")
length = len(text)
loop = length - 1
copy_text = ""

while loop >= 0:
    copy_text += text[loop]
    loop -= 1

print(copy_text)

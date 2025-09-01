text = input("enter your input: ")

i = 0
while i < len(text) and (text[i].isdigit() or text[i] == '.'):
    i += 1

number = float(text[:i])
animal = text[i:]

years = 1
spotted = round(number % 1, 1)

print(f"In {years} years I have spotted {spotted} {animal}.")

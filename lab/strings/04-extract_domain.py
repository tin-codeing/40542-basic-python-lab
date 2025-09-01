text = input("Enter the line: ")

at_pos = text.find("@")
space_pos = text.find(" ", at_pos)
domain = text[at_pos + 1 : space_pos]

print(domain)

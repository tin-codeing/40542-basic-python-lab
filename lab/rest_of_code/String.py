# จะเป็นการตรวจคำ

word = 'banana'
tin = 'tin code this .python and it was good for me. "tin-tin" '

if word == 'banana':
    print('All right, banana.')

if word < 'banana':
    print('Your word '+ word + ', come before banana.')
elif word > 'banana':
    print('Your word '+ word +', come before banana.')
else:
    print('All right, banana.')

print(tin.lower())#จะเป็นตัวเล็ก
print(tin.upper())#จะเป็นตัวใหญ่

data = 'From stephen.marquard@uct.ac.za Sat Jun 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

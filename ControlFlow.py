a = 3
b = 21

if a == b:
    print(a, ' and ', b, 'are equal')
else:
    print(a, ' and ', b, 'are not equal')


while a < b:
    print(a)
    a += 5


while True:
    response = input()
    if int(response) % 7 == 0:
        break  # breaks only inner statement

a = 30
b = 21

if a == b:
    print(a, ' and ', b, 'are equal')
else:
    print(a, ' and ', b, 'are not equal')

if a <b:
    print (a , ' is less than ', b)
elif a > b :
    print ( a,' is greate than ', b)
else:
    print( a, ' equals ', b)


while a < b:
    print(a)
    a += 5


while True:
    response = input()
    if int(response) % 7 == 0:
        break  # breaks only inner most loop.In this case while loop.

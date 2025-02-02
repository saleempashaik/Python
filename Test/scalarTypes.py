print(10)

print(int(10.9))  # int converts decimal point to lower end.

# int - arbitrary precision integer
# float - 64bit floating point number 15-16 digits.
# none - the null object
# bool true/false - boolean logical values.
# bool(0) - false. any other value other than 0 is true.
# Empty collection/lists are considered as false.
# Empty strings are also false.

a = 3e7
print(a)

b = None
if b is None:
    print('b is none')
b = '01'
print('printing b '+b)
print(b == '01')
print('printing c')
c = bool(4)
d = bool(0)
dd = bool(0.0)
e = bool()

print(c)
print(d)
print(dd)
print('printing e: ')
print(e)

print(bool('False'))  # since passing non empty string to bool. Its true
print(bool('True'))
x = bool('False')
print(x)
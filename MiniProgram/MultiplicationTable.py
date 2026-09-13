
#  write a program to disply the multiplication table of any number

num = int(input('Enter the number : '))

for i in range(1, 11) :
    print(f'{num} * {i} = {num*i}')
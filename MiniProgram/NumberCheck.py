
# write a program to check if a number is positive, negative and zero

num = int(input('Enter the number : '))

if num == 0 :
    print('Number is zero')
elif num > 0 :
    print(f'{num} is positive number')
else :
    print(f'{num} is negative number')
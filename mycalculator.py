# mycalculator.py 
# This program will do addition, substruction, Multiplication and division.
# This is for Pull command check. 
# 3rd check - develop to master.

aa = int(input('Please enter your 1st number: '))
bb = int(input('Please enter your 2nd number: '))

print ('Please select options from below: \n'
       'a = addition \n'
       'b =substruction \n'
       'c = multiplication \n'
       'd = division \n')

option = input('You have selected: \n')

if option == 'a':
    print ('Sum of your 2 numbers are:', int(aa+ bb))
elif option == 'b':
    print('Substraction of your 2 numbers are:' , int(aa - bb))
elif option == 'c':
    print('Multiplication of your 2 numbers are:' , int(aa * bb))
elif option == 'd':
    print('Division of your 2 numbers are:' , float(aa / bb))

